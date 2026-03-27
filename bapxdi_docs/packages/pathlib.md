PACKAGE: pathlib
MODULE:  pathlib
VERSION: stdlib

DESCRIPTION:
Object-oriented filesystem paths.

This module provides classes to represent abstract paths and concrete
paths with operations that have semantics appropriate for different
operating systems.


PUBLIC API:

def Path(*args, **kwargs):
    PurePath subclass that can make system calls.

    Path represents a filesystem path but unlike PurePath, also offers
    methods to do system calls on path objects. Depending on your system,
    instantiating a Path will return either a PosixPath or a WindowsPath
    object. You can also instantiat

def PosixPath(*args, **kwargs):
    Path subclass for non-Windows systems.

    On a POSIX system, instantiating a Path should return this object.
    

def PurePath(*args, **kwargs):
    Base class for manipulating paths without I/O.

    PurePath represents a filesystem path and offers operations which
    don't imply any actual filesystem I/O.  Depending on your system,
    instantiating a PurePath will return either a PurePosixPath or a
    PureWindowsPath object.  You can also i

def PurePosixPath(*args, **kwargs):
    PurePath subclass for non-Windows systems.

    On a POSIX system, instantiating a PurePath should return this object.
    However, you can also instantiate it directly on any system.
    

def PureWindowsPath(*args, **kwargs):
    PurePath subclass for Windows systems.

    On a Windows system, instantiating a PurePath should return this object.
    However, you can also instantiate it directly on any system.
    

def S_ISBLK:
    S_ISBLK(mode) -> bool

Return True if mode is from a block special device file.

def S_ISCHR:
    S_ISCHR(mode) -> bool

Return True if mode is from a character special device file.

def S_ISDIR:
    S_ISDIR(mode) -> bool

Return True if mode is from a directory.

def S_ISFIFO:
    S_ISFIFO(mode) -> bool

Return True if mode is from a FIFO (named pipe).

def S_ISLNK:
    S_ISLNK(mode) -> bool

Return True if mode is from a symbolic link.

def S_ISREG:
    S_ISREG(mode) -> bool

Return True if mode is from a regular file.

def S_ISSOCK:
    S_ISSOCK(mode) -> bool

Return True if mode is from a socket.

def Sequence():
    All the operations on a read-only sequence.

    Concrete subclasses must override __new__ or __init__,
    __getitem__, and __len__.
    

def WindowsPath(*args, **kwargs):
    Path subclass for Windows systems.

    On a Windows system, instantiating a Path should return this object.
    

def urlquote_from_bytes(bs, safe='/'):
    Like quote(), but accepts a bytes object rather than a str, and does
    not perform string-to-bytes encoding.  It always returns an ASCII string.
    quote_from_bytes(b'abc def?') -> 'abc%20def%3f'
    


SOURCE:
"""Object-oriented filesystem paths.

This module provides classes to represent abstract paths and concrete
paths with operations that have semantics appropriate for different
operating systems.
"""

import fnmatch
import functools
import io
import os
import posixpath
import re
import sys
import warnings
from _collections_abc import Sequence
from errno import ENOENT, ENOTDIR, EBADF, ELOOP
from stat import S_ISDIR, S_ISLNK, S_ISREG, S_ISSOCK, S_ISBLK, S_ISCHR, S_ISFIFO
from urllib.parse import quote_from_bytes as urlquote_from_bytes


__all__ = [
    "PurePath", "PurePosixPath", "PureWindowsPath",
    "Path", "PosixPath", "WindowsPath",
    ]

#
# Internals
#

# Reference for Windows paths can be found at
# https://learn.microsoft.com/en-gb/windows/win32/fileio/naming-a-file .
_WIN_RESERVED_NAMES = frozenset(
    {'CON', 'PRN', 'AUX', 'NUL', 'CONIN$', 'CONOUT$'} |
    {f'COM{c}' for c in '123456789\xb9\xb2\xb3'} |
    {f'LPT{c}' for c in '123456789\xb9\xb2\xb3'}
)

_WINERROR_NOT_READY = 21  # drive exists but is not accessible
_WINERROR_INVALID_NAME = 123  # fix for bpo-35306
_WINERROR_CANT_RESOLVE_FILENAME = 1921  # broken symlink pointing to itself

# EBADF - guard against macOS `stat` throwing EBADF
_IGNORED_ERRNOS = (ENOENT, ENOTDIR, EBADF, ELOOP)

_IGNORED_WINERRORS = (
    _WINERROR_NOT_READY,
    _WINERROR_INVALID_NAME,
    _WINERROR_CANT_RESOLVE_FILENAME)

def _ignore_error(exception):
    return (getattr(exception, 'errno', None) in _IGNORED_ERRNOS or
            getattr(exception, 'winerror', None) in _IGNORED_WINERRORS)


@functools.cache
def _is_case_sensitive(flavour):
    return flavour.normcase('Aa') == 'Aa'

#
# Globbing helpers
#


# fnmatch.translate() returns a regular expression that includes a prefix and
# a suffix, which enable matching newlines and ensure the end of the string is
# matched, respectively. These features are undesirable for our implementation
# of PurePatch.match(), which represents path separators as newlines and joins
# pattern segments together. As a workaround, we define a slice object that
# can remove the prefix and suffix from any translate() result. See the
# _compile_pattern_lines() function for more details.
_FNMATCH_PREFIX, _FNMATCH_SUFFIX = fnmatch.translate('_').split('_')
_FNMATCH_SLICE = slice(len(_FNMATCH_PREFIX), -len(_FNMATCH_SUFFIX))
_SWAP_SEP_AND_NEWLINE = {
    '/': str.maketrans({'/': '\n', '\n': '/'}),
    '\\': str.maketrans({'\\': '\n', '\n': '\\'}),
}


@functools.lru_cache()
def _make_selector(pattern_parts, flavour, case_sensitive):
    pat = pattern_parts[0]
    if not pat:
        return _TerminatingSelector()
    if pat == '**':
        child_parts_idx = 1
        while child_parts_idx < len(pattern_parts) and pattern_parts[child_parts_idx] == '**':
            child_parts_idx += 1
        child_parts = pattern_parts[child_parts_idx:]
        if '**' in child_parts:
            cls = _DoubleRecursiveWildcardSelector
        else:
            cls = _RecursiveWildcardSelector
    else:
        child_parts = pattern_parts[1:]
        if pat == '..':
            cls = _ParentSelector
        elif '**' in pat:
            raise ValueError("Invalid pattern: '**' can only be an entire path component")
        else:
            cls = _WildcardSelector
    return cls(pat, child_parts, flavour, case_sensitive)


@functools.lru_cache(maxsize=256)
def _compile_pattern(pat, case_sensitive):
    flags = re.NOFLAG if case_sensitive else re.IGNORECASE
    return re.compile(fnmatch.translate(pat), flags).match


@functools.lru_cache()
def _compile_pattern_lines(pattern_lines, case_sensitive):
    """Compile the given pattern lines to an `re.Pattern` object.

    The *pattern_lines* argument is a glob-style pattern (e.g. '*/*.py') with
    its path separators and newlines swapped (e.g. '*\n*.py`). By using
    newlines to separate path components, and not setting `re.DOTALL`, we
    ensure that the `*` wildcard cannot match path separators.

    The returned `re.Pattern` object may have its `match()` method called to
    match a complete pattern, or `search()` to match from the right. The
    argument supplied to these methods must also have its path separators and
    newlines swapped.
    """

    # Match the start of the path, or just after a path separator
    parts = ['^']
    for part in pattern_lines.splitlines(keepends=True):
        if part == '*\n':
            part = r'.+\n'
        elif part == '*':
            part = r'.+'
        else:
            # Any other component: pass to fnmatch.translate(). We slice off
            # the common prefix and suffix added by translate() to ensure that
            # re.DOTALL is not set, and the end of the string not matched,
            # respectively. With DOTALL not set, '*' wildcards will not match
            # path separators, because the '.' characters in the pattern will
            # not match newlines.
            part = fnmatch.translate(part)[_FNMATCH_SLICE]
        parts.append(part)
    # Match the end of the path, always.
    parts.append(r'\Z')
    flags = re.MULTILINE
    if not case_sensitive:
        flags |= re.IGNORECASE
    return re.compile(''.join(parts), flags=flags)


class _Selector:
    """A selector matches a specific glob pattern part against the children
    of a given path."""

    def __init__(self, child_parts, flavour, case_sensitive):
        self.child_parts = child_parts
        if child_parts:
            self.successor = _make_selector(child_parts, flavour, case_sensitive)
            self.dironly = True
        else:
            self.successor = _TerminatingSelector()
            self.dironly = False

    def select_from(self, parent_path):
        """Iterate over all child paths of `parent_path` matched by this
        selector.  This can contain parent_path itself."""
        path_cls = type(parent_path)
        scandir = path_cls._scandir
        if not parent_path.is_dir():
            return iter([])
        return self._select_from(parent_path, scandir)


class _TerminatingSelector:

    def _select_from(self, parent_path, scandir):
        yield parent_path


class _ParentSelector(_Selector):

    def __init__(self, name, child_parts, flavour, case_sensitive):
        _Selector.__init__(self, child_parts, flavour, case_sensitive)

    def _select_from(self,  parent_path, scandir):
        path = parent_path._make_child_relpath('..')
        for p in self.successor._select_from(path, scandir):
            yield p


class _WildcardSelector(_Selector):

    def __init__(self, pat, child_parts, flavour, case_sensitive):
        _Selector.__init__(self, child_parts, flavour, case_sensitive)
        if case_sensitive is None:
            # TODO: evaluate case-sensitivity of each directory in _select_from()
            case_sensitive = _is_case_sensitive(flavour)
        self.match = _compile_pattern(pat, case_sensitive)

    def _select_from(self, parent_path, scandir):
        try:
            # We must close the scandir() object before proceeding to
            # avoid exhausting file descriptors when globbing deep trees.
            with scandir(parent_path) as scandir_it:
                entries = list(scandir_it)
        except OSError:
            pass
        else:
            for entry in entries:
                if self.dironly:
                    try:
                        if not entry.is_dir():
                            continue
                    except OSError:
                        continue
                name = entry.name
                if self.match(name):
                    path = parent_path._make_child_relpath(name)
                    for p in self.successor._select_from(path, scandir):
                        yield p


class _RecursiveWildcardSelector(_Selector):

    def __init__(self, pat, child_parts, flavour, case_sensitive):
        _Selector.__init__(self, child_parts, flavour, case_sensitive)

    def _iterate_directories(self, parent_path):
        yield parent_path
  
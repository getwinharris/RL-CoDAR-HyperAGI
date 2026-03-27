PACKAGE: threading
MODULE:  threading
VERSION: stdlib

DESCRIPTION:
Thread module emulating a subset of Java's threading model.

PUBLIC API:

def Barrier(parties, action=None, timeout=None):
    Implements a Barrier.

    Useful for synchronizing a fixed number of threads at known synchronization
    points.  Threads block on 'wait()' and are simultaneously awoken once they
    have all made that call.

    

def BoundedSemaphore(value=1):
    Implements a bounded semaphore.

    A bounded semaphore checks to make sure its current value doesn't exceed its
    initial value. If it does, ValueError is raised. In most situations
    semaphores are used to guard resources with limited capacity.

    If the semaphore is released too many times

def Condition(lock=None):
    Class that implements a condition variable.

    A condition variable allows one or more threads to wait until they are
    notified by another thread.

    If the lock argument is given and not None, it must be a Lock or RLock
    object, and it is used as the underlying lock. Otherwise, a new RLoc

def Event():
    Class implementing event objects.

    Events manage a flag that can be set to true with the set() method and reset
    to false with the clear() method. The wait() method blocks until the flag is
    true.  The flag is initially false.

    

def ExceptHookArgs(iterable=(), /):
    ExceptHookArgs

Type used to pass arguments to threading.excepthook.

def Lock:
    allocate_lock() -> lock object
(allocate() is an obsolete synonym)

Create a new lock object. See help(type(threading.Lock())) for
information about locks.

def RLock(*args, **kwargs):
    Factory function that returns a new reentrant lock.

    A reentrant lock must be released by the thread that acquired it. Once a
    thread has acquired a reentrant lock, the same thread may acquire it again
    without blocking; the thread must release it once for each time it has
    acquired it.

def Semaphore(value=1):
    This class implements semaphore objects.

    Semaphores manage a counter representing the number of release() calls minus
    the number of acquire() calls, plus an initial value. The acquire() method
    blocks if necessary until it can return without making the counter
    negative. If not given,

def Thread(group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
    A class that represents a thread of control.

    This class can be safely subclassed in a limited fashion. There are two ways
    to specify the activity: by passing a callable object to the constructor, or
    by overriding the run() method in a subclass.

    

def ThreadError:
    Unspecified run-time error.

def Timer(interval, function, args=None, kwargs=None):
    Call a function after a specified number of seconds:

            t = Timer(30.0, f, args=None, kwargs=None)
            t.start()
            t.cancel()     # stop the timer's action if it's still waiting

    

def activeCount():
    Return the number of Thread objects currently alive.

    This function is deprecated, use active_count() instead.

    

def active_count():
    Return the number of Thread objects currently alive.

    The returned count is equal to the length of the list returned by
    enumerate().

    

def currentThread():
    Return the current Thread object, corresponding to the caller's thread of control.

    This function is deprecated, use current_thread() instead.

    

def current_thread():
    Return the current Thread object, corresponding to the caller's thread of control.

    If the caller's thread of control was not created through the threading
    module, a dummy thread object with limited functionality is returned.

    

def enumerate():
    Return a list of all Thread objects currently alive.

    The list includes daemonic threads, dummy thread objects created by
    current_thread(), and the main thread. It excludes terminated threads and
    threads that have not yet been started.

    

def excepthook:
    excepthook(exc_type, exc_value, exc_traceback, thread)

Handle uncaught Thread.run() exception.

def get_ident:
    get_ident() -> integer

Return a non-zero integer that uniquely identifies the current thread
amongst other threads that exist simultaneously.
This may be used to identify per-thread resources.
Even though on some platforms threads identities may appear to be
allocated consecutive numbers starting a

def get_native_id:
    get_native_id() -> integer

Return a non-negative integer identifying the thread as reported
by the OS (kernel). This may be used to uniquely identify a
particular thread within a system.

def getprofile():
    Get the profiler function as set by threading.setprofile().

def gettrace():
    Get the trace function as set by threading.settrace().

def local:
    Thread-local data

def main_thread():
    Return the main thread object.

    In normal conditions, the main thread is the thread from which the
    Python interpreter was started.
    

def setprofile(func):
    Set a profile function for all threads started from the threading module.

    The func will be passed to sys.setprofile() for each thread, before its
    run() method is called.
    

def setprofile_all_threads(func):
    Set a profile function for all threads started from the threading module
    and all Python threads that are currently executing.

    The func will be passed to sys.setprofile() for each thread, before its
    run() method is called.
    

def settrace(func):
    Set a trace function for all threads started from the threading module.

    The func will be passed to sys.settrace() for each thread, before its run()
    method is called.
    

def settrace_all_threads(func):
    Set a trace function for all threads started from the threading module
    and all Python threads that are currently executing.

    The func will be passed to sys.settrace() for each thread, before its run()
    method is called.
    

def stack_size:
    stack_size([size]) -> size

Return the thread stack size used when creating new threads.  The
optional size argument specifies the stack size (in bytes) to be used
for subsequently created threads, and must be 0 (use platform or
configured default) or a positive integer value of at least 32,768 (32k


SOURCE:
"""Thread module emulating a subset of Java's threading model."""

import os as _os
import sys as _sys
import _thread
import functools

from time import monotonic as _time
from _weakrefset import WeakSet
from itertools import count as _count
try:
    from _collections import deque as _deque
except ImportError:
    from collections import deque as _deque

# Note regarding PEP 8 compliant names
#  This threading model was originally inspired by Java, and inherited
# the convention of camelCase function and method names from that
# language. Those original names are not in any imminent danger of
# being deprecated (even for Py3k),so this module provides them as an
# alias for the PEP 8 compliant names
# Note that using the new PEP 8 compliant names facilitates substitution
# with the multiprocessing module, which doesn't provide the old
# Java inspired names.

__all__ = ['get_ident', 'active_count', 'Condition', 'current_thread',
           'enumerate', 'main_thread', 'TIMEOUT_MAX',
           'Event', 'Lock', 'RLock', 'Semaphore', 'BoundedSemaphore', 'Thread',
           'Barrier', 'BrokenBarrierError', 'Timer', 'ThreadError',
           'setprofile', 'settrace', 'local', 'stack_size',
           'excepthook', 'ExceptHookArgs', 'gettrace', 'getprofile',
           'setprofile_all_threads','settrace_all_threads']

# Rename some stuff so "from threading import *" is safe
_start_new_thread = _thread.start_new_thread
_daemon_threads_allowed = _thread.daemon_threads_allowed
_allocate_lock = _thread.allocate_lock
_set_sentinel = _thread._set_sentinel
get_ident = _thread.get_ident
try:
    _is_main_interpreter = _thread._is_main_interpreter
except AttributeError:
    # See https://github.com/python/cpython/issues/112826.
    # We can pretend a subinterpreter is the main interpreter for the
    # sake of _shutdown(), since that only means we do not wait for the
    # subinterpreter's threads to finish.  Instead, they will be stopped
    # later by the mechanism we use for daemon threads.  The likelihood
    # of this case is small because rarely will the _thread module be
    # replaced by a module without _is_main_interpreter().
    # Furthermore, this is all irrelevant in applications
    # that do not use subinterpreters.
    def _is_main_interpreter():
        return True
try:
    get_native_id = _thread.get_native_id
    _HAVE_THREAD_NATIVE_ID = True
    __all__.append('get_native_id')
except AttributeError:
    _HAVE_THREAD_NATIVE_ID = False
ThreadError = _thread.error
try:
    _CRLock = _thread.RLock
except AttributeError:
    _CRLock = None
TIMEOUT_MAX = _thread.TIMEOUT_MAX
del _thread


# Support for profile and trace hooks

_profile_hook = None
_trace_hook = None

def setprofile(func):
    """Set a profile function for all threads started from the threading module.

    The func will be passed to sys.setprofile() for each thread, before its
    run() method is called.
    """
    global _profile_hook
    _profile_hook = func

def setprofile_all_threads(func):
    """Set a profile function for all threads started from the threading module
    and all Python threads that are currently executing.

    The func will be passed to sys.setprofile() for each thread, before its
    run() method is called.
    """
    setprofile(func)
    _sys._setprofileallthreads(func)

def getprofile():
    """Get the profiler function as set by threading.setprofile()."""
    return _profile_hook

def settrace(func):
    """Set a trace function for all threads started from the threading module.

    The func will be passed to sys.settrace() for each thread, before its run()
    method is called.
    """
    global _trace_hook
    _trace_hook = func

def settrace_all_threads(func):
    """Set a trace function for all threads started from the threading module
    and all Python threads that are currently executing.

    The func will be passed to sys.settrace() for each thread, before its run()
    method is called.
    """
    settrace(func)
    _sys._settraceallthreads(func)

def gettrace():
    """Get the trace function as set by threading.settrace()."""
    return _trace_hook

# Synchronization classes

Lock = _allocate_lock

def RLock(*args, **kwargs):
    """Factory function that returns a new reentrant lock.

    A reentrant lock must be released by the thread that acquired it. Once a
    thread has acquired a reentrant lock, the same thread may acquire it again
    without blocking; the thread must release it once for each time it has
    acquired it.

    """
    if _CRLock is None:
        return _PyRLock(*args, **kwargs)
    return _CRLock(*args, **kwargs)

class _RLock:
    """This class implements reentrant lock objects.

    A reentrant lock must be released by the thread that acquired it. Once a
    thread has acquired a reentrant lock, the same thread may acquire it
    again without blocking; the thread must release it once for each time it
    has acquired it.

    """

    def __init__(self):
        self._block = _allocate_lock()
        self._owner = None
        self._count = 0

    def __repr__(self):
        owner = self._owner
        try:
            owner = _active[owner].name
        except KeyError:
            pass
        return "<%s %s.%s object owner=%r count=%d at %s>" % (
            "locked" if self._block.locked() else "unlocked",
            self.__class__.__module__,
            self.__class__.__qualname__,
            owner,
            self._count,
            hex(id(self))
        )

    def _at_fork_reinit(self):
        self._block._at_fork_reinit()
        self._owner = None
        self._count = 0

    def acquire(self, blocking=True, timeout=-1):
        """Acquire a lock, blocking or non-blocking.

        When invoked without arguments: if this thread already owns the lock,
        increment the recursion level by one, and return immediately. Otherwise,
        if another thread owns the lock, block until the lock is unlocked. Once
        the lock is unlocked (not owned by any thread), then grab ownership, set
        the recursion level to one, and return. If more than one thread is
        blocked waiting until the lock is unlocked, only one at a time will be
        able to grab ownership of the lock. There is no return value in this
        case.

        When invoked with the blocking argument set to true, do the same thing
        as when called without arguments, and return true.

        When invoked with the blocking argument set to false, do not block. If a
        call without an argument would block, return false immediately;
        otherwise, do the same thing as when called without arguments, and
        return true.

        When invoked with the floating-point timeout argument set to a positive
        value, block for at most the number of seconds specified by timeout
        and as long as the lock cannot be acquired.  Return true if the lock has
        been acquired, false if the timeout has elapsed.

        """
        me = get_ident()
        if self._owner == me:
            self._count += 1
            return 1
        rc = self._block.acquire(blocking, timeout)
        if rc:
            self._owner = me
            self._count = 1
        return rc

    __enter__ = acquire

    def release(self):
        """Release a lock, decrementing the recursion level.

        If after the decrement it is zero, reset the lock to unlocked (not owned
        by any thread), and if any other threads are blocked waiting for the
        lock to become unlocked, allow exactly one of them to proceed. If after
        the decrement the recursion level is still nonzero, the lock remains
        locked and owned by the calling thread.

        Only call this method when the calling thread owns the lock. A
        RuntimeError is raised if this method is called when the lock is
        unlocked.

        There is no return value.

        """
        if self._owner != get_ident():
            raise RuntimeError("cannot 
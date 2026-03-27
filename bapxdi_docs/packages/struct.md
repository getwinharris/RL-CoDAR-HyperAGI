PACKAGE: struct
MODULE:  struct
VERSION: stdlib

DESCRIPTION:
Functions to convert between Python values and C structs.
Python bytes objects are used to hold the data representing the C struct
and also as format strings (explained below) to describe the layout of data
in the C struct.

The optional first format char indicates byte order, size and alignment:
  @: native order, size & alignment (default)
  =: native order, std. size & alignment
  <: little-endian, std. size & alignment
  >: big-endian, std. size & alignment
  !: same as >

The remaining chars indicate types of args and must match exactly;
these can be preceded by a decimal repeat count:
  x: pad byte (no data); c:char; b:signed byte; B:unsigned byte;
  ?: _Bool (requires C99; if not available, char is used instead)
  h:short; H:unsigned short; i:int; I:unsigned int;
  l:long; L:unsigned long; f:float; d:double; e:half-float.
Special cases (preceding decimal count indicates length):
  s:string (array of char); p: pascal string (with count byte).
Special cases (only available in nati

PUBLIC API:

def Struct:
    Struct(fmt) --> compiled struct object



def calcsize(format, /):
    Return size in bytes of the struct described by the format string.

def iter_unpack(format, buffer, /):
    Return an iterator yielding tuples unpacked from the given bytes.

The bytes are unpacked according to the format string, like
a repeated invocation of unpack_from().

Requires that the bytes length be a multiple of the format struct size.

def pack:
    pack(format, v1, v2, ...) -> bytes

Return a bytes object containing the values v1, v2, ... packed according
to the format string.  See help(struct) for more on format strings.

def pack_into:
    pack_into(format, buffer, offset, v1, v2, ...)

Pack the values v1, v2, ... according to the format string and write
the packed bytes into the writable buffer buf starting at offset.  Note
that the offset is a required argument.  See help(struct) for more
on format strings.

def unpack(format, buffer, /):
    Return a tuple containing values unpacked according to the format string.

The buffer's size in bytes must be calcsize(format).

See help(struct) for more on format strings.

def unpack_from(format, /, buffer, offset=0):
    Return a tuple containing values unpacked according to the format string.

The buffer's size, minus offset, must be at least calcsize(format).

See help(struct) for more on format strings.


SOURCE:
__all__ = [
    # Functions
    'calcsize', 'pack', 'pack_into', 'unpack', 'unpack_from',
    'iter_unpack',

    # Classes
    'Struct',

    # Exceptions
    'error'
    ]

from _struct import *
from _struct import _clearcache
from _struct import __doc__

PACKAGE: numpy
MODULE:  numpy
VERSION: 2.4.2

DESCRIPTION:

NumPy
=====

Provides
  1. An array object of arbitrary homogeneous items
  2. Fast mathematical operations over arrays
  3. Linear Algebra, Fourier Transforms, Random Number Generation

How to use the documentation
----------------------------
Documentation is available in two forms: docstrings provided
with the code, and a loose standing reference guide, available from
`the NumPy homepage <https://numpy.org>`_.

We recommend exploring the docstrings using
`IPython <https://ipython.org>`_, an advanced Python shell with
TAB-completion and introspection capabilities.  See below for further
instructions.

The docstring examples assume that `numpy` has been imported as ``np``::

  >>> import numpy as np

Code snippets are indicated by three greater-than signs::

  >>> x = 42
  >>> x = x + 1

Use the built-in ``help`` function to view a function's docstring::

  >>> help(np.sort)
  ... # doctest: +SKIP

For some objects, ``np.info(obj)`` may provide additional help.  This is
particularly 

PUBLIC API:

def abs(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    absolute(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Calculate the absolute value element-wise.

``np.abs`` is a shorthand for this function.

Parameters
----------
x : array_like
    Input array.
out : ndarray, None, or tuple of ndarray and N

def absolute(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    absolute(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Calculate the absolute value element-wise.

``np.abs`` is a shorthand for this function.

Parameters
----------
x : array_like
    Input array.
out : ndarray, None, or tuple of ndarray and N

def acos(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    arccos(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Trigonometric inverse cosine, element-wise.

The inverse of `cos` so that, if ``y = cos(x)``, then ``x = arccos(y)``.

Parameters
----------
x : array_like
    `x`-coordinate on the unit circl

def acosh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    arccosh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Inverse hyperbolic cosine, element-wise.

Parameters
----------
x : array_like
    Input array.
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which the resul

def add(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    add(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Add arguments element-wise.

Parameters
----------
x1, x2 : array_like
    The arrays to be added.
    If ``x1.shape != x2.shape``, they must be broadcastable to a common
    shape (which be

def all(a, axis=None, out=None, keepdims=<no value>, *, where=<no value>):
    
    Test whether all array elements along a given axis evaluate to True.

    Parameters
    ----------
    a : array_like
        Input array or object that can be converted to an array.
    axis : None or int or tuple of ints, optional
        Axis or axes along which a logical AND reduction is p

def allclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False):
    
    Returns True if two arrays are element-wise equal within a tolerance.

    The tolerance values are positive, typically very small numbers.  The
    relative difference (`rtol` * abs(`b`)) and the absolute difference
    `atol` are added together to compare against the absolute difference
    b

def amax(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>):
    
    Return the maximum of an array or maximum along an axis.

    `amax` is an alias of `~numpy.max`.

    See Also
    --------
    max : alias of this function
    ndarray.max : equivalent method
    

def amin(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>):
    
    Return the minimum of an array or minimum along an axis.

    `amin` is an alias of `~numpy.min`.

    See Also
    --------
    min : alias of this function
    ndarray.min : equivalent method
    

def angle(z, deg=False):
    
    Return the angle of the complex argument.

    Parameters
    ----------
    z : array_like
        A complex number or sequence of complex numbers.
    deg : bool, optional
        Return angle in degrees if True, radians if False (default).

    Returns
    -------
    angle : ndarray or scal

def any(a, axis=None, out=None, keepdims=<no value>, *, where=<no value>):
    
    Test whether any array element along a given axis evaluates to True.

    Returns single boolean if `axis` is ``None``

    Parameters
    ----------
    a : array_like
        Input array or object that can be converted to an array.
    axis : None or int or tuple of ints, optional
        Axi

def append(arr, values, axis=None):
    
    Append values to the end of an array.

    Parameters
    ----------
    arr : array_like
        Values are appended to a copy of this array.
    values : array_like
        These values are appended to a copy of `arr`.  It must be of the
        correct shape (the same shape as `arr`, excludi

def apply_along_axis(func1d, axis, arr, *args, **kwargs):
    
    Apply a function to 1-D slices along the given axis.

    Execute `func1d(a, *args, **kwargs)` where `func1d` operates on 1-D arrays
    and `a` is a 1-D slice of `arr` along `axis`.

    This is equivalent to (but faster than) the following use of `ndindex` and
    `s_`, which sets each of ``i

def apply_over_axes(func, a, axes):
    
    Apply a function repeatedly over multiple axes.

    `func` is called as `res = func(a, axis)`, where `axis` is the first
    element of `axes`.  The result `res` of the function call must have
    either the same dimensions as `a` or one less dimension.  If `res`
    has one less dimension tha

def arange(start_or_stop, /, stop=None, step=1, *, dtype=None, device=None, like=None):
    arange([start,] stop[, step,], dtype=None, *, device=None, like=None)

Return evenly spaced values within a given interval.

``arange`` can be called with a varying number of positional arguments:

* ``arange(stop)``: Values are generated within the half-open interval
  ``[0, stop)`` (in other words

def arccos(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    arccos(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Trigonometric inverse cosine, element-wise.

The inverse of `cos` so that, if ``y = cos(x)``, then ``x = arccos(y)``.

Parameters
----------
x : array_like
    `x`-coordinate on the unit circl

def arccosh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    arccosh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Inverse hyperbolic cosine, element-wise.

Parameters
----------
x : array_like
    Input array.
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which the resul

def arcsin(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    arcsin(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Inverse sine, element-wise.

Parameters
----------
x : array_like
    `y`-coordinate on the unit circle.
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which t

def arcsinh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    arcsinh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Inverse hyperbolic sine element-wise.

Parameters
----------
x : array_like
    Input array.
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which the result i

def arctan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    arctan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Trigonometric inverse tangent, element-wise.

The inverse of tan, so that if ``y = tan(x)`` then ``x = arctan(y)``.

Parameters
----------
x : array_like
out : ndarray, None, or tuple of ndarr

def arctan2(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    arctan2(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Element-wise arc tangent of ``x1/x2`` choosing the quadrant correctly.

The quadrant (i.e., branch) is chosen so that ``arctan2(x1, x2)`` is
the signed angle in radians between the ray e

def arctanh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    arctanh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Inverse hyperbolic tangent element-wise.

Parameters
----------
x : array_like
    Input array.
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which the resul

def argmax(a, axis=None, out=None, *, keepdims=<no value>):
    
    Returns the indices of the maximum values along an axis.

    Parameters
    ----------
    a : array_like
        Input array.
    axis : int, optional
        By default, the index is into the flattened array, otherwise
        along the specified axis.
    out : array, optional
        If pr

def argmin(a, axis=None, out=None, *, keepdims=<no value>):
    
    Returns the indices of the minimum values along an axis.

    Parameters
    ----------
    a : array_like
        Input array.
    axis : int, optional
        By default, the index is into the flattened array, otherwise
        along the specified axis.
    out : array, optional
        If pr

def argpartition(a, kth, axis=-1, kind='introselect', order=None):
    
    Perform an indirect partition along the given axis using the
    algorithm specified by the `kind` keyword. It returns an array of
    indices of the same shape as `a` that index data along the given
    axis in partitioned order.

    Parameters
    ----------
    a : array_like
        Array 

def argsort(a, axis=-1, kind=None, order=None, *, stable=None):
    
    Returns the indices that would sort an array.

    Perform an indirect sort along the given axis using the algorithm specified
    by the `kind` keyword. It returns an array of indices of the same shape as
    `a` that index data along the given axis in sorted order.

    Parameters
    -------

def argwhere(a):
    
    Find the indices of array elements that are non-zero, grouped by element.

    Parameters
    ----------
    a : array_like
        Input data.

    Returns
    -------
    index_array : (N, a.ndim) ndarray
        Indices of elements that are non-zero. Indices are grouped by element.
        T

def around(a, decimals=0, out=None):
    
    Round an array to the given number of decimals.

    `around` is an alias of `~numpy.round`.

    See Also
    --------
    ndarray.round : equivalent method
    round : alias for this function
    ceil, fix, floor, rint, trunc

    

def array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, ndmax=0, like=None):
    array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0,
      ndmax=0, like=None)

Create an array.

Parameters
----------
object : array_like
    An array, any object exposing the array interface, an object whose
    ``__array__`` method returns an array, or any (nested) sequence.


def array2string(a, max_line_width=None, precision=None, suppress_small=None, separator=' ', prefix='', *, formatter:
    
    Return a string representation of an array.

    Parameters
    ----------
    a : ndarray
        Input array.
    max_line_width : int, optional
        Inserts newlines if text is longer than `max_line_width`.
        Defaults to ``numpy.get_printoptions()['linewidth']``.
    precision : int

def array_equal(a1, a2, equal_nan=False):
    
    True if two arrays have the same shape and elements, False otherwise.

    Parameters
    ----------
    a1, a2 : array_like
        Input arrays.
    equal_nan : bool
        Whether to compare NaN's as equal. If the dtype of a1 and a2 is
        complex, values will be considered equal if eit

def array_equiv(a1, a2):
    
    Returns True if input arrays are shape consistent and all elements equal.

    Shape consistent means they are either the same shape, or one input array
    can be broadcasted to create the same shape as the other one.

    Parameters
    ----------
    a1, a2 : array_like
        Input arrays.

def array_repr(arr, max_line_width=None, precision=None, suppress_small=None):
    
    Return the string representation of an array.

    Parameters
    ----------
    arr : ndarray
        Input array.
    max_line_width : int, optional
        Inserts newlines if text is longer than `max_line_width`.
        Defaults to ``numpy.get_printoptions()['linewidth']``.
    precision :

def array_split(ary, indices_or_sections, axis=0):
    
    Split an array into multiple sub-arrays.

    Please refer to the ``split`` documentation.  The only difference
    between these functions is that ``array_split`` allows
    `indices_or_sections` to be an integer that does *not* equally
    divide the axis. For an array of length l that should

def array_str(a, max_line_width=None, precision=None, suppress_small=None):
    
    Return a string representation of the data in an array.

    The data in the array is returned as a single string.  This function is
    similar to `array_repr`, the difference being that `array_repr` also
    returns information on the kind of array and its data type.

    Parameters
    -----

def asanyarray(a, dtype=None, order=None, *, device=None, copy=None, like=None):
    asanyarray(a, dtype=None, order=None, *, device=None, copy=None, like=None)

Convert the input to an ndarray, but pass ndarray subclasses through.

Parameters
----------
a : array_like
    Input data, in any form that can be converted to an array.  This
    includes scalars, lists, lists of tuples, 

def asarray(a, dtype=None, order=None, *, device=None, copy=None, like=None):
    asarray(a, dtype=None, order=None, *, device=None, copy=None, like=None)

Convert the input to an array.

Parameters
----------
a : array_like
    Input data, in any form that can be converted to an array.  This
    includes lists, lists of tuples, tuples, tuples of tuples, tuples
    of lists and n

def asarray_chkfinite(a, dtype=None, order=None):
    Convert the input to an array, checking for NaNs or Infs.

    Parameters
    ----------
    a : array_like
        Input data, in any form that can be converted to an array.  This
        includes lists, lists of tuples, tuples, tuples of tuples, tuples
        of lists and ndarrays.  Success requi

def ascontiguousarray(a, dtype=None, *, like=None):
    ascontiguousarray(a, dtype=None, *, like=None)

Return a contiguous array (ndim >= 1) in memory (C order).

Parameters
----------
a : array_like
    Input array.
dtype : str or dtype object, optional
    Data-type of returned array.
like : array_like, optional
    Reference object to allow the creat

def asfortranarray(a, dtype=None, *, like=None):
    asfortranarray(a, dtype=None, *, like=None)

Return an array (ndim >= 1) laid out in Fortran order in memory.

Parameters
----------
a : array_like
    Input array.
dtype : str or dtype object, optional
    By default, the data-type is inferred from the input data.
like : array_like, optional
    Re

def asin(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    arcsin(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Inverse sine, element-wise.

Parameters
----------
x : array_like
    `y`-coordinate on the unit circle.
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which t

def asinh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    arcsinh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Inverse hyperbolic sine element-wise.

Parameters
----------
x : array_like
    Input array.
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which the result i

def asmatrix(data, dtype=None):
    
    Interpret the input as a matrix.

    Unlike `matrix`, `asmatrix` does not make a copy if the input is already
    a matrix or an ndarray.  Equivalent to ``matrix(data, copy=False)``.

    Parameters
    ----------
    data : array_like
        Input data.
    dtype : data-type
       Data-type

def astype(x, dtype, /, *, copy=True, device=None):
    
    Copies an array to a specified data type.

    This function is an Array API compatible alternative to
    `numpy.ndarray.astype`.

    Parameters
    ----------
    x : ndarray
        Input NumPy array to cast. ``array_likes`` are explicitly not
        supported here.
    dtype : dtype
     

def atan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    arctan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Trigonometric inverse tangent, element-wise.

The inverse of tan, so that if ``y = tan(x)`` then ``x = arctan(y)``.

Parameters
----------
x : array_like
out : ndarray, None, or tuple of ndarr

def atan2(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    arctan2(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Element-wise arc tangent of ``x1/x2`` choosing the quadrant correctly.

The quadrant (i.e., branch) is chosen so that ``arctan2(x1, x2)`` is
the signed angle in radians between the ray e

def atanh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    arctanh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Inverse hyperbolic tangent element-wise.

Parameters
----------
x : array_like
    Input array.
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which the resul

def atleast_1d(*arys):
    
    Convert inputs to arrays with at least one dimension.

    Scalar inputs are converted to 1-dimensional arrays, whilst
    higher-dimensional inputs are preserved.

    Parameters
    ----------
    arys1, arys2, ... : array_like
        One or more input arrays.

    Returns
    -------
    re

def atleast_2d(*arys):
    
    View inputs as arrays with at least two dimensions.

    Parameters
    ----------
    arys1, arys2, ... : array_like
        One or more array-like sequences.  Non-array inputs are converted
        to arrays.  Arrays that already have two or more dimensions are
        preserved.

    Returns

def atleast_3d(*arys):
    
    View inputs as arrays with at least three dimensions.

    Parameters
    ----------
    arys1, arys2, ... : array_like
        One or more array-like sequences.  Non-array inputs are converted to
        arrays.  Arrays that already have three or more dimensions are
        preserved.

    Ret

def average(a, axis=None, weights=None, returned=False, *, keepdims=<no value>):
    
    Compute the weighted average along the specified axis.

    Parameters
    ----------
    a : array_like
        Array containing data to be averaged. If `a` is not an array, a
        conversion is attempted.
    axis : None or int or tuple of ints, optional
        Axis or axes along which to

def bartlett(M):
    
    Return the Bartlett window.

    The Bartlett window is very similar to a triangular window, except
    that the end points are at zero.  It is often used in signal
    processing for tapering a signal, without generating too much
    ripple in the frequency domain.

    Parameters
    --------

def base_repr(number, base=2, padding=0):
    
    Return a string representation of a number in the given base system.

    Parameters
    ----------
    number : int
        The value to convert. Positive and negative values are handled.
    base : int, optional
        Convert `number` to the `base` number system. The valid range is 2-36,
  

def binary_repr(num, width=None):
    
    Return the binary representation of the input number as a string.

    For negative numbers, if width is not given, a minus sign is added to the
    front. If width is given, the two's complement of the number is
    returned, with respect to that width.

    In a two's-complement system negati

def bincount(x, /, weights=None, minlength=0):
    bincount(x, /, weights=None, minlength=0)

Count number of occurrences of each value in array of non-negative ints.

The number of bins (of size 1) is one larger than the largest value in
`x`. If `minlength` is specified, there will be at least this number
of bins in the output array (though it will

def bitwise_and(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    bitwise_and(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Compute the bit-wise AND of two arrays element-wise.

Computes the bit-wise AND of the underlying binary representation of
the integers in the input arrays. This ufunc implements the

def bitwise_count(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    bitwise_count(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Computes the number of 1-bits in the absolute value of ``x``.
Analogous to the builtin `int.bit_count` or ``popcount`` in C++.

Parameters
----------
x : array_like, unsigned int
    In

def bitwise_invert(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    invert(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Compute bit-wise inversion, or bit-wise NOT, element-wise.

Computes the bit-wise NOT of the underlying binary representation of
the integers in the input arrays. This ufunc implements the C/P

def bitwise_left_shift(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    left_shift(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Shift the bits of an integer to the left.

Bits are shifted to the left by appending `x2` 0s at the right of `x1`.
Since the internal representation of numbers is in binary format, th

def bitwise_not(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    invert(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Compute bit-wise inversion, or bit-wise NOT, element-wise.

Computes the bit-wise NOT of the underlying binary representation of
the integers in the input arrays. This ufunc implements the C/P

def bitwise_or(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    bitwise_or(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Compute the bit-wise OR of two arrays element-wise.

Computes the bit-wise OR of the underlying binary representation of
the integers in the input arrays. This ufunc implements the C/

def bitwise_right_shift(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    right_shift(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Shift the bits of an integer to the right.

Bits are shifted to the right `x2`.  Because the internal
representation of numbers is in binary format, this operation is
equivalent to d

def bitwise_xor(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    bitwise_xor(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Compute the bit-wise XOR of two arrays element-wise.

Computes the bit-wise XOR of the underlying binary representation of
the integers in the input arrays. This ufunc implements the

def blackman(M):
    
    Return the Blackman window.

    The Blackman window is a taper formed by using the first three
    terms of a summation of cosines. It was designed to have close to the
    minimal leakage possible.  It is close to optimal, only slightly worse
    than a Kaiser window.

    Parameters
    ----

def block(arrays):
    
    Assemble an nd-array from nested lists of blocks.

    Blocks in the innermost lists are concatenated (see `concatenate`) along
    the last dimension (-1), then these are concatenated along the
    second-last dimension (-2), and so on until the outermost list is reached.

    Blocks can be of

def bmat(obj, ldict=None, gdict=None):
    
    Build a matrix object from a string, nested sequence, or array.

    Parameters
    ----------
    obj : str or array_like
        Input data. If a string, variables in the current scope may be
        referenced by name.
    ldict : dict, optional
        A dictionary that replaces local opera

def bool(value=False, /):
    Boolean type (True or False), stored as a byte.

.. warning::

    The :class:`bool` type is not a subclass of the :class:`int_` type
    (the :class:`bool` is not even a number type). This is different
    than Python's default implementation of :class:`bool` as a
    sub-class of :class:`int`.

:C

def bool_(value=False, /):
    Boolean type (True or False), stored as a byte.

.. warning::

    The :class:`bool` type is not a subclass of the :class:`int_` type
    (the :class:`bool` is not even a number type). This is different
    than Python's default implementation of :class:`bool` as a
    sub-class of :class:`int`.

:C

def broadcast(*arrays):
    Produce an object that mimics broadcasting.

Parameters
----------
in1, in2, ... : array_like
    Input parameters.

Returns
-------
b : broadcast object
    Broadcast the input parameters against one another, and
    return an object that encapsulates the result.
    Amongst others, it has ``shape`

def broadcast_arrays(*args, subok=False):
    
    Broadcast any number of arrays against each other.

    Parameters
    ----------
    *args : array_likes
        The arrays to broadcast.

    subok : bool, optional
        If True, then sub-classes will be passed-through, otherwise
        the returned arrays will be forced to be a base-clas

def broadcast_shapes(*args):
    
    Broadcast the input shapes into a single shape.

    :ref:`Learn more about broadcasting here <basics.broadcasting>`.

    .. versionadded:: 1.20.0

    Parameters
    ----------
    *args : tuples of ints, or ints
        The shapes to be broadcast against each other.

    Returns
    -------


def broadcast_to(array, shape, subok=False):
    Broadcast an array to a new shape.

    Parameters
    ----------
    array : array_like
        The array to broadcast.
    shape : tuple or int
        The shape of the desired array. A single integer ``i`` is interpreted
        as ``(i,)``.
    subok : bool, optional
        If True, then sub-cl

def busday_count(begindates, enddates, weekmask='1111100', holidays=(), busdaycal=None, out=None):
    busday_count(
    begindates,
    enddates,
    weekmask='1111100',
    holidays=[],
    busdaycal=None,
    out=None
)

Counts the number of valid days between `begindates` and
`enddates`, not including the day of `enddates`.

If ``enddates`` specifies a date value that is earlier than the
correspo

def busday_offset(dates, offsets, roll='raise', weekmask='1111100', holidays=None, busdaycal=None, out=None):
    busday_offset(
    dates,
    offsets,
    roll='raise',
    weekmask='1111100',
    holidays=None,
    busdaycal=None,
    out=None,
)

First adjusts the date to fall on a valid day according to
the ``roll`` rule, then applies offsets to the given dates
counted in valid days.

Parameters
----------

def busdaycalendar(weekmask='1111100', holidays=None):
    busdaycalendar(weekmask='1111100', holidays=None)

A business day calendar object that efficiently stores information
defining valid days for the busday family of functions.

The default valid days are Monday through Friday ("business days").
A busdaycalendar object can be specified with any set of 

def byte(value=0, /):
    Signed integer type, compatible with C ``char``.

:Character code: ``'b'``
:Canonical name: `numpy.byte`
:Alias on this platform (Linux x86_64): `numpy.int8`: 8-bit signed integer (``-128`` to ``127``).

def bytes_(value='', /, *args, **kwargs):
    A byte string.

When used in arrays, this type strips trailing null bytes.

:Character code: ``'S'``

def can_cast(from_, to, casting='safe'):
    can_cast(from_, to, casting='safe')

Returns True if cast between data types can occur according to the
casting rule.

Parameters
----------
from_ : dtype, dtype specifier, NumPy scalar, or array
    Data type, NumPy scalar, or array to cast from.
to : dtype or dtype specifier
    Data type to cast 

def cbrt(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    cbrt(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Return the cube-root of an array, element-wise.

Parameters
----------
x : array_like
    The values whose cube-roots are required.
out : ndarray, None, or tuple of ndarray and None, optional
  

def cdouble(real=0, imag=0, /):
    Complex number type composed of two double-precision floating-point numbers,
compatible with Python :class:`complex`.

:Character code: ``'D'``
:Canonical name: `numpy.cdouble`
:Alias on this platform (Linux x86_64): `numpy.complex128`: Complex number type composed of 2 64-bit-precision floating-poi

def ceil(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    ceil(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Return the ceiling of the input, element-wise.

The ceil of the scalar `x` is the smallest integer `i`, such that
``i >= x``.  It is often denoted as :math:`\lceil x \rceil`.

Parameters
-------

def character():
    Abstract base class of all character string scalar types.

def choose(a, choices, out=None, mode='raise'):
    
    Construct an array from an index array and a list of arrays to choose from.

    First of all, if confused or uncertain, definitely look at the Examples -
    in its full generality, this function is less simple than it might
    seem from the following code description::

        np.choose(a,c

def clip(a, a_min=<no value>, a_max=<no value>, out=None, *, min=<no value>, max=<no value>, **kwargs):
    
    Clip (limit) the values in an array.

    Given an interval, values outside the interval are clipped to
    the interval edges.  For example, if an interval of ``[0, 1]``
    is specified, values smaller than 0 become 0, and values larger
    than 1 become 1.

    Equivalent to but faster than 

def clongdouble(real=0, imag=0, /):
    Complex number type composed of two extended-precision floating-point numbers.

:Character code: ``'G'``
:Alias on this platform (Linux x86_64): `numpy.complex256`: Complex number type composed of 2 128-bit extended-precision floating-point numbers.

def column_stack(tup):
    
    Stack 1-D arrays as columns into a 2-D array.

    Take a sequence of 1-D arrays and stack them as columns
    to make a single 2-D array. 2-D arrays are stacked as-is,
    just like with `hstack`.  1-D arrays are turned into 2-D columns
    first.

    Parameters
    ----------
    tup : seque

def common_type(*arrays):
    
    Return a scalar type which is common to the input arrays.

    The return type will always be an inexact (i.e. floating point) scalar
    type, even if all the arrays are integer arrays. If one of the inputs is
    an integer array, the minimum precision type that is returned is a
    64-bit fl

def complex128(real=0, imag=0, /):
    Complex number type composed of two double-precision floating-point numbers,
compatible with Python :class:`complex`.

:Character code: ``'D'``
:Canonical name: `numpy.cdouble`
:Alias on this platform (Linux x86_64): `numpy.complex128`: Complex number type composed of 2 64-bit-precision floating-poi

def complex256(real=0, imag=0, /):
    Complex number type composed of two extended-precision floating-point numbers.

:Character code: ``'G'``
:Alias on this platform (Linux x86_64): `numpy.complex256`: Complex number type composed of 2 128-bit extended-precision floating-point numbers.

def complex64(real=0, imag=0, /):
    Complex number type composed of two single-precision floating-point numbers.

:Character code: ``'F'``
:Canonical name: `numpy.csingle`
:Alias on this platform (Linux x86_64): `numpy.complex64`: Complex number type composed of 2 32-bit-precision floating-point numbers.

def complexfloating():
    Abstract base class of all complex number scalar types that are made up of
floating-point numbers.

def compress(condition, a, axis=None, out=None):
    
    Return selected slices of an array along given axis.

    When working along a given axis, a slice along that axis is returned in
    `output` for each index where `condition` evaluates to True. When
    working on a 1-D array, `compress` is equivalent to `extract`.

    Parameters
    --------

def concat(arrays, /, axis=0, out=None, *, dtype=None, casting='same_kind'):
    Join a sequence of arrays along an existing axis.

Parameters
----------
a1, a2, ... : sequence of array_like
    The arrays must have the same shape, except in the dimension
    corresponding to `axis` (the first, by default).
axis : int, optional
    The axis along which the arrays will be joined.

def concatenate(arrays, /, axis=0, out=None, *, dtype=None, casting='same_kind'):
    Join a sequence of arrays along an existing axis.

Parameters
----------
a1, a2, ... : sequence of array_like
    The arrays must have the same shape, except in the dimension
    corresponding to `axis` (the first, by default).
axis : int, optional
    The axis along which the arrays will be joined.

def conj(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    conjugate(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Return the complex conjugate, element-wise.

The complex conjugate of a complex number is obtained by changing the
sign of its imaginary part.

Parameters
----------
x : array_like
    Inpu

def conjugate(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    conjugate(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Return the complex conjugate, element-wise.

The complex conjugate of a complex number is obtained by changing the
sign of its imaginary part.

Parameters
----------
x : array_like
    Inpu

def convolve(a, v, mode='full'):
    
    Returns the discrete, linear convolution of two one-dimensional sequences.

    The convolution operator is often seen in signal processing, where it
    models the effect of a linear time-invariant system on a signal [1]_.  In
    probability theory, the sum of two independent random variables

def copy(a, order='K', subok=False):
    
    Return an array copy of the given object.

    Parameters
    ----------
    a : array_like
        Input data.
    order : {'C', 'F', 'A', 'K'}, optional
        Controls the memory layout of the copy. 'C' means C-order,
        'F' means F-order, 'A' means 'F' if `a` is Fortran contiguous,
  

def copysign(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    copysign(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Change the sign of x1 to that of x2, element-wise.

If `x2` is a scalar, its sign will be copied to all elements of `x1`.

Parameters
----------
x1 : array_like
    Values to change the

def copyto(dst, src, casting='same_kind', where=True):
    copyto(dst, src, casting='same_kind', where=True)

Copies values from one array to another, broadcasting as necessary.

Raises a TypeError if the `casting` rule is violated, and if
`where` is provided, it selects which elements to copy.

Parameters
----------
dst : ndarray
    The array into which v

def corrcoef(x, y=None, rowvar=True, *, dtype=None):
    
    Return Pearson product-moment correlation coefficients.

    Please refer to the documentation for `cov` for more detail.  The
    relationship between the correlation coefficient matrix, `R`, and the
    covariance matrix, `C`, is

    .. math:: R_{ij} = \frac{ C_{ij} } { \sqrt{ C_{ii} C_{jj} 

def correlate(a, v, mode='valid'):
    
    Cross-correlation of two 1-dimensional sequences.

    This function computes the correlation as generally defined in signal
    processing texts [1]_:

    .. math:: c_k = \sum_n a_{n+k} \cdot \overline{v}_n

    with a and v sequences being zero-padded where necessary and
    :math:`\overline

def cos(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    cos(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Cosine element-wise.

Parameters
----------
x : array_like
    Input array in radians.
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which the result is stored. 

def cosh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    cosh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Hyperbolic cosine, element-wise.

Equivalent to ``1/2 * (np.exp(x) + np.exp(-x))`` and ``np.cos(1j*x)``.

Parameters
----------
x : array_like
    Input array.
out : ndarray, None, or tuple of n

def count_nonzero(a, axis=None, *, keepdims=False):
    
    Counts the number of non-zero values in the array ``a``.

    The word "non-zero" is in reference to the Python 2.x
    built-in method ``__nonzero__()`` (renamed ``__bool__()``
    in Python 3.x) of Python objects that tests an object's
    "truthfulness". For example, any number is considered

def cov(m, y=None, rowvar=True, bias=False, ddof=None, fweights=None, aweights=None, *, dtype=None):
    
    Estimate a covariance matrix, given data and weights.

    Covariance indicates the level to which two variables vary together.
    If we examine N-dimensional samples, :math:`X = [x_1, x_2, ..., x_N]^T`,
    then the covariance matrix element :math:`C_{ij}` is the covariance of
    :math:`x_i`

def cross(a, b, axisa=-1, axisb=-1, axisc=-1, axis=None):
    
    Return the cross product of two (arrays of) vectors.

    The cross product of `a` and `b` in :math:`R^3` is a vector perpendicular
    to both `a` and `b`.  If `a` and `b` are arrays of vectors, the vectors
    are defined by the last axis of `a` and `b` by default, and these axes
    can have

def csingle(real=0, imag=0, /):
    Complex number type composed of two single-precision floating-point numbers.

:Character code: ``'F'``
:Canonical name: `numpy.csingle`
:Alias on this platform (Linux x86_64): `numpy.complex64`: Complex number type composed of 2 32-bit-precision floating-point numbers.

def cumprod(a, axis=None, dtype=None, out=None):
    
    Return the cumulative product of elements along a given axis.

    Parameters
    ----------
    a : array_like
        Input array.
    axis : int, optional
        Axis along which the cumulative product is computed.  By default
        the input is flattened.
    dtype : dtype, optional
    

def cumsum(a, axis=None, dtype=None, out=None):
    
    Return the cumulative sum of the elements along a given axis.

    Parameters
    ----------
    a : array_like
        Input array.
    axis : int, optional
        Axis along which the cumulative sum is computed. The default
        (None) is to compute the cumsum over the flattened array.
  

def cumulative_prod(x, /, *, axis=None, dtype=None, out=None, include_initial=False):
    
    Return the cumulative product of elements along a given axis.

    This function is an Array API compatible alternative to `numpy.cumprod`.

    Parameters
    ----------
    x : array_like
        Input array.
    axis : int, optional
        Axis along which the cumulative product is computed

def cumulative_sum(x, /, *, axis=None, dtype=None, out=None, include_initial=False):
    
    Return the cumulative sum of the elements along a given axis.

    This function is an Array API compatible alternative to `numpy.cumsum`.

    Parameters
    ----------
    x : array_like
        Input array.
    axis : int, optional
        Axis along which the cumulative sum is computed. The

def datetime64(value=None, /, *args):
    If created from a 64-bit integer, it represents an offset from ``1970-01-01T00:00:00``.
If created from string, the string can be in ISO 8601 date or datetime format.

When parsing a string to create a datetime object, if the string contains
a trailing timezone (A 'Z' or a timezone offset), the time

def datetime_as_string(arr, unit=None, timezone='naive', casting='same_kind'):
    datetime_as_string(arr, unit=None, timezone='naive', casting='same_kind')

Convert an array of datetimes into an array of strings.

Parameters
----------
arr : array_like of datetime64
    The array of UTC timestamps to format.
unit : str
    One of None, 'auto', or
    a :ref:`datetime unit <arrays

def datetime_data(dtype, /):
    datetime_data(dtype, /)

Get information about the step size of a date or time type.

The returned tuple can be passed as the second argument of `numpy.datetime64` and
`numpy.timedelta64`.

Parameters
----------
dtype : dtype
    The dtype object, which must be a `datetime64` or `timedelta64` type.


def deg2rad(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    deg2rad(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Convert angles from degrees to radians.

Parameters
----------
x : array_like
    Angles in degrees.
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which the 

def degrees(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    degrees(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Convert angles from radians to degrees.

Parameters
----------
x : array_like
    Input array in radians.
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which

def delete(arr, obj, axis=None):
    
    Return a new array with sub-arrays along an axis deleted. For a one
    dimensional array, this returns those entries not returned by
    `arr[obj]`.

    Parameters
    ----------
    arr : array_like
        Input array.
    obj : slice, int, array-like of ints or bools
        Indicate indic

def diag(v, k=0):
    
    Extract a diagonal or construct a diagonal array.

    See the more detailed documentation for ``numpy.diagonal`` if you use this
    function to extract a diagonal and wish to write to the resulting array;
    whether it returns a copy or a view depends on what version of numpy you
    are usi

def diag_indices(n, ndim=2):
    
    Return the indices to access the main diagonal of an array.

    This returns a tuple of indices that can be used to access the main
    diagonal of an array `a` with ``a.ndim >= 2`` dimensions and shape
    (n, n, ..., n). For ``a.ndim = 2`` this is the usual diagonal, for
    ``a.ndim > 2`` t

def diag_indices_from(arr):
    
    Return the indices to access the main diagonal of an n-dimensional array.

    See `diag_indices` for full details.

    Parameters
    ----------
    arr : array, at least 2-D

    See Also
    --------
    diag_indices

    Examples
    --------
    >>> import numpy as np

    Create a 4 by 4

def diagflat(v, k=0):
    
    Create a two-dimensional array with the flattened input as a diagonal.

    Parameters
    ----------
    v : array_like
        Input data, which is flattened and set as the `k`-th
        diagonal of the output.
    k : int, optional
        Diagonal to set; 0, the default, corresponds to the

def diagonal(a, offset=0, axis1=0, axis2=1):
    
    Return specified diagonals.

    If `a` is 2-D, returns the diagonal of `a` with the given offset,
    i.e., the collection of elements of the form ``a[i, i+offset]``.  If
    `a` has more than two dimensions, then the axes specified by `axis1`
    and `axis2` are used to determine the 2-D sub-

def diff(a, n=1, axis=-1, prepend=<no value>, append=<no value>):
    
    Calculate the n-th discrete difference along the given axis.

    The first difference is given by ``out[i] = a[i+1] - a[i]`` along
    the given axis, higher differences are calculated by using `diff`
    recursively.

    Parameters
    ----------
    a : array_like
        Input array
    n 

def digitize(x, bins, right=False):
    
    Return the indices of the bins to which each value in input array belongs.

    =========  =============  ============================
    `right`    order of bins  returned index `i` satisfies
    =========  =============  ============================
    ``False``  increasing     ``bins[i-1] 

def divide(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    divide(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Divide arguments element-wise.

Parameters
----------
x1 : array_like
    Dividend array.
x2 : array_like
    Divisor array.
    If ``x1.shape != x2.shape``, they must be broadcastable to

def divmod(x1, x2, /, out=(None, None), *, where=True, casting='same_kind', order='K', dtype=None, subok=True,:
    divmod(x1, x2[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Return element-wise quotient and remainder simultaneously.

``np.divmod(x, y)`` is equivalent to ``(x // y, x % y)``, but faster
because it avoids redundant work.

def dot(a, b, out=None):
    dot(a, b, out=None)

Dot product of two arrays. Specifically,

- If both `a` and `b` are 1-D arrays, it is inner product of vectors
  (without complex conjugation).

- If both `a` and `b` are 2-D arrays, it is matrix multiplication,
  but using :func:`matmul` or ``a @ b`` is preferred.

- If either 

def double(value=0, /):
    Double-precision floating-point number type, compatible with Python :class:`float` and C ``double``.

:Character code: ``'d'``
:Canonical name: `numpy.double`
:Alias on this platform (Linux x86_64): `numpy.float64`: 64-bit precision floating-point number type: sign bit, 11 bits exponent, 52 bits man

def dsplit(ary, indices_or_sections):
    
    Split array into multiple sub-arrays along the 3rd axis (depth).

    Please refer to the `split` documentation.  `dsplit` is equivalent
    to `split` with ``axis=2``, the array is always split along the third
    axis provided the array dimension is greater than or equal to 3.

    See Also
 

def dstack(tup):
    
    Stack arrays in sequence depth wise (along third axis).

    This is equivalent to concatenation along the third axis after 2-D arrays
    of shape `(M,N)` have been reshaped to `(M,N,1)` and 1-D arrays of shape
    `(N,)` have been reshaped to `(1,N,1)`. Rebuilds arrays divided by
    `dsplit`

def dtype(dtype, align=False, copy=False, **kwargs):
    dtype(dtype, align=False, copy=False, **kwargs)
--

dtype(dtype, align=False, copy=False, [metadata])

Create a data type object.

A numpy array is homogeneous, and contains elements described by a
dtype object. A dtype object can be constructed from different
combinations of fundamental numeric typ

def ediff1d(ary, to_end=None, to_begin=None):
    
    The differences between consecutive elements of an array.

    Parameters
    ----------
    ary : array_like
        If necessary, will be flattened before the differences are taken.
    to_end : array_like, optional
        Number(s) to append at the end of the returned differences.
    to_be

def einsum(*operands, out=None, optimize=False, **kwargs):
    
    einsum(subscripts, *operands, out=None, dtype=None, order='K',
           casting='safe', optimize=False)

    Evaluates the Einstein summation convention on the operands.

    Using the Einstein summation convention, many common multi-dimensional,
    linear algebraic array operations can be r

def einsum_path(*operands, optimize='greedy', einsum_call=False):
    
    einsum_path(subscripts, *operands, optimize='greedy')

    Evaluates the lowest cost contraction order for an einsum expression by
    considering the creation of intermediate arrays.

    Parameters
    ----------
    subscripts : str
        Specifies the subscripts for summation.
    *operan

def empty(shape, dtype=None, order='C', *, device=None, like=None):
    empty(shape, dtype=None, order='C', *, device=None, like=None)

Return a new array of given shape and type, without initializing entries.

Parameters
----------
shape : int or tuple of int
    Shape of the empty array, e.g., ``(2, 3)`` or ``2``.
dtype : data-type, optional
    Desired output data-ty

def empty_like(prototype, /, dtype=None, order='K', subok=True, shape=None, *, device=None):
    Return a new array with the same shape and type as a given array.

Parameters
----------
prototype : array_like
    The shape and data-type of `prototype` define these same attributes
    of the returned array.
dtype : data-type, optional
    Overrides the data type of the result.
order : {'C', 'F',

def equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Return (x1 == x2) element-wise.

Parameters
----------
x1, x2 : array_like
    Input arrays.
    If ``x1.shape != x2.shape``, they must be broadcastable to a common
    shape (which become

def errstate(*, call=<numpy._core._ufunc_config._unspecified object at 0x7edb4f08f020>, all=None, divide=None, o:
    
    errstate(**kwargs)

    Context manager for floating-point error handling.

    Using an instance of `errstate` as a context manager allows statements in
    that context to execute with a known error handling behavior. Upon entering
    the context the error handling is set with `seterr` and `

def exp(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    exp(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Calculate the exponential of all elements in the input array.

Parameters
----------
x : array_like
    Input values.
out : ndarray, None, or tuple of ndarray and None, optional
    A location in

def exp2(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    exp2(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Calculate `2**p` for all `p` in the input array.

Parameters
----------
x : array_like
    Input values.
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which the

def expand_dims(a, axis):
    
    Expand the shape of an array.

    Insert a new axis that will appear at the `axis` position in the expanded
    array shape.

    Parameters
    ----------
    a : array_like
        Input array.
    axis : int or tuple of ints
        Position in the expanded axes where the new axis (or axes)

def expm1(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    expm1(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Calculate ``exp(x) - 1`` for all elements in the array.

Parameters
----------
x : array_like
    Input values.
out : ndarray, None, or tuple of ndarray and None, optional
    A location into w

def extract(condition, arr):
    
    Return the elements of an array that satisfy some condition.

    This is equivalent to ``np.compress(ravel(condition), ravel(arr))``.  If
    `condition` is boolean ``np.extract`` is equivalent to ``arr[condition]``.

    Note that `place` does the exact opposite of `extract`.

    Parameters


def eye(N, M=None, k=0, dtype=<class 'float'>, order='C', *, device=None, like=None):
    
    Return a 2-D array with ones on the diagonal and zeros elsewhere.

    Parameters
    ----------
    N : int
      Number of rows in the output.
    M : int, optional
      Number of columns in the output. If None, defaults to `N`.
    k : int, optional
      Index of the diagonal: 0 (the defau

def fabs(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    fabs(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Compute the absolute values element-wise.

This function returns the absolute values (positive magnitude) of the
data in `x`. Complex values are not handled, use `absolute` to find the
absolute 

def fill_diagonal(a, val, wrap=False):
    Fill the main diagonal of the given array of any dimensionality.

    For an array `a` with ``a.ndim >= 2``, the diagonal is the list of
    values ``a[i, ..., i]`` with indices ``i`` all identical.  This function
    modifies the input array in-place without returning a value.

    Parameters
    -

def finfo(dtype):
    
    finfo(dtype)

    Machine limits for floating point types.

    Attributes
    ----------
    bits : int
        The number of bits occupied by the type.
    dtype : dtype
        Returns the dtype for which `finfo` returns information. For complex
        input, the returned dtype is the assoc

def fix(x, out=None):
    
    Round to nearest integer towards zero.

    Round an array of floats element-wise to nearest integer towards zero.
    The rounded values have the same data-type as the input.

    Parameters
    ----------
    x : array_like
        An array to be rounded
    out : ndarray, optional
        A 

def flatiter():
    Flat iterator object to iterate over arrays.

A `flatiter` iterator is returned by ``x.flat`` for any array `x`.
It allows iterating over the array as if it were a 1-D array,
either in a for-loop or by calling its `next` method.

Iteration is done in row-major, C-style order (the last
index varying 

def flatnonzero(a):
    
    Return indices that are non-zero in the flattened version of a.

    This is equivalent to ``np.nonzero(np.ravel(a))[0]``.

    Parameters
    ----------
    a : array_like
        Input data.

    Returns
    -------
    res : ndarray
        Output array, containing the indices of the element

def flexible():
    Abstract base class of all scalar types without predefined length.
The actual size of these types depends on the specific `numpy.dtype`
instantiation.

def flip(m, axis=None):
    
    Reverse the order of elements in an array along the given axis.

    The shape of the array is preserved, but the elements are reordered.

    Parameters
    ----------
    m : array_like
        Input array.
    axis : None or int or tuple of ints, optional
         Axis or axes along which to

def fliplr(m):
    
    Reverse the order of elements along axis 1 (left/right).

    For a 2-D array, this flips the entries in each row in the left/right
    direction. Columns are preserved, but appear in a different order than
    before.

    Parameters
    ----------
    m : array_like
        Input array, must 

def flipud(m):
    
    Reverse the order of elements along axis 0 (up/down).

    For a 2-D array, this flips the entries in each column in the up/down
    direction. Rows are preserved, but appear in a different order than before.

    Parameters
    ----------
    m : array_like
        Input array.

    Returns
  

def float128(value=0, /):
    Extended-precision floating-point number type, compatible with C ``long double``
but not necessarily with IEEE 754 quadruple-precision.

:Character code: ``'g'``
:Alias on this platform (Linux x86_64): `numpy.float128`: 128-bit extended-precision floating-point number type.

def float16(value=0, /):
    Half-precision floating-point number type.

:Character code: ``'e'``
:Canonical name: `numpy.half`
:Alias on this platform (Linux x86_64): `numpy.float16`: 16-bit-precision floating-point number type: sign bit, 5 bits exponent, 10 bits mantissa.

def float32(value=0, /):
    Single-precision floating-point number type, compatible with C ``float``.

:Character code: ``'f'``
:Canonical name: `numpy.single`
:Alias on this platform (Linux x86_64): `numpy.float32`: 32-bit-precision floating-point number type: sign bit, 8 bits exponent, 23 bits mantissa.

def float64(value=0, /):
    Double-precision floating-point number type, compatible with Python :class:`float` and C ``double``.

:Character code: ``'d'``
:Canonical name: `numpy.double`
:Alias on this platform (Linux x86_64): `numpy.float64`: 64-bit precision floating-point number type: sign bit, 11 bits exponent, 52 bits man

def float_power(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    float_power(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

First array elements raised to powers from second array, element-wise.

Raise each base in `x1` to the positionally-corresponding power in `x2`.
`x1` and `x2` must be broadcastable t

def floating():
    Abstract base class of all floating-point scalar types.

def floor(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    floor(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Return the floor of the input, element-wise.

The floor of the scalar `x` is the largest integer `i`, such that
`i <= x`.  It is often denoted as :math:`\lfloor x \rfloor`.

Parameters
--------

def floor_divide(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    floor_divide(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Return the largest integer smaller or equal to the division of the inputs.
It is equivalent to the Python ``//`` operator and pairs with the
Python ``%`` (`remainder`), function so 

def fmax(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    fmax(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Element-wise maximum of array elements.

Compare two arrays and return a new array containing the element-wise
maxima. If one of the elements being compared is a NaN, then the
non-nan eleme

def fmin(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    fmin(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Element-wise minimum of array elements.

Compare two arrays and return a new array containing the element-wise
minima. If one of the elements being compared is a NaN, then the
non-nan eleme

def fmod(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    fmod(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Returns the element-wise remainder of division.

This is the NumPy implementation of the C library function fmod, the
remainder has the same sign as the dividend `x1`. It is equivalent to
t

def format_float_positional(x, precision=None, unique=True, fractional=True, trim='k', sign=False, pad_left=None, pad_right=Non:
    
    Format a floating-point scalar as a decimal string in positional notation.

    Provides control over rounding, trimming and padding. Uses and assumes
    IEEE unbiased rounding. Uses the "Dragon4" algorithm.

    Parameters
    ----------
    x : python float or numpy floating scalar
        V

def format_float_scientific(x, precision=None, unique=True, trim='k', sign=False, pad_left=None, exp_digits=None, min_digits=No:
    
    Format a floating-point scalar as a decimal string in scientific notation.

    Provides control over rounding, trimming and padding. Uses and assumes
    IEEE unbiased rounding. Uses the "Dragon4" algorithm.

    Parameters
    ----------
    x : python float or numpy floating scalar
        V

def frexp(x, /, out=(None, None), *, where=True, casting='same_kind', order='K', dtype=None, subok=True, sign:
    frexp(x[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Decompose the elements of x into mantissa and twos exponent.

Returns (`mantissa`, `exponent`), where ``x = mantissa * 2**exponent``.
The mantissa lies in the open inte

def from_dlpack(x, /, *, device=None, copy=None):
    from_dlpack(x, /, *, device=None, copy=None)

Create a NumPy array from an object implementing the ``__dlpack__``
protocol. Generally, the returned NumPy array is a view of the input
object. See [1]_ and [2]_ for more details.

Parameters
----------
x : object
    A Python object that implements the

def frombuffer(buffer, dtype=None, count=-1, offset=0, *, like=None):
    frombuffer(buffer, dtype=float, count=-1, offset=0, *, like=None)

Interpret a buffer as a 1-dimensional array.

Parameters
----------
buffer : buffer_like
    An object that exposes the buffer interface.
dtype : data-type, optional
    Data-type of the returned array.  Default is `numpy.float64`.
c

def fromfile(file, dtype=None, count=-1, sep='', offset=0, *, like=None):
    fromfile(file, dtype=float, count=-1, sep='', offset=0, *, like=None)

Construct an array from data in a text or binary file.

A highly efficient way of reading binary data with a known data-type,
as well as parsing simply formatted text files.  Data written using the
`tofile` method can be read usi

def fromfunction(function, shape, *, dtype=<class 'float'>, like=None, **kwargs):
    
    Construct an array by executing a function over each coordinate.

    The resulting array therefore has a value ``fn(x, y, z)`` at
    coordinate ``(x, y, z)``.

    Parameters
    ----------
    function : callable
        The function is called with N parameters, where N is the rank of
      

def fromiter(iter, dtype, count=-1, *, like=None):
    fromiter(iter, dtype, count=-1, *, like=None)

Create a new 1-dimensional array from an iterable object.

Parameters
----------
iter : iterable object
    An iterable object providing data for the array.
dtype : data-type
    The data-type of the returned array.

    .. versionchanged:: 1.23
       

def frompyfunc(func, /, nin, nout, **kwargs):
    frompyfunc(func, /, nin, nout, *[, identity])

Takes an arbitrary Python function and returns a NumPy ufunc.

Can be used, for example, to add broadcasting to a built-in Python
function (see Examples section).

Parameters
----------
func : Python function object
    An arbitrary Python function.
nin

def fromregex(file, regexp, dtype, encoding=None):
    
    Construct an array from a text file, using regular expression parsing.

    The returned array is always a structured array, and is constructed from
    all matches of the regular expression in the file. Groups in the regular
    expression are converted to fields of the structured array.

    

def fromstring:
    fromstring(string, dtype=float, count=-1, *, sep, like=None)

A new 1-D array initialized from text data in a string.

Parameters
----------
string : str
    A string containing the data.
dtype : data-type, optional
    The data type of the array; default: `numpy.float64`.  For binary input data,
  

def full(shape, fill_value, dtype=None, order='C', *, device=None, like=None):
    
    Return a new array of given shape and type, filled with `fill_value`.

    Parameters
    ----------
    shape : int or sequence of ints
        Shape of the new array, e.g., ``(2, 3)`` or ``2``.
    fill_value : scalar or array_like
        Fill value.
    dtype : data-type, optional
        T

def full_like(a, fill_value, dtype=None, order='K', subok=True, shape=None, *, device=None):
    
    Return a full array with the same shape and type as a given array.

    Parameters
    ----------
    a : array_like
        The shape and data-type of `a` define these same attributes of
        the returned array.
    fill_value : array_like
        Fill value.
    dtype : data-type, optional

def gcd(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    gcd(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Returns the greatest common divisor of ``|x1|`` and ``|x2|``

Parameters
----------
x1, x2 : array_like, int
    Arrays of values.
    If ``x1.shape != x2.shape``, they must be broadcastable

def generic():
    Base class for numpy scalar types.

Class from which most (all?) numpy scalar types are derived.  For
consistency, exposes the same API as `ndarray`, despite many
consequent attributes being either "get-only," or completely irrelevant.
This is the class from which it is strongly suggested users shou

def genfromtxt(fname, dtype=<class 'float'>, comments='#', delimiter=None, skip_header=0, skip_footer=0, converter:
    
    Load data from a text file, with missing values handled as specified.

    Each line past the first `skip_header` lines is split at the `delimiter`
    character, and characters following the `comments` character are discarded.

    Parameters
    ----------
    fname : file, str, pathlib.Path,

def geomspace(start, stop, num=50, endpoint=True, dtype=None, axis=0):
    
    Return numbers spaced evenly on a log scale (a geometric progression).

    This is similar to `logspace`, but with endpoints specified directly.
    Each output sample is a constant multiple of the previous.

    Parameters
    ----------
    start : array_like
        The starting value of th

def get_include():
    
    Return the directory that contains the NumPy \*.h header files.

    Extension modules that need to compile against NumPy may need to use this
    function to locate the appropriate include directory.

    Notes
    -----
    When using ``setuptools``, for example in ``setup.py``::

        imp

def get_printoptions():
    
    Return the current print options.

    Returns
    -------
    print_opts : dict
        Dictionary of current print options with keys

        - precision : int
        - threshold : int
        - edgeitems : int
        - linewidth : int
        - suppress : bool
        - nanstr : str
      

def getbufsize():
    
    Return the size of the buffer used in ufuncs.

    Returns
    -------
    getbufsize : int
        Size of ufunc buffer in bytes.

    Notes
    -----

    **Concurrency note:** see :doc:`/reference/routines.err`


    Examples
    --------
    >>> import numpy as np
    >>> np.getbufsize()
  

def geterr():
    
    Get the current way of handling floating-point errors.

    Returns
    -------
    res : dict
        A dictionary with keys "divide", "over", "under", and "invalid",
        whose values are from the strings "ignore", "print", "log", "warn",
        "raise", and "call". The keys represent pos

def geterrcall():
    
    Return the current callback function used on floating-point errors.

    When the error handling for a floating-point error (one of "divide",
    "over", "under", or "invalid") is set to 'call' or 'log', the function
    that is called or the log instance that is written to is returned by
    `

def gradient(f, *varargs, axis=None, edge_order=1):
    
    Return the gradient of an N-dimensional array.

    The gradient is computed using second order accurate central differences
    in the interior points and either first or second order accurate one-sides
    (forward or backwards) differences at the boundaries.
    The returned gradient hence h

def greater(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    greater(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Return the truth value of (x1 > x2) element-wise.

Parameters
----------
x1, x2 : array_like
    Input arrays.
    If ``x1.shape != x2.shape``, they must be broadcastable to a common
   

def greater_equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    greater_equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Return the truth value of (x1 >= x2) element-wise.

Parameters
----------
x1, x2 : array_like
    Input arrays.
    If ``x1.shape != x2.shape``, they must be broadcastable to a com

def half(value=0, /):
    Half-precision floating-point number type.

:Character code: ``'e'``
:Canonical name: `numpy.half`
:Alias on this platform (Linux x86_64): `numpy.float16`: 16-bit-precision floating-point number type: sign bit, 5 bits exponent, 10 bits mantissa.

def hamming(M):
    
    Return the Hamming window.

    The Hamming window is a taper formed by using a weighted cosine.

    Parameters
    ----------
    M : int
        Number of points in the output window. If zero or less, an
        empty array is returned.

    Returns
    -------
    out : ndarray
        The 

def hanning(M):
    
    Return the Hanning window.

    The Hanning window is a taper formed by using a weighted cosine.

    Parameters
    ----------
    M : int
        Number of points in the output window. If zero or less, an
        empty array is returned.

    Returns
    -------
    out : ndarray, shape(M,)
 

def heaviside(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    heaviside(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Compute the Heaviside step function.

The Heaviside step function [1]_ is defined as::

                          0   if x1 < 0
    heaviside(x1, x2) =  x2   if x1 == 0
               

def histogram(a, bins=10, range=None, density=None, weights=None):
    
    Compute the histogram of a dataset.

    Parameters
    ----------
    a : array_like
        Input data. The histogram is computed over the flattened array.
    bins : int or sequence of scalars or str, optional
        If `bins` is an int, it defines the number of equal-width
        bins in 

def histogram2d(x, y, bins=10, range=None, density=None, weights=None):
    
    Compute the bi-dimensional histogram of two data samples.

    Parameters
    ----------
    x : array_like, shape (N,)
        An array containing the x coordinates of the points to be
        histogrammed.
    y : array_like, shape (N,)
        An array containing the y coordinates of the poi

def histogram_bin_edges(a, bins=10, range=None, weights=None):
    
    Function to calculate only the edges of the bins used by the `histogram`
    function.

    Parameters
    ----------
    a : array_like
        Input data. The histogram is computed over the flattened array.
    bins : int or sequence of scalars or str, optional
        If `bins` is an int, it

def histogramdd(sample, bins=10, range=None, density=None, weights=None):
    
    Compute the multidimensional histogram of some data.

    Parameters
    ----------
    sample : (N, D) array, or (N, D) array_like
        The data to be histogrammed.

        Note the unusual interpretation of sample when an array_like:

        * When an array, each row is a coordinate in a

def hsplit(ary, indices_or_sections):
    
    Split an array into multiple sub-arrays horizontally (column-wise).

    Please refer to the `split` documentation.  `hsplit` is equivalent
    to `split` with ``axis=1``, the array is always split along the second
    axis except for 1-D arrays, where it is split at ``axis=0``.

    See Also
 

def hstack(tup, *, dtype=None, casting='same_kind'):
    
    Stack arrays in sequence horizontally (column wise).

    This is equivalent to concatenation along the second axis, except for 1-D
    arrays where it concatenates along the first axis. Rebuilds arrays divided
    by `hsplit`.

    This function makes most sense for arrays with up to 3 dimensi

def hypot(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    hypot(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Given the "legs" of a right triangle, return its hypotenuse.

Equivalent to ``sqrt(x1**2 + x2**2)``, element-wise.  If `x1` or
`x2` is scalar_like (i.e., unambiguously cast-able to a scala

def i0(x):
    
    Modified Bessel function of the first kind, order 0.

    Usually denoted :math:`I_0`.

    Parameters
    ----------
    x : array_like of float
        Argument of the Bessel function.

    Returns
    -------
    out : ndarray, shape = x.shape, dtype = float
        The modified Bessel funct

def identity(n, dtype=None, *, like=None):
    
    Return the identity array.

    The identity array is a square array with ones on
    the main diagonal.

    Parameters
    ----------
    n : int
        Number of rows (and columns) in `n` x `n` output.
    dtype : data-type, optional
        Data-type of the output.  Defaults to ``float``.


def iinfo(int_type):
    
    iinfo(type)

    Machine limits for integer types.

    Attributes
    ----------
    bits : int
        The number of bits occupied by the type.
    dtype : dtype
        Returns the dtype for which `iinfo` returns information.
    min : int
        The smallest integer expressible by the type

def imag(val):
    
    Return the imaginary part of the complex argument.

    Parameters
    ----------
    val : array_like
        Input array.

    Returns
    -------
    out : ndarray or scalar
        The imaginary component of the complex argument. If `val` is real,
        the type of `val` is used for the o

def indices(dimensions, dtype=<class 'int'>, sparse=False):
    
    Return an array representing the indices of a grid.

    Compute an array where the subarrays contain index values 0, 1, ...
    varying only along the corresponding axis.

    Parameters
    ----------
    dimensions : sequence of ints
        The shape of the grid.
    dtype : dtype, optional

def inexact():
    Abstract base class of all numeric scalar types with a (potentially)
inexact representation of the values in its range, such as
floating-point numbers.

def info(object=None, maxwidth=76, output=None, toplevel='numpy'):
    
    Get help information for an array, function, class, or module.

    Parameters
    ----------
    object : object or str, optional
        Input object or name to get information about. If `object` is
        an `ndarray` instance, information about the array is printed.
        If `object` is 

def inner(a, b, /):
    inner(a, b, /)

Inner product of two arrays.

Ordinary inner product of vectors for 1-D arrays (without complex
conjugation), in higher dimensions a sum product over the last axes.

Parameters
----------
a, b : array_like
    If `a` and `b` are nonscalar, their last dimensions must match.

Returns
-

def insert(arr, obj, values, axis=None):
    
    Insert values along the given axis before the given indices.

    Parameters
    ----------
    arr : array_like
        Input array.
    obj : slice, int, array-like of ints or bools
        Object that defines the index or indices before which `values` is
        inserted.

        .. version

def int16(value=0, /):
    Signed integer type, compatible with C ``short``.

:Character code: ``'h'``
:Canonical name: `numpy.short`
:Alias on this platform (Linux x86_64): `numpy.int16`: 16-bit signed integer (``-32_768`` to ``32_767``).

def int32(value=0, /):
    Signed integer type, compatible with C ``int``.

:Character code: ``'i'``
:Canonical name: `numpy.intc`
:Alias on this platform (Linux x86_64): `numpy.int32`: 32-bit signed integer (``-2_147_483_648`` to ``2_147_483_647``).

def int64(value=0, /):
    Signed integer type, compatible with C ``long``.

:Character code: ``'l'``
:Canonical name: `numpy.long`
:Alias on this platform (Linux x86_64): `numpy.int64`: 64-bit signed integer (``-9_223_372_036_854_775_808`` to ``9_223_372_036_854_775_807``).
:Alias on this platform (Linux x86_64): `numpy.intp

def int8(value=0, /):
    Signed integer type, compatible with C ``char``.

:Character code: ``'b'``
:Canonical name: `numpy.byte`
:Alias on this platform (Linux x86_64): `numpy.int8`: 8-bit signed integer (``-128`` to ``127``).

def int_(value=0, /):
    Signed integer type, compatible with C ``long``.

:Character code: ``'l'``
:Canonical name: `numpy.long`
:Alias on this platform (Linux x86_64): `numpy.int64`: 64-bit signed integer (``-9_223_372_036_854_775_808`` to ``9_223_372_036_854_775_807``).
:Alias on this platform (Linux x86_64): `numpy.intp

def intc(value=0, /):
    Signed integer type, compatible with C ``int``.

:Character code: ``'i'``
:Canonical name: `numpy.intc`
:Alias on this platform (Linux x86_64): `numpy.int32`: 32-bit signed integer (``-2_147_483_648`` to ``2_147_483_647``).

def integer():
    Abstract base class of all integer scalar types.

def interp(x, xp, fp, left=None, right=None, period=None):
    
    One-dimensional linear interpolation for monotonically increasing sample points.

    Returns the one-dimensional piecewise linear interpolant to a function
    with given discrete data points (`xp`, `fp`), evaluated at `x`.

    Parameters
    ----------
    x : array_like
        The x-coordi

def intersect1d(ar1, ar2, assume_unique=False, return_indices=False):
    
    Find the intersection of two arrays.

    Return the sorted, unique values that are in both of the input arrays.

    Parameters
    ----------
    ar1, ar2 : array_like
        Input arrays. Will be flattened if not already 1D.
    assume_unique : bool
        If True, the input arrays are bot

def intp(value=0, /):
    Signed integer type, compatible with C ``long``.

:Character code: ``'l'``
:Canonical name: `numpy.long`
:Alias on this platform (Linux x86_64): `numpy.int64`: 64-bit signed integer (``-9_223_372_036_854_775_808`` to ``9_223_372_036_854_775_807``).
:Alias on this platform (Linux x86_64): `numpy.intp

def invert(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    invert(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Compute bit-wise inversion, or bit-wise NOT, element-wise.

Computes the bit-wise NOT of the underlying binary representation of
the integers in the input arrays. This ufunc implements the C/P

def is_busday(dates, weekmask='1111100', holidays=None, busdaycal=None, out=None):
    is_busday(
    dates,
    weekmask='1111100',
    holidays=None,
    busdaycal=None,
    out=None,
)

Calculates which of the given dates are valid days, and which are not.

Parameters
----------
dates : array_like of datetime64[D]
    The array of dates to process.
weekmask : str or array_like of b

def isclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False):
    
    Returns a boolean array where two arrays are element-wise equal within a
    tolerance.

    The tolerance values are positive, typically very small numbers.  The
    relative difference (`rtol` * abs(`b`)) and the absolute difference
    `atol` are added together to compare against the absolut

def iscomplex(x):
    
    Returns a bool array, where True if input element is complex.

    What is tested is whether the input has a non-zero imaginary part, not if
    the input type is complex.

    Parameters
    ----------
    x : array_like
        Input array.

    Returns
    -------
    out : ndarray of bools


def iscomplexobj(x):
    
    Check for a complex type or an array of complex numbers.

    The type of the input is checked, not the value. Even if the input
    has an imaginary part equal to zero, `iscomplexobj` evaluates to True.

    Parameters
    ----------
    x : any
        The input can be of any type and shape.


def isdtype(dtype, kind):
    
    Determine if a provided dtype is of a specified data type ``kind``.

    This function only supports built-in NumPy's data types.
    Third-party dtypes are not yet supported.

    Parameters
    ----------
    dtype : dtype
        The input dtype.
    kind : dtype or str or tuple of dtypes/st

def isfinite(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    isfinite(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Test element-wise for finiteness (not infinity and not Not a Number).

The result is returned as a boolean array.

Parameters
----------
x : array_like
    Input values.
out : ndarray, None,

def isfortran(a):
    
    Check if the array is Fortran contiguous but *not* C contiguous.

    This function is obsolete. If you only want to check if an array is Fortran
    contiguous use ``a.flags.f_contiguous`` instead.

    Parameters
    ----------
    a : ndarray
        Input array.

    Returns
    -------
   

def isin(element, test_elements, assume_unique=False, invert=False, *, kind=None):
    
    Calculates ``element in test_elements``, broadcasting over `element` only.
    Returns a boolean array of the same shape as `element` that is True
    where an element of `element` is in `test_elements` and False otherwise.

    Parameters
    ----------
    element : array_like
        Input a

def isinf(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    isinf(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Test element-wise for positive or negative infinity.

Returns a boolean array of the same shape as `x`, True where ``x ==
+/-inf``, otherwise False.

Parameters
----------
x : array_like
    In

def isnan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    isnan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Test element-wise for NaN and return result as a boolean array.

Parameters
----------
x : array_like
    Input array.
out : ndarray, None, or tuple of ndarray and None, optional
    A location

def isnat(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    isnat(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Test element-wise for NaT (not a time) and return result as a boolean array.

Parameters
----------
x : array_like
    Input array with datetime or timedelta data type.
out : ndarray, None, or 

def isneginf(x, out=None):
    
    Test element-wise for negative infinity, return result as bool array.

    Parameters
    ----------
    x : array_like
        The input array.
    out : array_like, optional
        A location into which the result is stored. If provided, it must have a
        shape that the input broadcasts

def isposinf(x, out=None):
    
    Test element-wise for positive infinity, return result as bool array.

    Parameters
    ----------
    x : array_like
        The input array.
    out : array_like, optional
        A location into which the result is stored. If provided, it must have a
        shape that the input broadcasts

def isreal(x):
    
    Returns a bool array, where True if input element is real.

    If element has complex type with zero imaginary part, the return value
    for that element is True.

    Parameters
    ----------
    x : array_like
        Input array.

    Returns
    -------
    out : ndarray, bool
        Bo

def isrealobj(x):
    
    Return True if x is a not complex type or an array of complex numbers.

    The type of the input is checked, not the value. So even if the input
    has an imaginary part equal to zero, `isrealobj` evaluates to False
    if the data type is complex.

    Parameters
    ----------
    x : any
 

def isscalar(element):
    
    Returns True if the type of `element` is a scalar type.

    Parameters
    ----------
    element : any
        Input argument, can be of any type and shape.

    Returns
    -------
    val : bool
        True if `element` is a scalar type, False if it is not.

    See Also
    --------
    n

def issubdtype(arg1, arg2):
    
    Returns True if first argument is a typecode lower/equal in type hierarchy.

    This is like the builtin :func:`issubclass`, but for `dtype`\ s.

    Parameters
    ----------
    arg1, arg2 : dtype_like
        `dtype` or object coercible to one

    Returns
    -------
    out : bool

    Se

def iterable(y):
    
    Check whether or not an object can be iterated over.

    Parameters
    ----------
    y : object
      Input object.

    Returns
    -------
    b : bool
      Return ``True`` if the object has an iterator method or is a
      sequence and ``False`` otherwise.


    Examples
    --------
   

def ix_(*args):
    
    Construct an open mesh from multiple sequences.

    This function takes N 1-D sequences and returns N outputs with N
    dimensions each, such that the shape is 1 in all but one dimension
    and the dimension with the non-unit shape value cycles through all
    N dimensions.

    Using `ix_` 

def kaiser(M, beta):
    
    Return the Kaiser window.

    The Kaiser window is a taper formed by using a Bessel function.

    Parameters
    ----------
    M : int
        Number of points in the output window. If zero or less, an
        empty array is returned.
    beta : float
        Shape parameter for window.

   

def kron(a, b):
    
    Kronecker product of two arrays.

    Computes the Kronecker product, a composite array made of blocks of the
    second array scaled by the first.

    Parameters
    ----------
    a, b : array_like

    Returns
    -------
    out : ndarray

    See Also
    --------
    outer : The outer pr

def lcm(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    lcm(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Returns the lowest common multiple of ``|x1|`` and ``|x2|``

Parameters
----------
x1, x2 : array_like, int
    Arrays of values.
    If ``x1.shape != x2.shape``, they must be broadcastable 

def ldexp(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    ldexp(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Returns x1 * 2**x2, element-wise.

The mantissas `x1` and twos exponents `x2` are used to construct
floating point numbers ``x1 * 2**x2``.

Parameters
----------
x1 : array_like
    Array 

def left_shift(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    left_shift(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Shift the bits of an integer to the left.

Bits are shifted to the left by appending `x2` 0s at the right of `x1`.
Since the internal representation of numbers is in binary format, th

def less(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    less(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Return the truth value of (x1 < x2) element-wise.

Parameters
----------
x1, x2 : array_like
    Input arrays.
    If ``x1.shape != x2.shape``, they must be broadcastable to a common
    sh

def less_equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    less_equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Return the truth value of (x1 <= x2) element-wise.

Parameters
----------
x1, x2 : array_like
    Input arrays.
    If ``x1.shape != x2.shape``, they must be broadcastable to a common

def lexsort(keys, axis=-1):
    lexsort(keys, axis=-1)

Perform an indirect stable sort using a sequence of keys.

Given multiple sorting keys, lexsort returns an array of integer indices
that describes the sort order by multiple keys. The last key in the
sequence is used for the primary sort order, ties are broken by the
second-t

def linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0, *, device=None):
    
    Return evenly spaced numbers over a specified interval.

    Returns `num` evenly spaced samples, calculated over the
    interval [`start`, `stop`].

    The endpoint of the interval can optionally be excluded.

    .. versionchanged:: 1.20.0
        Values are rounded towards ``-inf`` instead

def load(file, mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII', *, max_header_size=10:
    
    Load arrays or pickled objects from ``.npy``, ``.npz`` or pickled files.

    .. warning:: Loading files that contain object arrays uses the ``pickle``
                 module, which is not secure against erroneous or maliciously
                 constructed data. Consider passing ``allow_pickl

def loadtxt(fname, dtype=<class 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=No:
    
    Load data from a text file.

    Parameters
    ----------
    fname : file, str, pathlib.Path, list of str, generator
        File, filename, list, or generator to read.  If the filename
        extension is ``.gz`` or ``.bz2``, the file is first decompressed. Note
        that generators must

def log(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    log(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Natural logarithm, element-wise.

The natural logarithm `log` is the inverse of the exponential function,
so that `log(exp(x)) = x`. The natural logarithm is logarithm in base
`e`.

Parameters
--

def log10(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    log10(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Return the base 10 logarithm of the input array, element-wise.

Parameters
----------
x : array_like
    Input values.
out : ndarray, None, or tuple of ndarray and None, optional
    A location

def log1p(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    log1p(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Return the natural logarithm of one plus the input array, element-wise.

Calculates ``log(1 + x)``.

Parameters
----------
x : array_like
    Input values.
out : ndarray, None, or tuple of ndar

def log2(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    log2(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Base-2 logarithm of `x`.

Parameters
----------
x : array_like
    Input values.
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which the result is stored. If pr

def logaddexp(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    logaddexp(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Logarithm of the sum of exponentiations of the inputs.

Calculates ``log(exp(x1) + exp(x2))``. This function is useful in
statistics where the calculated probabilities of events may be

def logaddexp2(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    logaddexp2(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Logarithm of the sum of exponentiations of the inputs in base-2.

Calculates ``log2(2**x1 + 2**x2)``. This function is useful in machine
learning when the calculated probabilities of 

def logical_and(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    logical_and(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Compute the truth value of x1 AND x2 element-wise.

Parameters
----------
x1, x2 : array_like
    Input arrays.
    If ``x1.shape != x2.shape``, they must be broadcastable to a commo

def logical_not(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    logical_not(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Compute the truth value of NOT x element-wise.

Parameters
----------
x : array_like
    Logical NOT is applied to the elements of `x`.
out : ndarray, None, or tuple of ndarray and None, 

def logical_or(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    logical_or(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Compute the truth value of x1 OR x2 element-wise.

Parameters
----------
x1, x2 : array_like
    Logical OR is applied to the elements of `x1` and `x2`.
    If ``x1.shape != x2.shape`

def logical_xor(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    logical_xor(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Compute the truth value of x1 XOR x2, element-wise.

Parameters
----------
x1, x2 : array_like
    Logical XOR is applied to the elements of `x1` and `x2`.
    If ``x1.shape != x2.sh

def logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0):
    
    Return numbers spaced evenly on a log scale.

    In linear space, the sequence starts at ``base ** start``
    (`base` to the power of `start`) and ends with ``base ** stop``
    (see `endpoint` below).

    .. versionchanged:: 1.25.0
        Non-scalar 'base` is now supported

    Parameters


def long(value=0, /):
    Signed integer type, compatible with C ``long``.

:Character code: ``'l'``
:Canonical name: `numpy.long`
:Alias on this platform (Linux x86_64): `numpy.int64`: 64-bit signed integer (``-9_223_372_036_854_775_808`` to ``9_223_372_036_854_775_807``).
:Alias on this platform (Linux x86_64): `numpy.intp

def longdouble(value=0, /):
    Extended-precision floating-point number type, compatible with C ``long double``
but not necessarily with IEEE 754 quadruple-precision.

:Character code: ``'g'``
:Alias on this platform (Linux x86_64): `numpy.float128`: 128-bit extended-precision floating-point number type.

def longlong(value=0, /):
    Signed integer type, compatible with C ``long long``.

:Character code: ``'q'``

def mask_indices(n, mask_func, k=0):
    
    Return the indices to access (n, n) arrays, given a masking function.

    Assume `mask_func` is a function that, for a square array a of size
    ``(n, n)`` with a possible offset argument `k`, when called as
    ``mask_func(a, k)`` returns a new array with zeros in certain locations
    (func

def matmul(x1, x2, /, out=None, *, axes=<no value>, axis=<no value>, keepdims=False, casting='same_kind', orde:
    matmul(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])

Matrix product of two arrays.

Parameters
----------
x1, x2 : array_like
    Input arrays, scalars not allowed.
out : ndarray, optional
    A location into which the result is stored. If 

def matrix(data, dtype=None, copy=True):
    
    matrix(data, dtype=None, copy=True)

    Returns a matrix from an array-like object, or from a string of data.

    A matrix is a specialized 2-D array that retains its 2-D nature
    through operations.  It has certain special operators, such as ``*``
    (matrix multiplication) and ``**`` (ma

def matrix_transpose(x, /):
    
    Transposes a matrix (or a stack of matrices) ``x``.

    This function is Array API compatible.

    Parameters
    ----------
    x : array_like
        Input array having shape (..., M, N) and whose two innermost
        dimensions form ``MxN`` matrices.

    Returns
    -------
    out : nda

def matvec(x1, x2, /, out=None, *, axes=<no value>, axis=<no value>, keepdims=False, casting='same_kind', orde:
    matvec(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])

Matrix-vector dot product of two arrays.

Given a matrix (or stack of matrices) :math:`\mathbf{A}` in ``x1`` and
a vector (or stack of vectors) :math:`\mathbf{v}` in ``x2``, the
matrix-ve

def max(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>):
    
    Return the maximum of an array or maximum along an axis.

    Parameters
    ----------
    a : array_like
        Input data.
    axis : None or int or tuple of ints, optional
        Axis or axes along which to operate.  By default, flattened input is
        used. If this is a tuple of ints,

def maximum(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    maximum(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Element-wise maximum of array elements.

Compare two arrays and return a new array containing the element-wise
maxima. If one of the elements being compared is a NaN, then that
element i

def may_share_memory(a, b, /, max_work=0):
    may_share_memory(a, b, /, max_work=0)

Determine if two arrays might share memory

A return of True does not necessarily mean that the two arrays
share any element.  It just means that they *might*.

Only the memory bounds of a and b are checked by default.

Parameters
----------
a, b : ndarray
    

def mean(a, axis=None, dtype=None, out=None, keepdims=<no value>, *, where=<no value>):
    
    Compute the arithmetic mean along the specified axis.

    Returns the average of the array elements.  The average is taken over
    the flattened array by default, otherwise over the specified axis.
    `float64` intermediate and return values are used for integer inputs.

    Parameters
    -

def median(a, axis=None, out=None, overwrite_input=False, keepdims=False):
    
    Compute the median along the specified axis.

    Returns the median of the array elements.

    Parameters
    ----------
    a : array_like
        Input array or object that can be converted to an array.
    axis : {int, sequence of int, None}, optional
        Axis or axes along which the m

def memmap(filename, dtype=<class 'numpy.uint8'>, mode='r+', offset=0, shape=None, order='C'):
    Create a memory-map to an array stored in a *binary* file on disk.

    Memory-mapped files are used for accessing small segments of large files
    on disk, without reading the entire file into memory.  NumPy's
    memmap's are array-like objects.  This differs from Python's ``mmap``
    module, wh

def meshgrid(*xi, copy=True, sparse=False, indexing='xy'):
    
    Return a tuple of coordinate matrices from coordinate vectors.

    Make N-D coordinate arrays for vectorized evaluations of
    N-D scalar/vector fields over N-D grids, given
    one-dimensional coordinate arrays x1, x2,..., xn.

    Parameters
    ----------
    x1, x2,..., xn : array_like
  

def min(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>):
    
    Return the minimum of an array or minimum along an axis.

    Parameters
    ----------
    a : array_like
        Input data.
    axis : None or int or tuple of ints, optional
        Axis or axes along which to operate.  By default, flattened input is
        used.

        If this is a tuple

def min_scalar_type(a, /):
    min_scalar_type(a, /)

For scalar ``a``, returns the data type with the smallest size
and smallest scalar kind which can hold its value.  For non-scalar
array ``a``, returns the vector's dtype unmodified.

Floating point values are not demoted to integers,
and complex values are not demoted to float

def minimum(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    minimum(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Element-wise minimum of array elements.

Compare two arrays and return a new array containing the element-wise
minima. If one of the elements being compared is a NaN, then that
element i

def mintypecode(typechars, typeset='GDFgdf', default='d'):
    
    Return the character for the minimum-size type to which given types can
    be safely cast.

    The returned type character must represent the smallest size dtype such
    that an array of the returned type can handle the data from an array of
    all types in `typechars` (or if `typechars` is

def mod(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    remainder(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Returns the element-wise remainder of division.

Computes the remainder complementary to the `floor_divide` function.  It is
equivalent to the Python modulus operator ``x1 % x2`` and h

def modf(x, /, out=(None, None), *, where=True, casting='same_kind', order='K', dtype=None, subok=True, sign:
    modf(x[, out1, out2], / [, out=(None, None)], *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Return the fractional and integral parts of an array, element-wise.

The fractional and integral parts are negative if the given number is
negative.

Parameters
--------

def moveaxis(a, source, destination):
    
    Move axes of an array to new positions.

    Other axes remain in their original order.

    Parameters
    ----------
    a : np.ndarray
        The array whose axes should be reordered.
    source : int or sequence of int
        Original positions of the axes to move. These must be unique.
 

def multiply(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    multiply(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Multiply arguments element-wise.

Parameters
----------
x1, x2 : array_like
    Input arrays to be multiplied.
    If ``x1.shape != x2.shape``, they must be broadcastable to a common
  

def nan_to_num(x, copy=True, nan=0.0, posinf=None, neginf=None):
    
    Replace NaN with zero and infinity with large finite numbers (default
    behaviour) or with the numbers defined by the user using the `nan`,
    `posinf` and/or `neginf` keywords.

    If `x` is inexact, NaN is replaced by zero or by the user defined value in
    `nan` keyword, infinity is rep

def nanargmax(a, axis=None, out=None, *, keepdims=<no value>):
    
    Return the indices of the maximum values in the specified axis ignoring
    NaNs. For all-NaN slices ``ValueError`` is raised. Warning: the
    results cannot be trusted if a slice contains only NaNs and -Infs.


    Parameters
    ----------
    a : array_like
        Input data.
    axis : in

def nanargmin(a, axis=None, out=None, *, keepdims=<no value>):
    
    Return the indices of the minimum values in the specified axis ignoring
    NaNs. For all-NaN slices ``ValueError`` is raised. Warning: the results
    cannot be trusted if a slice contains only NaNs and Infs.

    Parameters
    ----------
    a : array_like
        Input data.
    axis : int,

def nancumprod(a, axis=None, dtype=None, out=None):
    
    Return the cumulative product of array elements over a given axis treating Not a
    Numbers (NaNs) as one.  The cumulative product does not change when NaNs are
    encountered and leading NaNs are replaced by ones.

    Ones are returned for slices that are all-NaN or empty.

    Parameters
 

def nancumsum(a, axis=None, dtype=None, out=None):
    
    Return the cumulative sum of array elements over a given axis treating Not a
    Numbers (NaNs) as zero.  The cumulative sum does not change when NaNs are
    encountered and leading NaNs are replaced by zeros.

    Zeros are returned for slices that are all-NaN or empty.

    Parameters
    --

def nanmax(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>):
    
    Return the maximum of an array or maximum along an axis, ignoring any
    NaNs.  When all-NaN slices are encountered a ``RuntimeWarning`` is
    raised and NaN is returned for that slice.

    Parameters
    ----------
    a : array_like
        Array containing numbers whose maximum is desired

def nanmean(a, axis=None, dtype=None, out=None, keepdims=<no value>, *, where=<no value>):
    
    Compute the arithmetic mean along the specified axis, ignoring NaNs.

    Returns the average of the array elements.  The average is taken over
    the flattened array by default, otherwise over the specified axis.
    `float64` intermediate and return values are used for integer inputs.

    F

def nanmedian(a, axis=None, out=None, overwrite_input=False, keepdims=<no value>):
    
    Compute the median along the specified axis, while ignoring NaNs.

    Returns the median of the array elements.

    Parameters
    ----------
    a : array_like
        Input array or object that can be converted to an array.
    axis : {int, sequence of int, None}, optional
        Axis or a

def nanmin(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>):
    
    Return minimum of an array or minimum along an axis, ignoring any NaNs.
    When all-NaN slices are encountered a ``RuntimeWarning`` is raised and
    Nan is returned for that slice.

    Parameters
    ----------
    a : array_like
        Array containing numbers whose minimum is desired. If 

def nanpercentile(a, q, axis=None, out=None, overwrite_input=False, method='linear', keepdims=<no value>, *, weights=:
    
    Compute the qth percentile of the data along the specified axis,
    while ignoring nan values.

    Returns the qth percentile(s) of the array elements.

    Parameters
    ----------
    a : array_like
        Input array or object that can be converted to an array, containing
        nan val

def nanprod(a, axis=None, dtype=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>):
    
    Return the product of array elements over a given axis treating Not a
    Numbers (NaNs) as ones.

    One is returned for slices that are all-NaN or empty.

    Parameters
    ----------
    a : array_like
        Array containing numbers whose product is desired. If `a` is not an
        arra

def nanquantile(a, q, axis=None, out=None, overwrite_input=False, method='linear', keepdims=<no value>, *, weights=:
    
    Compute the qth quantile of the data along the specified axis,
    while ignoring nan values.
    Returns the qth quantile(s) of the array elements.

    Parameters
    ----------
    a : array_like
        Input array or object that can be converted to an array, containing
        nan values t

def nanstd(a, axis=None, dtype=None, out=None, ddof=0, keepdims=<no value>, *, where=<no value>, mean=<no valu:
    
    Compute the standard deviation along the specified axis, while
    ignoring NaNs.

    Returns the standard deviation, a measure of the spread of a
    distribution, of the non-NaN array elements. The standard deviation is
    computed for the flattened array by default, otherwise over the
    

def nansum(a, axis=None, dtype=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>):
    
    Return the sum of array elements over a given axis treating Not a
    Numbers (NaNs) as zero.

    In NumPy versions <= 1.9.0 Nan is returned for slices that are all-NaN or
    empty. In later versions zero is returned.

    Parameters
    ----------
    a : array_like
        Array containing 

def nanvar(a, axis=None, dtype=None, out=None, ddof=0, keepdims=<no value>, *, where=<no value>, mean=<no valu:
    
    Compute the variance along the specified axis, while ignoring NaNs.

    Returns the variance of the array elements, a measure of the spread of
    a distribution.  The variance is computed for the flattened array by
    default, otherwise over the specified axis.

    For all-NaN slices or sli

def ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None):
    ndarray(shape, dtype=float, buffer=None, offset=0, strides=None, order=None)

An array object represents a multidimensional, homogeneous array
of fixed-size items.  An associated data-type object describes the
format of each element in the array (its byte-order, how many bytes it
occupies in memory,

def ndenumerate(arr):
    
    Multidimensional index iterator.

    Return an iterator yielding pairs of array coordinates and values.

    Parameters
    ----------
    arr : ndarray
      Input array.

    See Also
    --------
    ndindex, flatiter

    Examples
    --------
    >>> import numpy as np
    >>> a = np.arra

def ndim(a):
    
    Return the number of dimensions of an array.

    Parameters
    ----------
    a : array_like
        Input array.  If it is not already an ndarray, a conversion is
        attempted.

    Returns
    -------
    number_of_dimensions : int
        The number of dimensions in `a`.  Scalars are 

def ndindex(*shape):
    
    An N-dimensional iterator object to index arrays.

    Given the shape of an array, an `ndindex` instance iterates over
    the N-dimensional index of the array. At each iteration a tuple
    of indices is returned, the last dimension is iterated over first.

    Parameters
    ----------
    s

def nditer(op, flags=None, op_flags=None, op_dtypes=None, order='K', casting='safe', op_axes=None, itershape=N:
    nditer(op, flags=None, op_flags=None, op_dtypes=None, order='K',
    casting='safe', op_axes=None, itershape=None, buffersize=0)

Efficient multi-dimensional iterator object to iterate over arrays.
To get started using this object, see the
:ref:`introductory guide to array iteration <arrays.nditer>`

def negative(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    negative(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Numerical negative, element-wise.

Parameters
----------
x : array_like or scalar
    Input array.
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which the r

def nested_iters(op, axes, flags=None, op_flags=None, op_dtypes=None, order='K', casting='safe', buffersize=0):
    nested_iters(op, axes, flags=None, op_flags=None, op_dtypes=None,
order='K', casting='safe', buffersize=0)

Create nditers for use in nested loops

Create a tuple of `nditer` objects which iterate in nested loops over
different axes of the op argument. The first iterator is used in the
outermost loo

def nextafter(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    nextafter(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Return the next floating-point value after x1 towards x2, element-wise.

Parameters
----------
x1 : array_like
    Values to find the next representable value of.
x2 : array_like
    T

def nonzero(a):
    
    Return the indices of the elements that are non-zero.

    Returns a tuple of arrays, one for each dimension of `a`,
    containing the indices of the non-zero elements in that
    dimension. The values in `a` are always tested and returned in
    row-major, C-style order.

    To group the ind

def not_equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    not_equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Return (x1 != x2) element-wise.

Parameters
----------
x1, x2 : array_like
    Input arrays.
    If ``x1.shape != x2.shape``, they must be broadcastable to a common
    shape (which be

def number():
    Abstract base class of all numeric scalar types.

def object_(value=None, /):
    Any Python object.

:Character code: ``'O'``

def ones(shape, dtype=None, order='C', *, device=None, like=None):
    
    Return a new array of given shape and type, filled with ones.

    Parameters
    ----------
    shape : int or sequence of ints
        Shape of the new array, e.g., ``(2, 3)`` or ``2``.
    dtype : data-type, optional
        The desired data-type for the array, e.g., `numpy.int8`.  Default i

def ones_like(a, dtype=None, order='K', subok=True, shape=None, *, device=None):
    
    Return an array of ones with the same shape and type as a given array.

    Parameters
    ----------
    a : array_like
        The shape and data-type of `a` define these same attributes of
        the returned array.
    dtype : data-type, optional
        Overrides the data type of the resu

def outer(a, b, out=None):
    
    Compute the outer product of two vectors.

    Given two vectors `a` and `b` of length ``M`` and ``N``, respectively,
    the outer product [1]_ is::

      [[a_0*b_0  a_0*b_1 ... a_0*b_{N-1} ]
       [a_1*b_0    .
       [ ...          .
       [a_{M-1}*b_0            a_{M-1}*b_{N-1} ]]

    P

def packbits(a, /, axis=None, bitorder='big'):
    packbits(a, /, axis=None, bitorder='big')

Packs the elements of a binary-valued array into bits in a uint8 array.

The result is padded to full bytes by inserting zero bits at the end.

Parameters
----------
a : array_like
    An array of integers or booleans whose elements should be packed to
    

def pad(array, pad_width, mode='constant', **kwargs):
    
    Pad an array.

    Parameters
    ----------
    array : array_like of rank N
        The array to pad.
    pad_width : {sequence, array_like, int, dict}
        Number of values padded to the edges of each axis.
        ``((before_1, after_1), ... (before_N, after_N))`` unique pad widths
     

def partition(a, kth, axis=-1, kind='introselect', order=None):
    
    Return a partitioned copy of an array.

    Creates a copy of the array and partially sorts it in such a way that
    the value of the element in k-th position is in the position it would be
    in a sorted array. In the output array, all elements smaller than the k-th
    element are located t

def percentile(a, q, axis=None, out=None, overwrite_input=False, method='linear', keepdims=False, *, weights=None):
    
    Compute the q-th percentile of the data along the specified axis.

    Returns the q-th percentile(s) of the array elements.

    Parameters
    ----------
    a : array_like of real numbers
        Input array or object that can be converted to an array.
    q : array_like of float
        Per

def permute_dims(a, axes=None):
    
    Returns an array with axes transposed.

    For a 1-D array, this returns an unchanged view of the original array, as a
    transposed vector is simply the same vector.
    To convert a 1-D array into a 2-D column vector, an additional dimension
    must be added, e.g., ``np.atleast_2d(a).T`` a

def piecewise(x, condlist, funclist, *args, **kw):
    
    Evaluate a piecewise-defined function.

    Given a set of conditions and corresponding functions, evaluate each
    function on the input data wherever its condition is true.

    Parameters
    ----------
    x : ndarray or scalar
        The input domain.
    condlist : list of bool arrays o

def place(arr, mask, vals):
    
    Change elements of an array based on conditional and input values.

    Similar to ``np.copyto(arr, vals, where=mask)``, the difference is that
    `place` uses the first N elements of `vals`, where N is the number of
    True values in `mask`, while `copyto` uses the elements where `mask`
    

def poly(seq_of_zeros):
    
    Find the coefficients of a polynomial with the given sequence of roots.

    .. note::
       This forms part of the old polynomial API. Since version 1.4, the
       new polynomial API defined in `numpy.polynomial` is preferred.
       A summary of the differences can be found in the
       :d

def poly1d(c_or_r, r=False, variable=None):
    
    A one-dimensional polynomial class.

    .. note::
       This forms part of the old polynomial API. Since version 1.4, the
       new polynomial API defined in `numpy.polynomial` is preferred.
       A summary of the differences can be found in the
       :doc:`transition guide </reference/rou

def polyadd(a1, a2):
    
    Find the sum of two polynomials.

    .. note::
       This forms part of the old polynomial API. Since version 1.4, the
       new polynomial API defined in `numpy.polynomial` is preferred.
       A summary of the differences can be found in the
       :doc:`transition guide </reference/routin

def polyder(p, m=1):
    
    Return the derivative of the specified order of a polynomial.

    .. note::
       This forms part of the old polynomial API. Since version 1.4, the
       new polynomial API defined in `numpy.polynomial` is preferred.
       A summary of the differences can be found in the
       :doc:`transi

def polydiv(u, v):
    
    Returns the quotient and remainder of polynomial division.

    .. note::
       This forms part of the old polynomial API. Since version 1.4, the
       new polynomial API defined in `numpy.polynomial` is preferred.
       A summary of the differences can be found in the
       :doc:`transitio

def polyfit(x, y, deg, rcond=None, full=False, w=None, cov=False):
    
    Least squares polynomial fit.

    .. note::
       This forms part of the old polynomial API. Since version 1.4, the
       new polynomial API defined in `numpy.polynomial` is preferred.
       A summary of the differences can be found in the
       :doc:`transition guide </reference/routines.

def polyint(p, m=1, k=None):
    
    Return an antiderivative (indefinite integral) of a polynomial.

    .. note::
       This forms part of the old polynomial API. Since version 1.4, the
       new polynomial API defined in `numpy.polynomial` is preferred.
       A summary of the differences can be found in the
       :doc:`tran

def polymul(a1, a2):
    
    Find the product of two polynomials.

    .. note::
       This forms part of the old polynomial API. Since version 1.4, the
       new polynomial API defined in `numpy.polynomial` is preferred.
       A summary of the differences can be found in the
       :doc:`transition guide </reference/ro

def polysub(a1, a2):
    
    Difference (subtraction) of two polynomials.

    .. note::
       This forms part of the old polynomial API. Since version 1.4, the
       new polynomial API defined in `numpy.polynomial` is preferred.
       A summary of the differences can be found in the
       :doc:`transition guide </refe

def polyval(p, x):
    
    Evaluate a polynomial at specific values.

    .. note::
       This forms part of the old polynomial API. Since version 1.4, the
       new polynomial API defined in `numpy.polynomial` is preferred.
       A summary of the differences can be found in the
       :doc:`transition guide </referen

def positive(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    positive(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Numerical positive, element-wise.

Parameters
----------
x : array_like or scalar
    Input array.

Returns
-------
y : ndarray or scalar
    Returned array or scalar: `y = +x`.
    This is 

def pow(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    power(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

First array elements raised to powers from second array, element-wise.

Raise each base in `x1` to the positionally-corresponding power in
`x2`.  `x1` and `x2` must be broadcastable to the

def power(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    power(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

First array elements raised to powers from second array, element-wise.

Raise each base in `x1` to the positionally-corresponding power in
`x2`.  `x1` and `x2` must be broadcastable to the

def printoptions(*args, **kwargs):
    Context manager for setting print options.

    Set print options for the scope of the `with` block, and restore the old
    options at the end. See `set_printoptions` for the full description of
    available options.

    Examples
    --------
    >>> import numpy as np

    >>> from numpy.testing

def prod(a, axis=None, dtype=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>):
    
    Return the product of array elements over a given axis.

    Parameters
    ----------
    a : array_like
        Input data.
    axis : None or int or tuple of ints, optional
        Axis or axes along which a product is performed.  The default,
        axis=None, will calculate the product of

def promote_types(type1, type2, /):
    promote_types(type1, type2, /)

Returns the data type with the smallest size and smallest scalar
kind to which both ``type1`` and ``type2`` may be safely cast.
The returned data type is always considered "canonical", this mainly
means that the promoted dtype will always be in native byte order.

Thi

def ptp(a, axis=None, out=None, keepdims=<no value>):
    
    Range of values (maximum - minimum) along an axis.

    The name of the function comes from the acronym for 'peak to peak'.

    .. warning::
        `ptp` preserves the data type of the array. This means the
        return value for an input of signed integers with n bits
        (e.g. `numpy.

def put(a, ind, v, mode='raise'):
    
    Replaces specified elements of an array with given values.

    The indexing works on the flattened target array. `put` is roughly
    equivalent to:

    ::

        a.flat[ind] = v

    Parameters
    ----------
    a : ndarray
        Target array.
    ind : array_like
        Target indices

def put_along_axis(arr, indices, values, axis):
    
    Put values into the destination array by matching 1d index and data slices.

    This iterates over matching 1d slices oriented along the specified axis in
    the index and data arrays, and uses the former to place values into the
    latter. These slices can be different lengths.

    Functio

def putmask(a, /, mask, values):
    putmask(a, /, mask, values)

Changes elements of an array based on conditional and input values.

Sets ``a.flat[n] = values[n]`` for each n where ``mask.flat[n]==True``.

If `values` is not the same size as `a` and `mask` then it will repeat.
This gives behavior different from ``a[mask] = values``.


def quantile(a, q, axis=None, out=None, overwrite_input=False, method='linear', keepdims=False, *, weights=None):
    
    Compute the q-th quantile of the data along the specified axis.

    Parameters
    ----------
    a : array_like of real numbers
        Input array or object that can be converted to an array.
    q : array_like of float
        Probability or sequence of probabilities of the quantiles to com

def rad2deg(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    rad2deg(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Convert angles from radians to degrees.

Parameters
----------
x : array_like
    Angle in radians.
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which the r

def radians(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    radians(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Convert angles from degrees to radians.

Parameters
----------
x : array_like
    Input array in degrees.
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which

def ravel(a, order='C'):
    Return a contiguous flattened array.

    A 1-D array, containing the elements of the input, is returned.  A copy is
    made only if needed.

    As of NumPy 1.10, the returned array will have the same type as the input
    array. (for example, a masked array will be returned for a masked array
   

def ravel_multi_index(multi_index, dims, mode='raise', order='C'):
    ravel_multi_index(multi_index, dims, mode='raise', order='C')

Converts a tuple of index arrays into an array of flat
indices, applying boundary modes to the multi-index.

Parameters
----------
multi_index : tuple of array_like
    A tuple of integer arrays, one array for each dimension.
dims : tupl

def real(val):
    
    Return the real part of the complex argument.

    Parameters
    ----------
    val : array_like
        Input array.

    Returns
    -------
    out : ndarray or scalar
        The real component of the complex argument. If `val` is real, the type
        of `val` is used for the output.  If

def real_if_close(a, tol=100):
    
    If input is complex with all imaginary parts close to zero, return
    real parts.

    "Close to zero" is defined as `tol` * (machine epsilon of the type for
    `a`).

    Parameters
    ----------
    a : array_like
        Input array.
    tol : float
        Tolerance in machine epsilons f

def recarray(shape, dtype=None, buf=None, offset=0, strides=None, formats=None, names=None, titles=None, byteord:
    Construct an ndarray that allows field access using attributes.

    Arrays may have a data-types containing fields, analogous
    to columns in a spread sheet.  An example is ``[(x, int), (y, float)]``,
    where each entry in the array is a pair of ``(int, float)``.  Normally,
    these attributes

def reciprocal(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    reciprocal(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Return the reciprocal of the argument, element-wise.

Calculates ``1/x``.

Parameters
----------
x : array_like
    Input array.
out : ndarray, None, or tuple of ndarray and None, optional

def record(length_or_data, /, dtype=None):
    A data-type scalar that allows field access as attribute lookup.
    

def remainder(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    remainder(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Returns the element-wise remainder of division.

Computes the remainder complementary to the `floor_divide` function.  It is
equivalent to the Python modulus operator ``x1 % x2`` and h

def repeat(a, repeats, axis=None):
    
    Repeat each element of an array after themselves

    Parameters
    ----------
    a : array_like
        Input array.
    repeats : int or array of ints
        The number of repetitions for each element.  `repeats` is broadcasted
        to fit the shape of the given axis.
    axis : int, op

def require(a, dtype=None, requirements=None, *, like=None):
    
    Return an ndarray of the provided type that satisfies requirements.

    This function is useful to be sure that an array with the correct flags
    is returned for passing to compiled code (perhaps through ctypes).

    Parameters
    ----------
    a : array_like
       The object to be conve

def reshape(a, /, shape, order='C', *, copy=None):
    
    Gives a new shape to an array without changing its data.

    Parameters
    ----------
    a : array_like
        Array to be reshaped.
    shape : int or tuple of ints
        The new shape should be compatible with the original shape. If
        an integer, then the result will be a 1-D arra

def resize(a, new_shape):
    
    Return a new array with the specified shape.

    If the new array is larger than the original array, then the new
    array is filled with repeated copies of `a`.  Note that this behavior
    is different from a.resize(new_shape) which fills with zeros instead
    of repeated copies of `a`.

 

def result_type(*arrays_and_dtypes):
    result_type(*arrays_and_dtypes)

Returns the type that results from applying the NumPy
:ref:`type promotion <arrays.promotion>` rules to the arguments.

Parameters
----------
arrays_and_dtypes : list of arrays and dtypes
    The operands of some operation whose result type is needed.

Returns
------

def right_shift(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    right_shift(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Shift the bits of an integer to the right.

Bits are shifted to the right `x2`.  Because the internal
representation of numbers is in binary format, this operation is
equivalent to d

def rint(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    rint(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Round elements of the array to the nearest integer.

Parameters
----------
x : array_like
    Input array.
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which t

def roll(a, shift, axis=None):
    
    Roll array elements along a given axis.

    Elements that roll beyond the last position are re-introduced at
    the first.

    Parameters
    ----------
    a : array_like
        Input array.
    shift : int or tuple of ints
        The number of places by which elements are shifted.  If a 

def rollaxis(a, axis, start=0):
    
    Roll the specified axis backwards, until it lies in a given position.

    This function continues to be supported for backward compatibility, but you
    should prefer `moveaxis`. The `moveaxis` function was added in NumPy
    1.11.

    Parameters
    ----------
    a : ndarray
        Input 

def roots(p):
    
    Return the roots of a polynomial with coefficients given in p.

    .. note::
       This forms part of the old polynomial API. Since version 1.4, the
       new polynomial API defined in `numpy.polynomial` is preferred.
       A summary of the differences can be found in the
       :doc:`trans

def rot90(m, k=1, axes=(0, 1)):
    
    Rotate an array by 90 degrees in the plane specified by axes.

    Rotation direction is from the first towards the second axis.
    This means for a 2D array with the default `k` and `axes`, the
    rotation will be counterclockwise.

    Parameters
    ----------
    m : array_like
        Ar

def round(a, decimals=0, out=None):
    
    Evenly round to the given number of decimals.

    Parameters
    ----------
    a : array_like
        Input data.
    decimals : int, optional
        Number of decimal places to round to (default: 0).  If
        decimals is negative, it specifies the number of positions to
        the left 

def row_stack(tup, *, dtype=None, casting='same_kind'):
    
    Stack arrays in sequence vertically (row wise).

    This is equivalent to concatenation along the first axis after 1-D arrays
    of shape `(N,)` have been reshaped to `(1,N)`. Rebuilds arrays divided by
    `vsplit`.

    This function makes most sense for arrays with up to 3 dimensions. For


def save(file, arr, allow_pickle=True):
    
    Save an array to a binary file in NumPy ``.npy`` format.

    Parameters
    ----------
    file : file, str, or pathlib.Path
        File or filename to which the data is saved. If file is a file-object,
        then the filename is unchanged.  If file is a string or Path,
        a ``.npy`` e

def savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=N:
    
    Save an array to a text file.

    Parameters
    ----------
    fname : filename, file handle or pathlib.Path
        If the filename ends in ``.gz``, the file is automatically saved in
        compressed gzip format.  `loadtxt` understands gzipped files
        transparently.
    X : 1D or 2D

def savez(file, *args, allow_pickle=True, **kwds):
    Save several arrays into a single file in uncompressed ``.npz`` format.

    Provide arrays as keyword arguments to store them under the
    corresponding name in the output file: ``savez(fn, x=x, y=y)``.

    If arrays are specified as positional arguments, i.e., ``savez(fn,
    x, y)``, their name

def savez_compressed(file, *args, allow_pickle=True, **kwds):
    
    Save several arrays into a single file in compressed ``.npz`` format.

    Provide arrays as keyword arguments to store them under the
    corresponding name in the output file: ``savez_compressed(fn, x=x, y=y)``.

    If arrays are specified as positional arguments, i.e.,
    ``savez_compresse

def searchsorted(a, v, side='left', sorter=None):
    
    Find indices where elements should be inserted to maintain order.

    Find the indices into a sorted array `a` such that, if the
    corresponding elements in `v` were inserted before the indices, the
    order of `a` would be preserved.

    Assuming that `a` is sorted:

    ======  =========

def select(condlist, choicelist, default=0):
    
    Return an array drawn from elements in choicelist, depending on conditions.

    Parameters
    ----------
    condlist : list of bool ndarrays
        The list of conditions which determine from which array in `choicelist`
        the output elements are taken. When multiple conditions are sat

def set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, suppress=None, nanstr=None, infstr=:
    
    Set printing options.

    These options determine the way floating point numbers, arrays and
    other NumPy objects are displayed.

    Parameters
    ----------
    precision : int or None, optional
        Number of digits of precision for floating point output (default 8).
        May be N

def setbufsize(size):
    
    Set the size of the buffer used in ufuncs.

    .. versionchanged:: 2.0
        The scope of setting the buffer is tied to the `numpy.errstate`
        context.  Exiting a ``with errstate():`` will also restore the bufsize.

    Parameters
    ----------
    size : int
        Size of buffer.



def setdiff1d(ar1, ar2, assume_unique=False):
    
    Find the set difference of two arrays.

    Return the unique values in `ar1` that are not in `ar2`.

    Parameters
    ----------
    ar1 : array_like
        Input array.
    ar2 : array_like
        Input comparison array.
    assume_unique : bool
        If True, the input arrays are both 

def seterr(all=None, divide=None, over=None, under=None, invalid=None):
    
    Set how floating-point errors are handled.

    Note that operations on integer scalar types (such as `int16`) are
    handled like floating point, and are affected by these settings.

    Parameters
    ----------
    all : {'ignore', 'warn', 'raise', 'call', 'print', 'log'}, optional
        

def seterrcall(func):
    
    Set the floating-point error callback function or log object.

    There are two ways to capture floating-point error messages.  The first
    is to set the error-handler to 'call', using `seterr`.  Then, set
    the function to call using this function.

    The second is to set the error-hand

def setxor1d(ar1, ar2, assume_unique=False):
    
    Find the set exclusive-or of two arrays.

    Return the sorted, unique values that are in only one (not both) of the
    input arrays.

    Parameters
    ----------
    ar1, ar2 : array_like
        Input arrays.
    assume_unique : bool
        If True, the input arrays are both assumed to b

def shape(a):
    
    Return the shape of an array.

    Parameters
    ----------
    a : array_like
        Input array.

    Returns
    -------
    shape : tuple of ints
        The elements of the shape tuple give the lengths of the
        corresponding array dimensions.

    See Also
    --------
    len : ``

def shares_memory(a, b, /, max_work=-1):
    shares_memory(a, b, /, max_work=-1)

Determine if two arrays share memory.

.. warning::

   This function can be exponentially slow for some inputs, unless
   `max_work` is set to zero or a positive integer.
   If in doubt, use `numpy.may_share_memory` instead.

Parameters
----------
a, b : ndarray

def short(value=0, /):
    Signed integer type, compatible with C ``short``.

:Character code: ``'h'``
:Canonical name: `numpy.short`
:Alias on this platform (Linux x86_64): `numpy.int16`: 16-bit signed integer (``-32_768`` to ``32_767``).

def show_config(mode='stdout'):
    
    Show libraries and system information on which NumPy was built
    and is being used

    Parameters
    ----------
    mode : {`'stdout'`, `'dicts'`}, optional.
        Indicates how to display the config information.
        `'stdout'` prints to console, `'dicts'` returns a dictionary
       

def show_runtime():
    
    Print information about various resources in the system
    including available intrinsic support and BLAS/LAPACK library
    in use

    .. versionadded:: 1.24.0

    See Also
    --------
    show_config : Show libraries in the system on which NumPy was built.

    Notes
    -----
    1. Info

def sign(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    sign(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Returns an element-wise indication of the sign of a number.

The `sign` function returns ``-1 if x < 0, 0 if x==0, 1 if x > 0``.  nan
is returned for nan inputs.

For complex inputs, the `sign` 

def signbit(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    signbit(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Returns element-wise True where signbit is set (less than zero).

Parameters
----------
x : array_like
    The input value(s).
out : ndarray, None, or tuple of ndarray and None, optional
    

def signedinteger():
    Abstract base class of all signed integer scalar types.

def sin(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    sin(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Trigonometric sine, element-wise.

Parameters
----------
x : array_like
    Angle, in radians (:math:`2 \pi` rad equals 360 degrees).
out : ndarray, None, or tuple of ndarray and None, optional
 

def sinc(x):
    
    Return the normalized sinc function.

    The sinc function is equal to :math:`\sin(\pi x)/(\pi x)` for any argument
    :math:`x\ne 0`. ``sinc(0)`` takes the limit value 1, making ``sinc`` not
    only everywhere continuous but also infinitely differentiable.

    .. note::

        Note the n

def single(value=0, /):
    Single-precision floating-point number type, compatible with C ``float``.

:Character code: ``'f'``
:Canonical name: `numpy.single`
:Alias on this platform (Linux x86_64): `numpy.float32`: 32-bit-precision floating-point number type: sign bit, 8 bits exponent, 23 bits mantissa.

def sinh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    sinh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Hyperbolic sine, element-wise.

Equivalent to ``1/2 * (np.exp(x) - np.exp(-x))`` or
``-1j * np.sin(1j*x)``.

Parameters
----------
x : array_like
    Input array.
out : ndarray, None, or tuple o

def size(a, axis=None):
    
    Return the number of elements along a given axis.

    Parameters
    ----------
    a : array_like
        Input data.
    axis : None or int or tuple of ints, optional
        Axis or axes along which the elements are counted.  By default, give
        the total number of elements.

        .

def sort(a, axis=-1, kind=None, order=None, *, stable=None):
    
    Return a sorted copy of an array.

    Parameters
    ----------
    a : array_like
        Array to be sorted.
    axis : int or None, optional
        Axis along which to sort. If None, the array is flattened before
        sorting. The default is -1, which sorts along the last axis.
    kind

def sort_complex(a):
    
    Sort a complex array using the real part first, then the imaginary part.

    Parameters
    ----------
    a : array_like
        Input array

    Returns
    -------
    out : complex ndarray
        Always returns a sorted complex array.

    Examples
    --------
    >>> import numpy as np


def spacing(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    spacing(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Return the distance between x and the nearest adjacent number.

Parameters
----------
x : array_like
    Values to find the spacing of.
out : ndarray, None, or tuple of ndarray and None, opti

def split(ary, indices_or_sections, axis=0):
    
    Split an array into multiple sub-arrays as views into `ary`.

    Parameters
    ----------
    ary : ndarray
        Array to be divided into sub-arrays.
    indices_or_sections : int or 1-D array
        If `indices_or_sections` is an integer, N, the array will be divided
        into N equal

def sqrt(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    sqrt(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Return the non-negative square-root of an array, element-wise.

Parameters
----------
x : array_like
    The values whose square-roots are required.
out : ndarray, None, or tuple of ndarray and 

def square(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    square(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Return the element-wise square of the input.

Parameters
----------
x : array_like
    Input data.
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which the res

def squeeze(a, axis=None):
    
    Remove axes of length one from `a`.

    Parameters
    ----------
    a : array_like
        Input data.
    axis : None or int or tuple of ints, optional
        Selects a subset of the entries of length one in the
        shape. If an axis is selected with shape entry greater than
        on

def stack(arrays, axis=0, out=None, *, dtype=None, casting='same_kind'):
    
    Join a sequence of arrays along a new axis.

    The ``axis`` parameter specifies the index of the new axis in the
    dimensions of the result. For example, if ``axis=0`` it will be the first
    dimension and if ``axis=-1`` it will be the last dimension.

    Parameters
    ----------
    arr

def std(a, axis=None, dtype=None, out=None, ddof=0, keepdims=<no value>, *, where=<no value>, mean=<no valu:
    
    Compute the standard deviation along the specified axis.

    Returns the standard deviation, a measure of the spread of a distribution,
    of the array elements. The standard deviation is computed for the
    flattened array by default, otherwise over the specified axis.

    Parameters
    -

def str_(value='', /, *args, **kwargs):
    A unicode string.

This type strips trailing null codepoints.

>>> s = np.str_("abc\x00")
>>> s
'abc'

Unlike the builtin :class:`str`, this supports the
:ref:`python:bufferobjects`, exposing its contents as UCS4:

>>> m = memoryview(np.str_("abc"))
>>> m.format
'3w'
>>> m.tobytes()
b'a\x00\x00\x00b

def subtract(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    subtract(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Subtract arguments, element-wise.

Parameters
----------
x1, x2 : array_like
    The arrays to be subtracted from each other.
    If ``x1.shape != x2.shape``, they must be broadcastable

def sum(a, axis=None, dtype=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>):
    
    Sum of array elements over a given axis.

    Parameters
    ----------
    a : array_like
        Elements to sum.
    axis : None or int or tuple of ints, optional
        Axis or axes along which a sum is performed.  The default,
        axis=None, will sum all of the elements of the input a

def swapaxes(a, axis1, axis2):
    
    Interchange two axes of an array.

    Parameters
    ----------
    a : array_like
        Input array.
    axis1 : int
        First axis.
    axis2 : int
        Second axis.

    Returns
    -------
    a_swapped : ndarray
        For NumPy >= 1.10.0, if `a` is an ndarray, then a view of `a

def take(a, indices, axis=None, out=None, mode='raise'):
    
    Take elements from an array along an axis.

    When axis is not None, this function does the same thing as "fancy"
    indexing (indexing arrays using arrays); however, it can be easier to use
    if you need elements along a given axis. A call such as
    ``np.take(arr, indices, axis=3)`` is 

def take_along_axis(arr, indices, axis=-1):
    
    Take values from the input array by matching 1d index and data slices.

    This iterates over matching 1d slices oriented along the specified axis in
    the index and data arrays, and uses the former to look up values in the
    latter. These slices can be different lengths.

    Functions re

def tan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    tan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Compute tangent element-wise.

Equivalent to ``np.sin(x)/np.cos(x)`` element-wise.

Parameters
----------
x : array_like
    Input array.
out : ndarray, None, or tuple of ndarray and None, option

def tanh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    tanh(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Compute hyperbolic tangent element-wise.

Equivalent to ``np.sinh(x)/np.cosh(x)`` or ``-1j * np.tan(1j*x)``.

Parameters
----------
x : array_like
    Input array.
out : ndarray, None, or tuple 

def tensordot(a, b, axes=2):
    
    Compute tensor dot product along specified axes.

    Given two tensors, `a` and `b`, and an array_like object containing
    two array_like objects, ``(a_axes, b_axes)``, sum the products of
    `a`'s and `b`'s elements (components) over the axes specified by
    ``a_axes`` and ``b_axes``. The

def test(label='fast', verbose=1, extra_argv=None, doctests=False, coverage=False, durations=-1, tests=None):
    
    Pytest test runner.

    A test function is typically added to a package's __init__.py like so::

      from numpy._pytesttester import PytestTester
      test = PytestTester(__name__).test
      del PytestTester

    Calling this test function finds and runs all tests associated with the
    m

def tile(A, reps):
    
    Construct an array by repeating A the number of times given by reps.

    If `reps` has length ``d``, the result will have dimension of
    ``max(d, A.ndim)``.

    If ``A.ndim < d``, `A` is promoted to be d-dimensional by prepending new
    axes. So a shape (3,) array is promoted to (1, 3) for

def timedelta64(value=0, /, *args):
    A timedelta stored as a 64-bit integer.

See :ref:`arrays.datetime` for more information.

:Character code: ``'m'``

def trace(a, offset=0, axis1=0, axis2=1, dtype=None, out=None):
    
    Return the sum along diagonals of the array.

    If `a` is 2-D, the sum along its diagonal with the given offset
    is returned, i.e., the sum of elements ``a[i,i+offset]`` for all i.

    If `a` has more than two dimensions, then the axes specified by axis1 and
    axis2 are used to determin

def transpose(a, axes=None):
    
    Returns an array with axes transposed.

    For a 1-D array, this returns an unchanged view of the original array, as a
    transposed vector is simply the same vector.
    To convert a 1-D array into a 2-D column vector, an additional dimension
    must be added, e.g., ``np.atleast_2d(a).T`` a

def trapezoid(y, x=None, dx=1.0, axis=-1):
    
    Integrate along the given axis using the composite trapezoidal rule.

    If `x` is provided, the integration happens in sequence along its
    elements - they are not sorted.

    Integrate `y` (`x`) along each 1d slice on the given axis, compute
    :math:`\int y(x) dx`.
    When `x` is speci

def tri(N, M=None, k=0, dtype=<class 'float'>, *, like=None):
    
    An array with ones at and below the given diagonal and zeros elsewhere.

    Parameters
    ----------
    N : int
        Number of rows in the array.
    M : int, optional
        Number of columns in the array.
        By default, `M` is taken equal to `N`.
    k : int, optional
        The 

def tril(m, k=0):
    
    Lower triangle of an array.

    Return a copy of an array with elements above the `k`-th diagonal zeroed.
    For arrays with ``ndim`` exceeding 2, `tril` will apply to the final two
    axes.

    Parameters
    ----------
    m : array_like, shape (..., M, N)
        Input array.
    k : int

def tril_indices(n, k=0, m=None):
    
    Return the indices for the lower-triangle of an (n, m) array.

    Parameters
    ----------
    n : int
        The row dimension of the arrays for which the returned
        indices will be valid.
    k : int, optional
        Diagonal offset (see `tril` for details).
    m : int, optional
  

def tril_indices_from(arr, k=0):
    
    Return the indices for the lower-triangle of arr.

    See `tril_indices` for full details.

    Parameters
    ----------
    arr : array_like
        The indices will be valid for square arrays whose dimensions are
        the same as arr.
    k : int, optional
        Diagonal offset (see `t

def trim_zeros(filt, trim='fb', axis=None):
    Remove values along a dimension which are zero along all other.

    Parameters
    ----------
    filt : array_like
        Input array.
    trim : {"fb", "f", "b"}, optional
        A string with 'f' representing trim from front and 'b' to trim from
        back. By default, zeros are trimmed on b

def triu(m, k=0):
    
    Upper triangle of an array.

    Return a copy of an array with the elements below the `k`-th diagonal
    zeroed. For arrays with ``ndim`` exceeding 2, `triu` will apply to the
    final two axes.

    Please refer to the documentation for `tril` for further details.

    See Also
    --------

def triu_indices(n, k=0, m=None):
    
    Return the indices for the upper-triangle of an (n, m) array.

    Parameters
    ----------
    n : int
        The size of the arrays for which the returned indices will
        be valid.
    k : int, optional
        Diagonal offset (see `triu` for details).
    m : int, optional
        The

def triu_indices_from(arr, k=0):
    
    Return the indices for the upper-triangle of arr.

    See `triu_indices` for full details.

    Parameters
    ----------
    arr : ndarray, shape(N, N)
        The indices will be valid for square arrays.
    k : int, optional
        Diagonal offset (see `triu` for details).

    Returns
   

def true_divide(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signatu:
    divide(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Divide arguments element-wise.

Parameters
----------
x1 : array_like
    Dividend array.
x2 : array_like
    Divisor array.
    If ``x1.shape != x2.shape``, they must be broadcastable to

def trunc(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=No:
    trunc(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])

Return the truncated value of the input, element-wise.

The truncated value of the scalar `x` is the nearest integer `i` which
is closer to zero than `x` is. In short, the fractional part of th

def typename(char):
    
    Return a description for the given data type code.

    Parameters
    ----------
    char : str
        Data type code.

    Returns
    -------
    out : str
        Description of the input data type code.

    See Also
    --------
    dtype

    Examples
    --------
    >>> import numpy a

def ubyte(value=0, /):
    Unsigned integer type, compatible with C ``unsigned char``.

:Character code: ``'B'``
:Canonical name: `numpy.ubyte`
:Alias on this platform (Linux x86_64): `numpy.uint8`: 8-bit unsigned integer (``0`` to ``255``).

def ufunc():
    Functions that operate element by element on whole arrays.

To see the documentation for a specific ufunc, use `info`.  For
example, ``np.info(np.sin)``.  Because ufuncs are written in C
(for speed) and linked into Python with NumPy's ufunc facility,
Python's help() function finds this page whenever

def uint(value=0, /):
    Unsigned signed integer type, 64bit on 64bit systems and 32bit on 32bit systems.

:Character code: ``'L'``
:Canonical name: `numpy.uint`
:Alias on this platform (Linux x86_64): `numpy.uint64`: 64-bit unsigned integer (``0`` to ``18_446_744_073_709_551_615``).
:Alias on this platform (Linux x86_64): 

def uint16(value=0, /):
    Unsigned integer type, compatible with C ``unsigned short``.

:Character code: ``'H'``
:Canonical name: `numpy.ushort`
:Alias on this platform (Linux x86_64): `numpy.uint16`: 16-bit unsigned integer (``0`` to ``65_535``).

def uint32(value=0, /):
    Unsigned integer type, compatible with C ``unsigned int``.

:Character code: ``'I'``
:Canonical name: `numpy.uintc`
:Alias on this platform (Linux x86_64): `numpy.uint32`: 32-bit unsigned integer (``0`` to ``4_294_967_295``).

def uint64(value=0, /):
    Unsigned signed integer type, 64bit on 64bit systems and 32bit on 32bit systems.

:Character code: ``'L'``
:Canonical name: `numpy.uint`
:Alias on this platform (Linux x86_64): `numpy.uint64`: 64-bit unsigned integer (``0`` to ``18_446_744_073_709_551_615``).
:Alias on this platform (Linux x86_64): 

def uint8(value=0, /):
    Unsigned integer type, compatible with C ``unsigned char``.

:Character code: ``'B'``
:Canonical name: `numpy.ubyte`
:Alias on this platform (Linux x86_64): `numpy.uint8`: 8-bit unsigned integer (``0`` to ``255``).

def uintc(value=0, /):
    Unsigned integer type, compatible with C ``unsigned int``.

:Character code: ``'I'``
:Canonical name: `numpy.uintc`
:Alias on this platform (Linux x86_64): `numpy.uint32`: 32-bit unsigned integer (``0`` to ``4_294_967_295``).

def uintp(value=0, /):
    Unsigned signed integer type, 64bit on 64bit systems and 32bit on 32bit systems.

:Character code: ``'L'``
:Canonical name: `numpy.uint`
:Alias on this platform (Linux x86_64): `numpy.uint64`: 64-bit unsigned integer (``0`` to ``18_446_744_073_709_551_615``).
:Alias on this platform (Linux x86_64): 

def ulong(value=0, /):
    Unsigned signed integer type, 64bit on 64bit systems and 32bit on 32bit systems.

:Character code: ``'L'``
:Canonical name: `numpy.uint`
:Alias on this platform (Linux x86_64): `numpy.uint64`: 64-bit unsigned integer (``0`` to ``18_446_744_073_709_551_615``).
:Alias on this platform (Linux x86_64): 

def ulonglong(value=0, /):
    Unsigned integer type, compatible with C ``unsigned long long``.

:Character code: ``'Q'``

def union1d(ar1, ar2):
    
    Find the union of two arrays.

    Return the unique, sorted array of values that are in either of the two
    input arrays.

    Parameters
    ----------
    ar1, ar2 : array_like
        Input arrays. They are flattened if they are not already 1D.

    Returns
    -------
    union1d : ndarr

def unique(ar, return_index=False, return_inverse=False, return_counts=False, axis=None, *, equal_nan=True, so:
    
    Find the unique elements of an array.

    Returns the sorted unique elements of an array. There are three optional
    outputs in addition to the unique elements:

    * the indices of the input array that give the unique values
    * the indices of the unique array that reconstruct the input 

def unique_all(x):
    
    Find the unique elements of an array, and counts, inverse, and indices.

    This function is an Array API compatible alternative to::

        np.unique(x, return_index=True, return_inverse=True,
                  return_counts=True, equal_nan=False, sorted=False)

    but returns a namedtuple

def unique_counts(x):
    
    Find the unique elements and counts of an input array `x`.

    This function is an Array API compatible alternative to::

        np.unique(x, return_counts=True, equal_nan=False, sorted=False)

    but returns a namedtuple for easier access to each output.

    .. note::
        This function

def unique_inverse(x):
    
    Find the unique elements of `x` and indices to reconstruct `x`.

    This function is an Array API compatible alternative to::

        np.unique(x, return_inverse=True, equal_nan=False, sorted=False)

    but returns a namedtuple for easier access to each output.

    .. note::
        This fu

def unique_values(x):
    
    Returns the unique elements of an input array `x`.

    This function is an Array API compatible alternative to::

        np.unique(x, equal_nan=False, sorted=False)

    .. versionchanged:: 2.3
       The algorithm was changed to a faster one that does not rely on
       sorting, and hence th

def unpackbits(a, /, axis=None, count=None, bitorder='big'):
    unpackbits(a, /, axis=None, count=None, bitorder='big')

Unpacks elements of a uint8 array into a binary-valued output array.

Each element of `a` represents a bit-field that should be unpacked
into a binary-valued output array. The shape of the output array is
either 1-D (if `axis` is ``None``) or 

def unravel_index(indices, shape, order='C'):
    unravel_index(indices, shape, order='C')

Converts a flat index or array of flat indices into a tuple
of coordinate arrays.

Parameters
----------
indices : array_like
    An integer array whose elements are indices into the flattened
    version of an array of dimensions ``shape``. Before version 1

def unsignedinteger():
    Abstract base class of all unsigned integer scalar types.

def unstack(x, /, *, axis=0):
    
    Split an array into a sequence of arrays along the given axis.

    The ``axis`` parameter specifies the dimension along which the array will
    be split. For example, if ``axis=0`` (the default) it will be the first
    dimension and if ``axis=-1`` it will be the last dimension.

    The resu

def unwrap(p, discont=None, axis=-1, *, period=6.283185307179586):
    
    Unwrap by taking the complement of large deltas with respect to the period.

    This unwraps a signal `p` by changing elements which have an absolute
    difference from their predecessor of more than ``max(discont, period/2)``
    to their `period`-complementary values.

    For the default c

def ushort(value=0, /):
    Unsigned integer type, compatible with C ``unsigned short``.

:Character code: ``'H'``
:Canonical name: `numpy.ushort`
:Alias on this platform (Linux x86_64): `numpy.uint16`: 16-bit unsigned integer (``0`` to ``65_535``).

def vander(x, N=None, increasing=False):
    
    Generate a Vandermonde matrix.

    The columns of the output matrix are powers of the input vector. The
    order of the powers is determined by the `increasing` boolean argument.
    Specifically, when `increasing` is False, the `i`-th output column is
    the input vector raised element-wise

def var(a, axis=None, dtype=None, out=None, ddof=0, keepdims=<no value>, *, where=<no value>, mean=<no valu:
    
    Compute the variance along the specified axis.

    Returns the variance of the array elements, a measure of the spread of a
    distribution.  The variance is computed for the flattened array by
    default, otherwise over the specified axis.

    Parameters
    ----------
    a : array_like
 

def vdot(a, b, /):
    vdot(a, b, /)

Return the dot product of two vectors.

The `vdot` function handles complex numbers differently than `dot`:
if the first argument is complex, it is replaced by its complex conjugate
in the dot product calculation. `vdot` also handles multidimensional
arrays differently than `dot`: it 

def vecdot(x1, x2, /, out=None, *, axes=<no value>, axis=<no value>, keepdims=False, casting='same_kind', orde:
    vecdot(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])

Vector dot product of two arrays.

Let :math:`\mathbf{a}` be a vector in `x1` and :math:`\mathbf{b}` be
a corresponding vector in `x2`. The dot product is defined as:

.. math::
   \mathb

def vecmat(x1, x2, /, out=None, *, axes=<no value>, axis=<no value>, keepdims=False, casting='same_kind', orde:
    vecmat(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, axes, axis])

Vector-matrix dot product of two arrays.

Given a vector (or stack of vector) :math:`\mathbf{v}` in ``x1`` and
a matrix (or stack of matrices) :math:`\mathbf{A}` in ``x2``, the
vector-mat

def vectorize(pyfunc=<no value>, otypes=None, doc=None, excluded=None, cache=False, signature=None):
    
    vectorize(pyfunc=np._NoValue, otypes=None, doc=None, excluded=None,
    cache=False, signature=None)

    Returns an object that acts like pyfunc, but takes arrays as input.

    Define a vectorized function which takes a nested sequence of objects or
    numpy arrays as inputs and returns a si

def void(length_or_data, /, dtype=None):
    np.void(length_or_data, /, dtype=None)

Create a new structured or unstructured void scalar.

Parameters
----------
length_or_data : int, array-like, bytes-like, object
    One of multiple meanings (see notes).  The length or
    bytes data of an unstructured void.  Or alternatively,
    the data to

def vsplit(ary, indices_or_sections):
    
    Split an array into multiple sub-arrays vertically (row-wise).

    Please refer to the ``split`` documentation.  ``vsplit`` is equivalent
    to ``split`` with `axis=0` (default), the array is always split along the
    first axis regardless of the array dimension.

    See Also
    --------
 

def vstack(tup, *, dtype=None, casting='same_kind'):
    
    Stack arrays in sequence vertically (row wise).

    This is equivalent to concatenation along the first axis after 1-D arrays
    of shape `(N,)` have been reshaped to `(1,N)`. Rebuilds arrays divided by
    `vsplit`.

    This function makes most sense for arrays with up to 3 dimensions. For


def where(condition, x=None, y=None, /):
    where(condition, [x, y], /)

Return elements chosen from `x` or `y` depending on `condition`.

.. note::
    When only `condition` is provided, this function is a shorthand for
    ``np.asarray(condition).nonzero()``. Using `nonzero` directly should be
    preferred, as it behaves correctly for subc

def zeros(shape, dtype=None, order='C', *, device=None, like=None):
    zeros(shape, dtype=None, order='C', *, device=None, like=None)

Return a new array of given shape and type, filled with zeros.

Parameters
----------
shape : int or tuple of ints
    Shape of the new array, e.g., ``(2, 3)`` or ``2``.
dtype : data-type, optional
    The desired data-type for the arra

def zeros_like(a, dtype=None, order='K', subok=True, shape=None, *, device=None):
    
    Return an array of zeros with the same shape and type as a given array.

    Parameters
    ----------
    a : array_like
        The shape and data-type of `a` define these same attributes of
        the returned array.
    dtype : data-type, optional
        Overrides the data type of the res


SOURCE:
"""
NumPy
=====

Provides
  1. An array object of arbitrary homogeneous items
  2. Fast mathematical operations over arrays
  3. Linear Algebra, Fourier Transforms, Random Number Generation

How to use the documentation
----------------------------
Documentation is available in two forms: docstrings provided
with the code, and a loose standing reference guide, available from
`the NumPy homepage <https://numpy.org>`_.

We recommend exploring the docstrings using
`IPython <https://ipython.org>`_, an advanced Python shell with
TAB-completion and introspection capabilities.  See below for further
instructions.

The docstring examples assume that `numpy` has been imported as ``np``::

  >>> import numpy as np

Code snippets are indicated by three greater-than signs::

  >>> x = 42
  >>> x = x + 1

Use the built-in ``help`` function to view a function's docstring::

  >>> help(np.sort)
  ... # doctest: +SKIP

For some objects, ``np.info(obj)`` may provide additional help.  This is
particularly true if you see the line "Help on ufunc object:" at the top
of the help() page.  Ufuncs are implemented in C, not Python, for speed.
The native Python help() does not know how to view their help, but our
np.info() function does.

Available subpackages
---------------------
lib
    Basic functions used by several sub-packages.
random
    Core Random Tools
linalg
    Core Linear Algebra Tools
fft
    Core FFT routines
polynomial
    Polynomial tools
testing
    NumPy testing tools
distutils
    Enhancements to distutils with support for
    Fortran compilers support and more (for Python <= 3.11)

Utilities
---------
test
    Run numpy unittests
show_config
    Show numpy build configuration
__version__
    NumPy version string

Viewing documentation using IPython
-----------------------------------

Start IPython and import `numpy` usually under the alias ``np``: `import
numpy as np`.  Then, directly past or use the ``%cpaste`` magic to paste
examples into the shell.  To see which functions are available in `numpy`,
type ``np.<TAB>`` (where ``<TAB>`` refers to the TAB key), or use
``np.*cos*?<ENTER>`` (where ``<ENTER>`` refers to the ENTER key) to narrow
down the list.  To view the docstring for a function, use
``np.cos?<ENTER>`` (to view the docstring) and ``np.cos??<ENTER>`` (to view
the source code).

Copies vs. in-place operation
-----------------------------
Most of the functions in `numpy` return a copy of the array argument
(e.g., `np.sort`).  In-place versions of these functions are often
available as array methods, i.e. ``x = np.array([1,2,3]); x.sort()``.
Exceptions to this rule are documented.

"""
import os
import sys
import warnings

# If a version with git hash was stored, use that instead
from . import version
from ._expired_attrs_2_0 import __expired_attributes__
from ._globals import _CopyMode, _NoValue
from .version import __version__

# We first need to detect if we're being called as part of the numpy setup
# procedure itself in a reliable manner.
try:
    __NUMPY_SETUP__  # noqa: B018
except NameError:
    __NUMPY_SETUP__ = False

if __NUMPY_SETUP__:
    sys.stderr.write('Running from numpy source directory.\n')
else:
    # Allow distributors to run custom init code before importing numpy._core
    from . import _distributor_init

    try:
        from numpy.__config__ import show_config
    except ImportError as e:
        if isinstance(e, ModuleNotFoundError) and e.name == "numpy.__config__":
            # The __config__ module itself was not found, so add this info:
            msg = """Error importing numpy: you should not try to import numpy from
            its source directory; please exit the numpy source tree, and relaunch
            your python interpreter from there."""
            raise ImportError(msg) from e
        raise

    from . import _core
    from ._core import (
        False_,
        ScalarType,
        True_,
        abs,
        absolute,
        acos,
        acosh,
        add,
        all,
        allclose,
        amax,
        amin,
        any,
        arange,
        arccos,
        arccosh,
        arcsin,
        arcsinh,
        arctan,
        arctan2,
        arctanh,
        argmax,
        argmin,
        argpartition,
        argsort,
        argwhere,
        around,
        array,
        array2string,
        array_equal,
        array_equiv,
        array_repr,
        array_str,
        asanyarray,
        asarray,
        ascontiguousarray,
        asfortranarray,
        asin,
        asinh,
        astype,
        atan,
        atan2,
        atanh,
        atleast_1d,
        atleast_2d,
        atleast_3d,
        base_repr,
        binary_repr,
        bitwise_and,
        bitwise_count,
        bitwise_invert,
        bitwise_left_shift,
        bitwise_not,
        bitwise_or,
        bitwise_right_shift,
        bitwise_xor,
        block,
        bool,
        bool_,
        broadcast,
        busday_count,
        busday_offset,
        busdaycalendar,
        byte,
        bytes_,
        can_cast,
        cbrt,
        cdouble,
        ceil,
        character,
        choose,
        clip,
        clongdouble,
        complex64,
        complex128,
        complexfloating,
        compress,
        concat,
        concatenate,
        conj,
        conjugate,
        convolve,
        copysign,
        copyto,
        correlate,
        cos,
        cosh,
        count_nonzero,
        cross,
        csingle,
        cumprod,
        cumsum,
        cumulative_prod,
        cumulative_sum,
        datetime64,
        datetime_as_string,
        datetime_data,
        deg2rad,
        degrees,
        diagonal,
        divide,
        divmod,
        dot,
        double,
        dtype,
        e,
        einsum,
        einsum_path,
        empty,
        empty_like,
        equal,
        errstate,
        euler_gamma,
        exp,
        exp2,
        expm1,
        fabs,
        finfo,
        flatiter,
        flatnonzero,
        flexible,
        float16,
        float32,
        float64,
        float_power,
        floating,
        floor,
        floor_divide,
        fmax,
        fmin,
        fmod,
        format_float_positional,
        format_float_scientific,
        frexp,
        from_dlpack,
        frombuffer,
        fromfile,
        fromfunction,
        fromiter,
        frompyfunc,
        fromstring,
        full,
        full_like,
        gcd,
        generic,
        geomspace,
        get_printoptions,
        getbufsize,
        geterr,
        geterrcall,
        greater,
        greater_equal,
        half,
        heaviside,
        hstack,
        hypot,
        identity,
        iinfo,
        indices,
        inexact,
        inf,
        inner,
        int8,
        int16,
        int32,
        int64,
        int_,
        intc,
        integer,
        intp,
        invert,
        is_busday,
        isclose,
        isdtype,
        isfinite,
        isfortran,
        isinf,
        isnan,
        isnat,
        isscalar,
        issubdtype,
        lcm,
        ldexp,
        left_shift,
        less,
        less_equal,
        lexsort,
        linspace,
        little_endian,
        log,
        log1p,
        log2,
        log10,
        logaddexp,
        logaddexp2,
        logical_and,
        logical_not,
        logical_or,
        logical_xor,
        logspace,
        long,
        longdouble,
        longlong,
        matmul,
        matrix_transpose,
        matvec,
        max,
        maximum,
        may_share_memory,
        mean,
        memmap,
        min,
        min_scalar_type,
        minimum,
        mod,
        modf,
        moveaxis,
        multiply,
        nan,
        ndarray,
        ndim,
        nditer,
        negative,
        nested_iters,
        newaxis,
        nextafter,
        nonzero,
        not_equal,
        number,
        object_,
        ones,
        ones_like,
        outer,
        partition
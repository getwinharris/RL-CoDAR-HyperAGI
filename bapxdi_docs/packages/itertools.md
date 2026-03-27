PACKAGE: itertools
MODULE:  itertools
VERSION: stdlib

DESCRIPTION:
Functional tools for creating and using iterators.

Infinite iterators:
count(start=0, step=1) --> start, start+step, start+2*step, ...
cycle(p) --> p0, p1, ... plast, p0, p1, ...
repeat(elem [,n]) --> elem, elem, elem, ... endlessly or up to n times

Iterators terminating on the shortest input sequence:
accumulate(p[, func]) --> p0, p0+p1, p0+p1+p2
batched(p, n) --> [p0, p1, ..., p_n-1], [p_n, p_n+1, ..., p_2n-1], ...
chain(p, q, ...) --> p0, p1, ... plast, q0, q1, ...
chain.from_iterable([p, q, ...]) --> p0, p1, ... plast, q0, q1, ...
compress(data, selectors) --> (d[0] if s[0]), (d[1] if s[1]), ...
dropwhile(predicate, seq) --> seq[n], seq[n+1], starting when predicate fails
groupby(iterable[, keyfunc]) --> sub-iterators grouped by value of keyfunc(v)
filterfalse(predicate, seq) --> elements of seq where predicate(elem) is False
islice(seq, [start,] stop [, step]) --> elements from
       seq[start:stop:step]
pairwise(s) --> (s[0],s[1]), (s[1],s[2]), (s[2], s[3]), ...
starmap(fun, s

PUBLIC API:

def accumulate(iterable, func=None, *, initial=None):
    Return series of accumulated sums (or other binary function results).

def batched(iterable, n):
    Batch data into tuples of length n. The last batch may be shorter than n.

Loops over the input iterable and accumulates data into tuples
up to size n.  The input is consumed lazily, just enough to
fill a batch.  The result is yielded as soon as a batch is full
or when the input iterable is exhauste

def chain:
    chain(*iterables) --> chain object

Return a chain object whose .__next__() method returns elements from the
first iterable until it is exhausted, then elements from the next
iterable, until all of the iterables are exhausted.

def combinations(iterable, r):
    Return successive r-length combinations of elements in the iterable.

combinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)

def combinations_with_replacement(iterable, r):
    Return successive r-length combinations of elements in the iterable allowing individual elements to have successive repeats.

combinations_with_replacement('ABC', 2) --> ('A','A'), ('A','B'), ('A','C'), ('B','B'), ('B','C'), ('C','C')

def compress(data, selectors):
    Return data elements corresponding to true selector elements.

Forms a shorter iterator from selected data elements using the selectors to
choose the data elements.

def count(start=0, step=1):
    Return a count object whose .__next__() method returns consecutive values.

Equivalent to:
    def count(firstval=0, step=1):
        x = firstval
        while 1:
            yield x
            x += step

def cycle(iterable, /):
    Return elements from the iterable until it is exhausted. Then repeat the sequence indefinitely.

def dropwhile(predicate, iterable, /):
    Drop items from the iterable while predicate(item) is true.

Afterwards, return every element until the iterable is exhausted.

def filterfalse(function, iterable, /):
    Return those items of iterable for which function(item) is false.

If function is None, return the items that are false.

def groupby(iterable, key=None):
    make an iterator that returns consecutive keys and groups from the iterable

  iterable
    Elements to divide into groups according to the key function.
  key
    A function for computing the group category for each element.
    If the key function is not specified or is None, the element itself
  

def islice:
    islice(iterable, stop) --> islice object
islice(iterable, start, stop[, step]) --> islice object

Return an iterator whose next() method returns selected values from an
iterable.  If start is specified, will skip all preceding elements;
otherwise, start defaults to zero.  Step defaults to one.  If
s

def pairwise(iterable, /):
    Return an iterator of overlapping pairs taken from the input iterator.

    s -> (s0,s1), (s1,s2), (s2, s3), ...

def permutations(iterable, r=None):
    Return successive r-length permutations of elements in the iterable.

permutations(range(3), 2) --> (0,1), (0,2), (1,0), (1,2), (2,0), (2,1)

def product:
    product(*iterables, repeat=1) --> product object

Cartesian product of input iterables.  Equivalent to nested for-loops.

For example, product(A, B) returns the same as:  ((x,y) for x in A for y in B).
The leftmost iterators are in the outermost for-loop, so the output tuples
cycle in a manner simil

def repeat:
    repeat(object [,times]) -> create an iterator which returns the object
for the specified number of times.  If not specified, returns the object
endlessly.

def starmap(function, iterable, /):
    Return an iterator whose values are returned from the function evaluated with an argument tuple taken from the given sequence.

def takewhile(predicate, iterable, /):
    Return successive entries from an iterable as long as the predicate evaluates to true for each entry.

def tee(iterable, n=2, /):
    Returns a tuple of n independent iterators.

def zip_longest:
    zip_longest(iter1 [,iter2 [...]], [fillvalue=None]) --> zip_longest object

Return a zip_longest object whose .__next__() method returns a tuple where
the i-th element comes from the i-th iterable argument.  The .__next__()
method continues until the longest iterable in the argument sequence
is exha
PACKAGE: asyncio
MODULE:  asyncio
VERSION: stdlib

DESCRIPTION:
The asyncio package, tracking PEP 3156.

PUBLIC API:

def AbstractChildWatcher():
    Abstract base class for monitoring child processes.

    Objects derived from this class monitor a collection of subprocesses and
    report their termination or interruption by a signal.

    New callbacks are registered with .add_child_handler(). Starting a new
    process must be done within a 'w

def AbstractEventLoop():
    Abstract event loop.

def AbstractEventLoopPolicy():
    Abstract policy for accessing the event loop.

def AbstractServer():
    Abstract server returned by create_server().

def Barrier(parties):
    Asyncio equivalent to threading.Barrier

    Implements a Barrier primitive.
    Useful for synchronizing a fixed number of tasks at known synchronization
    points. Tasks block on 'wait()' and are simultaneously awoken once they
    have all made their call.
    

def BaseProtocol():
    Common base class for protocol interfaces.

    Usually user implements protocols that derived from BaseProtocol
    like Protocol or ProcessProtocol.

    The only case when BaseProtocol should be implemented directly is
    write-only transport like write pipe
    

def BaseTransport(extra=None):
    Base class for transports.

def BoundedSemaphore(value=1):
    A bounded semaphore implementation.

    This raises ValueError in release() if it would increase the value
    above the initial value.
    

def BrokenBarrierError:
    Barrier is broken by barrier.abort() call.

def BufferedProtocol():
    Interface for stream protocol with manual buffer control.

    Event methods, such as `create_server` and `create_connection`,
    accept factories that return protocols that implement this interface.

    The idea of BufferedProtocol is that it allows to manually allocate
    and control the receiv

def CancelledError:
    The Future or Task was cancelled.

def Condition(lock=None):
    Asynchronous equivalent to threading.Condition.

    This class implements condition variable objects. A condition variable
    allows one or more coroutines to wait until they are notified by another
    coroutine.

    A new Lock object is created and used as the underlying lock.
    

def DatagramProtocol():
    Interface for datagram protocol.

def DatagramTransport(extra=None):
    Interface for datagram (UDP) transports.

def DefaultEventLoopPolicy():
    UNIX event loop policy with a watcher for child processes.

def Event():
    Asynchronous equivalent to threading.Event.

    Class implementing event objects. An event manages a flag that can be set
    to true with the set() method and reset to false with the clear() method.
    The wait() method blocks until the flag is true. The flag is initially
    false.
    

def FastChildWatcher():
    'Fast' child watcher implementation.

    This implementation reaps every terminated processes by calling
    os.waitpid(-1) directly, possibly breaking other code spawning processes
    and waiting for their termination.

    There is no noticeable overhead when handling a big number of children
  

def Future(*, loop=None):
    This class is *almost* compatible with concurrent.futures.Future.

    Differences:

    - result() and exception() do not take a timeout argument and
      raise an exception when the future isn't done yet.

    - Callbacks registered with add_done_callback() are always called
      via the event l

def Handle(callback, args, loop, context=None):
    Object returned by callback registration methods.

def IncompleteReadError(partial, expected):
    
    Incomplete read error. Attributes:

    - partial: read bytes string before the end of stream was reached
    - expected: total number of expected bytes (or None if unknown)
    

def InvalidStateError:
    The operation is not allowed in this state.

def LifoQueue(maxsize=0):
    A subclass of Queue that retrieves most recently added entries first.

def LimitOverrunError(message, consumed):
    Reached the buffer limit while looking for a separator.

    Attributes:
    - consumed: total number of to be consumed bytes.
    

def Lock():
    Primitive lock objects.

    A primitive lock is a synchronization primitive that is not owned
    by a particular coroutine when locked.  A primitive lock is in one
    of two states, 'locked' or 'unlocked'.

    It is created in the unlocked state.  It has two basic methods,
    acquire() and rele

def MultiLoopChildWatcher():
    A watcher that doesn't require running loop in the main thread.

    This implementation registers a SIGCHLD signal handler on
    instantiation (which may conflict with other code that
    install own handler for this signal).

    The solution is safe but it has a significant overhead when
    han

def PidfdChildWatcher():
    Child watcher implementation using Linux's pid file descriptors.

    This child watcher polls process file descriptors (pidfds) to await child
    process termination. In some respects, PidfdChildWatcher is a "Goldilocks"
    child watcher implementation. It doesn't require signals or threads, does

def PriorityQueue(maxsize=0):
    A subclass of Queue; retrieves entries in priority order (lowest first).

    Entries are typically tuples of the form: (priority number, data).
    

def Protocol():
    Interface for stream protocol.

    The user should implement this interface.  They can inherit from
    this class but don't need to.  The implementations here do
    nothing (they don't raise exceptions).

    When the user wants to requests a transport, they pass a protocol
    factory to a utili

def Queue(maxsize=0):
    A queue, useful for coordinating producer and consumer coroutines.

    If maxsize is less than or equal to zero, the queue size is infinite. If it
    is an integer greater than 0, then "await put()" will block when the
    queue reaches maxsize, until an item is removed by get().

    Unlike the s

def QueueEmpty:
    Raised when Queue.get_nowait() is called on an empty Queue.

def QueueFull:
    Raised when the Queue.put_nowait() method is called on a full Queue.

def ReadTransport(extra=None):
    Interface for read-only transports.

def Runner(*, debug=None, loop_factory=None):
    A context manager that controls event loop life cycle.

    The context manager always creates a new event loop,
    allows to run async functions inside it,
    and properly finalizes the loop at the context manager exit.

    If debug is True, the event loop will be run in debug mode.
    If loop_

def SafeChildWatcher():
    'Safe' child watcher implementation.

    This implementation avoids disrupting other code spawning processes by
    polling explicitly each process in the SIGCHLD handler instead of calling
    os.waitpid(-1).

    This is a safe solution but it has a significant overhead when handling a
    big nu

def SelectorEventLoop(selector=None):
    Unix event loop.

    Adds signal handling and UNIX Domain Socket support to SelectorEventLoop.
    

def Semaphore(value=1):
    A Semaphore implementation.

    A semaphore manages an internal counter which is decremented by each
    acquire() call and incremented by each release() call. The counter
    can never go below zero; when acquire() finds that it is zero, it blocks,
    waiting until some other thread calls release

def SendfileNotAvailableError:
    Sendfile syscall is not available.

    Raised if OS does not support sendfile syscall for given socket or
    file type.
    

def StreamReaderProtocol(stream_reader, client_connected_cb=None, loop=None):
    Helper class to adapt between Protocol and StreamReader.

    (This is a helper class instead of making StreamReader itself a
    Protocol subclass, because the StreamReader has other potential
    uses, and to prevent the user of the StreamReader to accidentally
    call inappropriate methods of th

def StreamWriter(transport, protocol, reader, loop):
    Wraps a Transport.

    This exposes write(), writelines(), [can_]write_eof(),
    get_extra_info() and close().  It adds drain() which returns an
    optional Future on which you can wait for flow control.  It also
    adds a transport property which references the Transport
    directly.
    

def SubprocessProtocol():
    Interface for protocol for subprocess calls.

def Task(coro, *, loop=None, name=None, context=None, eager_start=False):
    A coroutine wrapped in a Future.

def TaskGroup():
    Asynchronous context manager for managing groups of tasks.

    Example use:

        async with asyncio.TaskGroup() as group:
            task1 = group.create_task(some_coroutine(...))
            task2 = group.create_task(other_coroutine(...))
        print("Both tasks have completed now.")

    A

def ThreadedChildWatcher():
    Threaded child watcher implementation.

    The watcher uses a thread per process
    for waiting for the process finish.

    It doesn't require subscription on POSIX signal
    but a thread creation is not free.

    The watcher has O(1) complexity, its performance doesn't depend
    on amount of 

def Timeout(when: Optional[float]) -> None:
    Asynchronous context manager for cancelling overdue coroutines.

    Use `timeout()` or `timeout_at()` rather than instantiating this class directly.
    

def TimeoutError:
    Timeout expired.

def TimerHandle(when, callback, args, loop, context=None):
    Object returned by timed callback registration methods.

def Transport(extra=None):
    Interface representing a bidirectional transport.

    There may be several implementations, but typically, the user does
    not implement new transports; rather, the platform provides some
    useful transports that are implemented using the platform's best
    practices.

    The user never insta

def WriteTransport(extra=None):
    Interface for write-only transports.

def all_tasks(loop=None):
    Return a set of all tasks for the loop.

def as_completed(fs, *, timeout=None):
    Return an iterator whose values are coroutines.

    When waiting for the yielded coroutines you'll get the results (or
    exceptions!) of the original Futures (or coroutines), in the order
    in which and as soon as they complete.

    This differs from PEP 3148; the proper way to use this is:

 

def create_eager_task_factory(custom_task_constructor):
    Create a function suitable for use as a task factory on an event-loop.

        Example usage:

            loop.set_task_factory(
                asyncio.create_eager_task_factory(my_task_constructor))

        Now, tasks created will be started immediately (rather than being first
        schedule

def create_task(coro, *, name=None, context=None):
    Schedule the execution of a coroutine object in a spawn task.

    Return a Task object.
    

def current_task(loop=None):
    Return a currently executed task.

def ensure_future(coro_or_future, *, loop=None):
    Wrap a coroutine or an awaitable in a future.

    If the argument is a Future, it is returned directly.
    

def gather(*coros_or_futures, return_exceptions=False):
    Return a future aggregating results from the given coroutines/futures.

    Coroutines will be wrapped in a future and scheduled in the event
    loop. They will not necessarily be scheduled in the same order as
    passed in.

    All futures must share the same event loop.  If all the tasks are
  

def get_child_watcher():
    Equivalent to calling get_event_loop_policy().get_child_watcher().

def get_event_loop():
    Return an asyncio event loop.

When called from a coroutine or a callback (e.g. scheduled with
call_soon or similar API), this function will always return the
running event loop.

If there is no running event loop set, the function will return
the result of `get_event_loop_policy().get_event_loop()`

def get_event_loop_policy():
    Get the current event loop policy.

def get_running_loop():
    Return the running event loop.  Raise a RuntimeError if there is none.

This function is thread-specific.

def iscoroutine(obj):
    Return True if obj is a coroutine object.

def iscoroutinefunction(func):
    Return True if func is a decorated coroutine function.

def isfuture(obj):
    Check for a Future.

    This returns True when obj is a Future instance or is advertising
    itself as duck-type compatible by setting _asyncio_future_blocking.
    See comment in Future for more details.
    

def new_event_loop():
    Equivalent to calling get_event_loop_policy().new_event_loop().

def open_connection(host=None, port=None, *, limit=65536, **kwds):
    A wrapper for create_connection() returning a (reader, writer) pair.

    The reader returned is a StreamReader instance; the writer is a
    StreamWriter instance.

    The arguments are all the usual arguments to create_connection()
    except protocol_factory; most common are positional host and 

def open_unix_connection(path=None, *, limit=65536, **kwds):
    Similar to `open_connection` but works with UNIX Domain Sockets.

def run(main, *, debug=None, loop_factory=None):
    Execute the coroutine and return the result.

    This function runs the passed coroutine, taking care of
    managing the asyncio event loop, finalizing asynchronous
    generators and closing the default executor.

    This function cannot be called when another asyncio event loop is
    running i

def run_coroutine_threadsafe(coro, loop):
    Submit a coroutine object to a given event loop.

    Return a concurrent.futures.Future to access the result.
    

def set_child_watcher(watcher):
    Equivalent to calling
    get_event_loop_policy().set_child_watcher(watcher).

def set_event_loop(loop):
    Equivalent to calling get_event_loop_policy().set_event_loop(loop).

def set_event_loop_policy(policy):
    Set the current event loop policy.

    If policy is None, the default policy is restored.

def shield(arg):
    Wait for a future, shielding it from cancellation.

    The statement

        task = asyncio.create_task(something())
        res = await shield(task)

    is exactly equivalent to the statement

        res = await something()

    *except* that if the coroutine containing it is cancelled, the
   

def sleep(delay, result=None):
    Coroutine that completes after a given time (in seconds).

def start_server(client_connected_cb, host=None, port=None, *, limit=65536, **kwds):
    Start a socket server, call back for each client connected.

    The first parameter, `client_connected_cb`, takes two parameters:
    client_reader, client_writer.  client_reader is a StreamReader
    object, while client_writer is a StreamWriter object.  This
    parameter can either be a plain ca

def start_unix_server(client_connected_cb, path=None, *, limit=65536, **kwds):
    Similar to `start_server` but works with UNIX Domain Sockets.

def timeout(delay: Optional[float]) -> asyncio.timeouts.Timeout:
    Timeout async context manager.

    Useful in cases when you want to apply timeout logic around block
    of code or in cases when asyncio.wait_for is not suitable. For example:

    >>> async with asyncio.timeout(10):  # 10 seconds timeout
    ...     await long_running_task()


    delay - value i

def timeout_at(when: Optional[float]) -> asyncio.timeouts.Timeout:
    Schedule the timeout at absolute time.

    Like timeout() but argument gives absolute time in the same clock system
    as loop.time().

    Please note: it is not POSIX time but a time with
    undefined starting base, e.g. the time of the system power on.

    >>> async with asyncio.timeout_at(lo

def to_thread(func, /, *args, **kwargs):
    Asynchronously run function *func* in a separate thread.

    Any *args and **kwargs supplied for this function are directly passed
    to *func*. Also, the current :class:`contextvars.Context` is propagated,
    allowing context variables from the main thread to be accessed in the
    separate thre

def wait(fs, *, timeout=None, return_when='ALL_COMPLETED'):
    Wait for the Futures or Tasks given by fs to complete.

    The fs iterable must not be empty.

    Coroutines will be wrapped in Tasks.

    Returns two sets of Future: (done, pending).

    Usage:

        done, pending = await asyncio.wait(fs)

    Note: This does not raise TimeoutError! Futures 

def wait_for(fut, timeout):
    Wait for the single Future or coroutine to complete, with timeout.

    Coroutine will be wrapped in Task.

    Returns result of the Future or coroutine.  When a timeout occurs,
    it cancels the task and raises TimeoutError.  To avoid the task
    cancellation, wrap it in shield().

    If the wa

def wrap_future(future, *, loop=None):
    Wrap concurrent.futures.Future object.


SOURCE:
"""The asyncio package, tracking PEP 3156."""

# flake8: noqa

import sys

# This relies on each of the submodules having an __all__ variable.
from .base_events import *
from .coroutines import *
from .events import *
from .exceptions import *
from .futures import *
from .locks import *
from .protocols import *
from .runners import *
from .queues import *
from .streams import *
from .subprocess import *
from .tasks import *
from .taskgroups import *
from .timeouts import *
from .threads import *
from .transports import *

__all__ = (base_events.__all__ +
           coroutines.__all__ +
           events.__all__ +
           exceptions.__all__ +
           futures.__all__ +
           locks.__all__ +
           protocols.__all__ +
           runners.__all__ +
           queues.__all__ +
           streams.__all__ +
           subprocess.__all__ +
           tasks.__all__ +
           taskgroups.__all__ +
           threads.__all__ +
           timeouts.__all__ +
           transports.__all__)

if sys.platform == 'win32':  # pragma: no cover
    from .windows_events import *
    __all__ += windows_events.__all__
else:
    from .unix_events import *  # pragma: no cover
    __all__ += unix_events.__all__

# 2015.11.18 11:59:44 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/bwobsolete_helpers/BWCoroutine.py
"""This module provides a number of utilities to simplify the writing of code
that needs to execute in order over a number of  frames using python generators
and BigWorld.callback().

To use this module, implement the required code as a generator by using the
'yield' keyword to specify points where the execution of the code needs to wait.
The generator function should be decorated with BWCoroutine or BWMemberCoroutine
to denote it as a coroutine. They yield should be used with one of the
BWWaitFor* classes defined in this module.
For example:

@BWCoroutine
def myFunction()
        print "Start of function"
        yeild BWWaitForPeriod( 10.0 )
        print "Ten seconds later"
"""
import BigWorld
from functools import partial
import types
import exceptions

def BWCoroutine(coroutineFunction):
    """The function doctorates the given function as a BWCoroutine. The
    decorated function will have an additional callback parameter as its first
    argument. This will be called when the coroutine exits.
    Note: For member functions of classes use @BWMemberCoroutine
    
    Example:
    
            @BWCoroutine
            def myCoroutine( waitTime ):
                    print "Start of myCoroutine. Waiting for %fseconds" % waitTime
                    yield BWWaitForPeriod( waitTime )
                    print "End of myCoroutine"
    
            def afterCoroutineFunction():
                    print "After coroutine"
    
            myCoroutine(afterCoroutineFunction )
    
    Result:
            Start of myCoroutine. Waiting for 8.65sec
            End of myCoroutine
            After coroutine
    
    """
    return _BWCoroutineFunction(coroutineFunction)


def BWMemberCoroutine(coroutineFunction):
    """This decorator function is similar to BWCoroutine but is designed for
    member functions of classes.
    """
    return _BWCoroutineMemberDescriptor(coroutineFunction)


class BWCoroutineTimeoutException(Exception):
    pass


class _BWCoroutineThread:

    def __init__(self, generator, completionCallback = None):
        raise isinstance(generator, types.GeneratorType) or AssertionError
        raise callable(completionCallback) or completionCallback is None or AssertionError
        self._generator = generator
        self._completionCallback = completionCallback
        self._waitObject = None
        return

    def run(self):
        self._tick()

    def _tick(self):
        raise isinstance(self._generator, types.GeneratorType) or AssertionError
        self._waitObject = None
        try:
            self._waitObject = self._generator.next()
            raise isinstance(self._waitObject, _BWWaitObject) or AssertionError
            self._waitObject.doWait(self)
        except StopIteration:
            if self._completionCallback is not None:
                self._completionCallback()
            return

        return

    def stop(self):
        raise isinstance(self._waitObject, _BWWaitObject) or AssertionError
        raise isinstance(self._generator, types.GeneratorType) or AssertionError
        self._waitObject.onStop()
        self._generator.close()

    def onContinue(self):
        self._tick()

    def raiseTimeout(self):
        try:
            self._waitObject = self._generator.throw(BWCoroutineTimeoutException)
        except StopIteration:
            pass


class _BWCoroutineFunction(object):

    def __init__(self, coroutineFunction):
        self._function = coroutineFunction

    def __call__(self, *args, **kwds):
        return _BWCoroutineThread(self._function(*args, **kwds))


class _BWCoroutineMemberFunction(object):

    def __init__(self, instance, coroutineFunction):
        self._instance = instance
        self._function = coroutineFunction

    def __call__(self, *args, **kwds):
        return _BWCoroutineThread(self._function(self._instance, *args, **kwds))


class _BWCoroutineMemberDescriptor(object):

    def __init__(self, coroutineFunction):
        self.coroutineFunction = coroutineFunction

    def __get__(self, instance, type):
        return _BWCoroutineMemberFunction(instance, self.coroutineFunction)


class _BWWaitObject:

    def __init__(self):
        pass

    def doWait(self, coroutineThread):
        pass

    def onStop(self):
        pass


class BWWaitForPeriod(_BWWaitObject):
    """This class implements a wait object that when yielded, from a suspends
    the coroutine for the given number of seconds using BigWorld.callback().
    """

    def __init__(self, waitTime):
        _BWWaitObject.__init__(self)
        self.waitTime = waitTime

    def doWait(self, coroutineThread):
        raise isinstance(coroutineThread, _BWCoroutineThread) or AssertionError
        BigWorld.callback(self.waitTime, coroutineThread.onContinue)


class BWWaitForCondition(_BWWaitObject):
    """This class implements a wait object that when yielded, poles it's
    provided condition at the specified frequency until true or the timeout
    period expires.
    """

    def __init__(self, condition, timeout = None, checkFrequency = 0.01):
        _BWWaitObject.__init__(self)
        if not callable(condition):
            raise AssertionError
            self._condition = condition
            self._checkFrequency = checkFrequency
            self._timeoutTime = timeout is not None and BigWorld.time() + timeout
        else:
            self._timeoutTime = None
        self._stopped = False
        return

    def doWait(self, coroutineThread):
        self._thread = coroutineThread
        self._tick()

    def _tick(self):
        if self._stopped:
            return
        else:
            if self._condition():
                self._thread.onContinue()
            elif self._timeoutTime is not None and BigWorld.time() >= self._timeoutTime:
                self._thread.raiseTimeout()
            else:
                BigWorld.callback(self._checkFrequency, self._tick)
            return

    def onStop(self):
        self._stopped = True


class BWWaitForCoroutine(_BWWaitObject):
    """This class implements a wait object that when yielded, waits for the
    given coroutine to complete.
    Note: This class provides its own callback for the given coroutine so that
    argument should not be included in the parameter list.
    
    @BWCoroutine
    def functionA( someString)
            print "Start of functionA", someString
            yeild BWWaitForPeriod( 10.0 )
            print "Ten seconds later: functionA", someString
    
    @BWCoroutine
    def functionB()
            print "Start of functionB"
    
            yeild BWWaitForCoroutine( functionA( "called from functionB" ) )
    
            print "functionB after function A (no timout)"
    
            try:
                    yeild BWWaitForCoroutine( functionA( "called from functionB with timeout" ), timeout = 5.0 )
            except BWCoroutineTimoutException:
                    print "functionB timed out waiting for function A"
    
    functionB( lambda: None )
    
    Result:
    Start of functionB
    Start of functionA called from functionB
    Ten seconds later: functionA called from functionB
    functionB after function A (no timout)
    Start of functionA called from functionB with timeout
    functionB timed out waiting for function A
    """

    def __init__(self, waitThread, timeout = None):
        _BWWaitObject.__init__(self)
        raise isinstance(waitThread, _BWCoroutineThread) or AssertionError
        self._waitThread = waitThread
        self._hostThread = None
        if not self._waitThread._completionCallback is None:
            raise AssertionError
            self._waitThread._completionCallback = self.handleCompletionCallback
            timeout is not None and BigWorld.callback(timeout, self.handleTimeout)
        return

    def doWait(self, coroutineThread):
        raise isinstance(coroutineThread, _BWCoroutineThread) or AssertionError
        self._hostThread = coroutineThread
        self._waitThread.run()

    def onStop(self):
        self._waitThread.stop()

    def handleCompletionCallback(self):

        def timeout_noop():
            pass

        self._onTimeout = timeout_noop
        self._hostThread.onContinue()

    def handleTimeout(self):
        self._onTimeout()

    def _onTimeout(self):
        self._waitThread.stop()
        self._hostThread.raiseTimeout()


def _niceFunctionString(f):
    if not (callable(f) or isinstance(f, types.GeneratorType) or isinstance(f, _BWCoroutineFunction)):
        raise AssertionError
        return isinstance(f, partial) and 'partial %s %s %s:%d' % (f.func.func_name,
         f.args,
         f.func.func_code.co_filename,
         f.func.func_code.co_firstlineno)
    elif isinstance(f, types.LambdaType):
        return 'lambda %s:%d' % (f.func_code.co_filename, f.func_code.co_firstlineno)
    elif isinstance(f, types.FunctionType):
        return 'function %s %s:%d' % (f.func_name, f.func_code.co_filename, f.func_code.co_firstlineno)
    elif isinstance(f, types.GeneratorType):
        return 'generator %s %s:%d' % (f.gi_frame.f_code.co_name, f.gi_frame.f_code.co_filename, f.gi_frame.f_lineno)
    elif isinstance(f, _BWCoroutineFunction):
        return _niceFunctionString(f.coroutineFunction)
    elif isinstance(f, _BWCoroutineMemberFunction):
        return _niceFunctionString(f.coroutineFunction)
    else:
        return str(f)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\bwobsolete_helpers\bwcoroutine.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:44 St�edn� Evropa (b�n� �as)

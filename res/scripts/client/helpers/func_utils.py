# 2015.11.18 11:57:17 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/helpers/func_utils.py
from time import sleep
import BigWorld
from functools import partial
from debug_utils import LOG_DEBUG

def callback(delay, obj, methodName, *args):
    return BigWorld.callback(delay, partial(callMethod, obj, methodName, *args))


def callMethod(obj, methodName, *args):
    if hasattr(obj, methodName):
        getattr(obj, methodName)(*args)


def debug_delay(timeLag):

    def delayCallDecorator(func):

        def delayCall(*args, **kwargs):
            BigWorld.callback(timeLag, partial(func, *args, **kwargs))

        return delayCall

    return delayCallDecorator


def logFunc(func):

    def wrapped(*args, **kwargs):
        LOG_DEBUG('|||||||||||||||||| %s(%s, %s) |||||||||||' % (func.func_name, args, kwargs))
        func(*args, **kwargs)

    return wrapped


def freeze(seconds, nextFrame = True):
    if nextFrame:
        LOG_DEBUG('Freeze call at', BigWorld.time())
        BigWorld.callback(0, partial(freeze, seconds, False))
        return
    LOG_DEBUG('Actual Freezing at', BigWorld.time())
    sleep(seconds)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\helpers\func_utils.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:57:17 Støední Evropa (bìžný èas)

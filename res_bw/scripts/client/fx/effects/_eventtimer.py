# 2015.11.18 12:00:00 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/FX/Effects/_EventTimer.py
import BigWorld

class EventTimer:

    def __init__(self):
        self.semaphore = 0
        self.callbackFn = None
        return

    def going(self):
        return self.semaphore != 0

    def reserve(self):
        self.semaphore += 1

    def release(self):
        self.semaphore -= 1

    def begin(self, duration, callbackFn):
        self.callbackFn = callbackFn
        self.semaphore += 1
        BigWorld.callback(duration, self.end)

    def extend(self, duration):
        self.semaphore += 1
        BigWorld.callback(duration, self.end)

    def end(self):
        self.semaphore -= 1
        if self.semaphore == 0:
            if self.callbackFn:
                self.callbackFn()
                self.callbackFn = None
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\fx\effects\_eventtimer.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:00:00 Støední Evropa (bìžný èas)

# 2015.11.18 11:59:57 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/bwobsolete_tests/Teleport.py
import BigWorld
import Math
import math
import random
from functools import partial

def teleportNext(timer, destinationList):
    dest = destinationList[0]
    BigWorld.player().tryToTeleport(dest[0], dest[1])
    if len(destinationList) > 1:
        BigWorld.callback(timer, partial(teleportNext, timer, destinationList[1:]))
    else:
        print 'teleport test finished'


def testTeleport():
    d = []
    d.append(['spaces/highlands', 'demo2'])
    d.append(['spaces/highlands', 'demo3'])
    d.append(['spaces/highlands', 'demo4'])
    d.append(['spaces/arctic', 'demo1'])
    d.append(['spaces/arctic', 'demo2'])
    d.append(['spaces/arctic', 'demo3'])
    d.append(['spaces/arctic', 'demo4'])
    d.append(['spaces/highlands', 'demo1'])
    BigWorld.callback(0.1, partial(teleportNext, 20, d))
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\bwobsolete_tests\teleport.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:57 Støední Evropa (bìžný èas)

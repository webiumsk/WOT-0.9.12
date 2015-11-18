# 2015.11.18 11:59:57 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/bwobsolete_tests/TerrainCollision.py
import BigWorld
import Math
import math
import random

def stab(start):
    samplePointStart = start - (0, 10000, 0)
    samplePointEnd = start + (0, 10000, 0)
    return BigWorld.collide(BigWorld.player().spaceID, samplePointStart, samplePointEnd)


def spam(numSamples, start, extent):
    misses = 0
    for i in range(numSamples):
        samplePoint = Math.Vector3()
        samplePoint[0] = start[0] + extent[0] * random.random()
        samplePoint[1] = 0
        samplePoint[2] = start[2] + extent[2] * random.random()
        samplePointStart = samplePoint - (0, 10000, 0)
        samplePointEnd = samplePoint + (0, 10000, 0)
        if None == stab(samplePoint):
            print 'Miss @ X,Z (', samplePointStart[0], ',', samplePointEnd[2], ')'
            misses += 1

    return misses


def scan(numSamples, start, extent):
    misses = 0
    ooNumSamples = 1 / float(numSamples)
    for i in range(numSamples):
        t = i * ooNumSamples
        sample = Math.Vector3()
        sample[0] = start[0] + extent[0] * t
        sample[1] = 0
        sample[2] = start[2] + extent[2] * t
        if None == stab(sample):
            print 'Miss @ X,Z (', sample[0], ',', sample[2], ')'
            misses += 1

    return misses
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\bwobsolete_tests\terraincollision.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:57 Støední Evropa (bìžný èas)

# 2015.11.18 11:59:00 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/GasAttackSettings.py
import Math

class GasAttackState(object):
    NO = 0
    PREPARE = 1
    ATTACK = 2
    DONE = 3


class GasAttackSettings:
    DEATH_DELAY = 10

    def __init__(self, attackLength, preparationPeriod, position, startRadius, endRadius, compressionTime):
        self.attackLength, self.preparationPeriod, self.position, self.startRadius, self.endRadius, self.compressionTime = (attackLength,
         preparationPeriod,
         Math.Vector3(position),
         startRadius,
         endRadius,
         compressionTime)
        if compressionTime == 0:
            self.compressionSpeed = 0
            self.startRadius = self.endRadius
        else:
            self.compressionSpeed = float(startRadius - endRadius) / compressionTime

    def stateFor(self, timeFromActivation):
        if timeFromActivation <= self.preparationPeriod:
            return (GasAttackState.PREPARE, (self.position, self.startRadius))
        currentRadius = self.startRadius - (timeFromActivation - self.preparationPeriod) * self.compressionSpeed
        if currentRadius <= self.endRadius:
            return (GasAttackState.DONE, (self.position, self.endRadius))
        return (GasAttackState.ATTACK, (self.position, currentRadius))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\gasattacksettings.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:00 St�edn� Evropa (b�n� �as)

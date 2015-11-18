# 2015.11.18 12:00:03 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/FX/Events/ResetTimeTriggeredParticles.py
from FX import s_sectionProcessors
from ParticleSubSystem import *

class ResetTimeTriggeredParticles(ParticleSubSystem):
    """
    This class implements an Event that resets the time trigger of a
    particle system actor.  This is useful in an Effect that is used
    multiple times.  It means that when reused, the time-triggered particles
    will begin "from the beginning" instead of sometime through their normal
    cycle.
    It only works on ParticleSystem actors.
    """

    def __init__(self):
        ParticleSubSystem.__init__(self)

    def isInteresting(self, subSystem):
        act = subSystem.action(SOURCE_PSA)
        return act and act.timeTriggered

    def resetTimeTrigger(self, actor, source, target, subSystem):
        subSystem.clear()
        act = subSystem.action(SOURCE_PSA)
        act.timeTriggered = 0
        act.timeTriggered = 1

    def go(self, effect, actor, source, target, **kargs):
        self.subSystemIterate(actor, source, target, self.resetTimeTrigger)
        return 0.0


s_sectionProcessors['ResetTimeTriggeredParticles'] = ResetTimeTriggeredParticles
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\fx\events\resettimetriggeredparticles.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:00:03 Støední Evropa (bìžný èas)

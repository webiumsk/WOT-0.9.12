# 2015.11.18 12:00:03 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/FX/Events/SetOrbitorPoint.py
from FX import s_sectionProcessors
from ParticleSubSystem import *
import Pixie
from bwdebug import *

class SetOrbitorPoint(ParticleSubSystem):
    """
    This class implements an event that sets the world location of an orbitor
    to the position of the Effect source when the effect is started.
    """

    def __init__(self):
        ParticleSubSystem.__init__(self)

    def isInteresting(self, subSystem):
        act = subSystem.action(ORBITOR_PSA)
        return act != None

    def setOrbitorPoint(self, actor, source, target, subSystem):
        try:
            act = subSystem.action(ORBITOR_PSA)
            act.point = source.position
        except:
            ERROR_MSG('setOrbitorPoint has a problem with finding the position of the source object', source)

    def go(self, effect, actor, source, target, **kargs):
        self.subSystemIterate(actor, source, target, self.setOrbitorPoint)
        return 0.0


s_sectionProcessors['SetOrbitorPoint'] = SetOrbitorPoint
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\fx\events\setorbitorpoint.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:00:03 Støední Evropa (bìžný èas)

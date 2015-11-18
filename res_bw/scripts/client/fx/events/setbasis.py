# 2015.11.18 12:00:03 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/FX/Events/SetBasis.py
from FX import s_sectionProcessors
from ParticleSubSystem import *
from bwdebug import *

class SetBasis(ParticleSubSystem):
    """
    This class implements an Event that sets the basis vectors for a Particle
    System.
    """

    def __init__(self):
        ParticleSubSystem.__init__(self)

    def setBasis(self, actor, source, target, subSystem):
        subSystem.explicitPosition = self.worldPos
        subSystem.explicitDirection = self.worldDir

    def go(self, effect, actor, source, target, **kargs):
        """
        This method initiates the SetBasis event.  It requires a "Basis"
        parameter to be passed into the variable arguments dictionary, which
        is a tuple of (dir,pos).  Both are in world-space.
        """
        try:
            self.worldDir, self.worldPos = kargs['Basis']
            self.subSystemIterate(actor, source, target, self.setBasis)
            del self.worldDir
            del self.worldPos
        except:
            WARNING_MSG('No basis was passed into the argument list', self, actor, source, target, kargs)

        return 0.0


s_sectionProcessors['SetBasis'] = SetBasis
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\fx\events\setbasis.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:00:03 Støední Evropa (bìžný èas)

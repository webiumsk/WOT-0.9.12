# 2015.11.18 11:59:58 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/FX/Actors/ParticleSystem.py
import Pixie
import BigWorld
from bwdebug import *
from FX.Actor import Actor
from FX import s_sectionProcessors

class ParticleSystem(Actor):
    """
    This class implements an Actor that is a PyMetaParticleSystem.
    """

    def load(self, pSection, prereqs = None):
        """
        This method loads the ParticleSystem Actor from a data section. The
        the particle system resource ID is read from the section name.
        
        It is recommended to call this method with prerequisites passed in, as
        even if the textures referred to by the particle system are already in
        memory, a PyMetaParticleSystem can still take a significant time to
        construct.
        """
        try:
            actor = prereqs.pop(pSection.asString)
        except:
            try:
                actor = Pixie.create(pSection.asString)
            except:
                ERROR_MSG('Could not create particle system', pSection.asString)
                actor = None

        return actor

    def prerequisites(self, pSection):
        return [pSection.asString]


s_sectionProcessors['ParticleSystem'] = ParticleSystem
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\fx\actors\particlesystem.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:58 Støední Evropa (bìžný èas)

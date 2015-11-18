# 2015.11.18 12:00:01 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/FX/Events/ForceParticle.py
from FX.Event import Event
from FX.Event import TRANSFORM_DEPENDENT_EVENT
from FX import s_sectionProcessors
import Pixie
from bwdebug import *

class ForceParticle(Event):
    """
    This class implements an Event that spawns particles from a particle
    system actor.  By default it spawns one unit of particles, however this is
    configurable at runtime via the variable arguments dictionary.
    This class can be created via the name "Force" in addition to the standard
    class factory name of "ForceParticle."
    """

    def go(self, effect, actor, source, target, **kargs):
        """
        This method initiates the ForceParticle Event.  It takes an
        optional "NumberToForce" argument in the variable arguments dictionary.
        """
        try:
            amount = kargs['NumberToForce']
        except:
            amount = 1

        try:
            actor.force(amount)
            return actor.duration() + 0.001
        except:
            ERROR_MSG('actor is not a particle system!', actor)
            return 0.0

    def duration(self, actor, source, target):
        try:
            return actor.duration() + 0.001
        except:
            return 0.0

    def eventTiming(self):
        return TRANSFORM_DEPENDENT_EVENT


s_sectionProcessors['ForceParticle'] = ForceParticle
s_sectionProcessors['Force'] = ForceParticle
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\fx\events\forceparticle.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:00:01 St�edn� Evropa (b�n� �as)

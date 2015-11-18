# 2015.11.18 12:00:04 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/FX/Joints/Entity.py
from FX import s_sectionProcessors
from FX import typeCheck
from FX.Joint import Joint
from bwdebug import *
import BigWorld
import traceback

class Entity(Joint):
    """
    This class implements a Joint that attaches an actor to an Entity.
    
    The actor may be any PyAttachment, for example a model or a
    particle system.
    
    If the actor is a Model, a motor is attached to it so that it
    follows the Entity's movements.
    
    If the actor is a Particle System, it is placed in the world at the
    current location of the Entity, but will not move around once attached.
    """

    def attach(self, actor, source, target = None):
        if actor.attached:
            ERROR_MSG('actor is already attached!', self, actor, source)
            return 0
        elif source is None:
            return 0
        else:
            try:
                source.addModel(actor)
            except:
                ERROR_MSG('error in addModel to entity', self, actor, source)

            moved = 0
            try:
                actor.addMotor(BigWorld.Servo(source.matrix))
                moved = 1
            except AttributeError:
                try:
                    actor.explicitPosition = source.position
                    moved = 1
                except AttributeError:
                    try:
                        for i in xrange(0, actor.nSystems()):
                            actor.system(i).explicitPosition = source.position

                        moved = 1
                    except:
                        traceback.print_exc()

            if not moved:
                ERROR_MSG('Unknown error trying to move actor to the correct location', actor, source)
            return

    def detach(self, actor, source, target = None):
        if not actor.attached:
            return
        try:
            source.delModel(actor)
        except:
            ERROR_MSG('error in delModel from entity', self, actor, source)


s_sectionProcessors['Entity'] = Entity
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\fx\joints\entity.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:00:04 St�edn� Evropa (b�n� �as)

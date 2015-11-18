# 2015.11.18 11:59:43 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/FilterUtilities.py
"""This module contains a number of useful script functions for working with the
entity filters shipped with BigWorld.
"""
import BigWorld

def enableVisualiseAvatarFilter(entity):
    """This method uses unit cubes to visulise the input data being sent to
    the given entity's filter.  The models are added to the given entity for
    rendering.
    """
    if hasattr(entity.filter, 'debugMatrixes') and callable(entity.filter.debugMatrixes):
        disableVisualiseAvatarFilter(entity)
        entity._filterCubeModels = []
        for matrixProvider in entity.filter.debugMatrixes():
            cubeModel = BigWorld.Model('helpers/models/unit_cube.model')
            servo = BigWorld.Servo(matrixProvider)
            cubeModel.addMotor(servo)
            entity.addModel(cubeModel)
            entity._filterCubeModels.append(cubeModel)


def disableVisualiseAvatarFilter(entity):
    """This method removes all the debug models used to visualise
    the AvatarFilter for the entity.
    """
    if hasattr(entity, '_filterCubeModels'):
        for cube in entity._filterCubeModels:
            entity.delModel(cube)

        del entity._filterCubeModels


def enableVisualiseAllAvatarFilters():
    """This method uses unit cubes to visulise the input data being sent to all
    AvatarFilters used in the current scene. The generated models are added to
    each entity for rendering.
    """
    for entity in BigWorld.entities.values():
        enableVisualiseAvatarFilter(entity)


def disableVisualiseAllAvatarFilters():
    """This method removes all the debug models used to visualise
    the AvatarFilter for all entities.
    """
    for entity in BigWorld.entities.values():
        disableVisualiseAvatarFilter(entity)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\filterutilities.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:43 St�edn� Evropa (b�n� �as)

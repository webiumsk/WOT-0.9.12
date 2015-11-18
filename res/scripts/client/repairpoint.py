# 2015.11.18 11:51:07 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/RepairPoint.py
import BigWorld
from Math import Vector3
from debug_utils import LOG_DEBUG
from CTFManager import _CTFCheckPoint, _CTFPointFlag, _UDOAttributeChecker

class RepairPoint(BigWorld.UserDataObject, _CTFCheckPoint, _CTFPointFlag, _UDOAttributeChecker):
    _COLOR = 4294967295L
    _OVER_TERRAIN_HEIGHT = 0.5

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        _UDOAttributeChecker.__init__(self)
        self.checkAttribute('radiusModel')
        self.checkAttribute('flagModel')
        LOG_DEBUG('RepairPoint ', self.position, self.radius)
        _CTFCheckPoint.__init__(self, self.radiusModel)
        _CTFPointFlag.__init__(self, self.flagModel, self.position)
        if self.__isVisibleForCurrentArena():
            self._createTerrainSelectedArea(self.position, self.radius * 2.0, self._OVER_TERRAIN_HEIGHT, self._COLOR)
            self._createFlag()

    def __del__(self):
        if self.isAttrCheckFailed:
            return
        _CTFCheckPoint.__del__(self)
        _CTFPointFlag.__del__(self)

    def __isVisibleForCurrentArena(self):
        arenaType = BigWorld.player().arena.arenaType
        if hasattr(arenaType, 'repairPoints'):
            repairPoints = arenaType.repairPoints
            for pt in repairPoints:
                if 'guid' not in pt:
                    continue
                if pt['guid'] == self.guid:
                    return True

        return False
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\repairpoint.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:51:07 Støední Evropa (bìžný èas)

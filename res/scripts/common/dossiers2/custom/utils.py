# 2015.11.18 11:59:30 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/dossiers2/custom/utils.py
from items import vehicles
import arena_achievements

def getVehicleNationID(vehTypeCompDescr):
    return vehicles.parseIntCompactDescr(vehTypeCompDescr)[1]


def isVehicleSPG(vehTypeCompDescr):
    itemTypeID, nationID, vehicleID = vehicles.parseIntCompactDescr(vehTypeCompDescr)
    return 'SPG' in vehicles.g_list.getList(nationID)[vehicleID]['tags']


def getInBattleSeriesIndex(seriesName):
    return arena_achievements.INBATTLE_SERIES_INDICES[seriesName]
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\dossiers2\custom\utils.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:30 Støední Evropa (bìžný èas)

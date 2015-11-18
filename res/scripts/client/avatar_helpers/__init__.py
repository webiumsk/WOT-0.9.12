# 2015.11.18 11:51:41 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/avatar_helpers/__init__.py
import BigWorld

def getAvatarDatabaseID():
    dbID = 0L
    player = BigWorld.player()
    arena = getattr(player, 'arena', None)
    if arena is not None:
        vehID = getattr(player, 'playerVehicleID', None)
        if vehID is not None and vehID in arena.vehicles:
            dbID = arena.vehicles[vehID]['accountDBID']
    return dbID
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\avatar_helpers\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:51:41 Støední Evropa (bìžný èas)

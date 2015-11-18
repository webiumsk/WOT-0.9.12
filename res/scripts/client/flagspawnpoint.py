# 2015.11.18 11:51:01 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/FlagSpawnPoint.py
import BigWorld
from debug_utils import LOG_DEBUG

class FlagSpawnPoint(BigWorld.UserDataObject):

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        LOG_DEBUG('FlagSpawnPoint ', self.position)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\flagspawnpoint.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:51:01 Støední Evropa (bìžný èas)

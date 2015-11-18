# 2015.11.18 11:51:03 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/Login.py
import BigWorld
from PlayerEvents import g_playerEvents
from ConnectionManager import connectionManager
from debug_utils import *

class PlayerLogin(BigWorld.Entity):

    def __init__(self):
        pass

    def onBecomePlayer(self):
        pass

    def onBecomeNonPlayer(self):
        pass

    def onKickedFromServer(self, checkoutPeripheryID):
        LOG_MX('onKickedFromServer', checkoutPeripheryID)
        g_playerEvents.onKickWhileLoginReceived(checkoutPeripheryID)

    def receiveLoginQueueNumber(self, queueNumber):
        LOG_MX('receiveLoginQueueNumber', queueNumber)
        g_playerEvents.onLoginQueueNumberReceived(queueNumber)

    def handleKeyEvent(self, event):
        return False


Login = PlayerLogin
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\login.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:51:03 Støední Evropa (bìžný èas)

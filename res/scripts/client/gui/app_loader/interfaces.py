# 2015.11.18 11:51:48 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/app_loader/interfaces.py


class IAppFactory(object):

    def getPackageImporter(self):
        return None

    def hasApp(self, appNS):
        return False

    def getApp(self, appNS = None):
        return None

    def getDefLobbyApp(self):
        return None

    def getDefBattleApp(self):
        return None

    def createLobby(self):
        pass

    def destroyLobby(self):
        pass

    def showLobby(self):
        pass

    def hideLobby(self):
        pass

    def createBattle(self):
        pass

    def destroyBattle(self):
        pass

    def destroy(self):
        pass

    def hasLobby(self):
        return False

    def hasBattle(self):
        return False

    def attachCursor(self, appNS):
        pass

    def detachCursor(self, appNS):
        pass

    def goToIntroVideo(self, appNS):
        pass

    def goToLogin(self, appNS):
        pass

    def goToLobby(self, appNS):
        pass

    def goToBattleLoading(self, appNS):
        pass

    def goToTutorialLoading(self, appNS):
        pass

    def goToFalloutMultiTeamLoading(self, appNS):
        pass

    def goToBattle(self, appNS):
        pass

    def showDisconnectDialog(self, appNS, description):
        pass
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\app_loader\interfaces.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:51:48 Støední Evropa (bìžný èas)

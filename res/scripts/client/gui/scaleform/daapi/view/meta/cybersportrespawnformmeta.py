# 2015.11.18 11:54:57 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CyberSportRespawnFormMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyRoomView import BaseRallyRoomView

class CyberSportRespawnFormMeta(BaseRallyRoomView):

    def as_updateEnemyStatusS(self, statusID, enemyStatusLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_updateEnemyStatus(statusID, enemyStatusLabel)

    def as_setTeamNameS(self, name):
        if self._isDAAPIInited():
            return self.flashObject.as_setTeamName(name)

    def as_setTeamEmblemS(self, teamEmblemId):
        if self._isDAAPIInited():
            return self.flashObject.as_setTeamEmblem(teamEmblemId)

    def as_setArenaTypeIdS(self, mapName, arenaTypeID):
        if self._isDAAPIInited():
            return self.flashObject.as_setArenaTypeId(mapName, arenaTypeID)

    def as_timerUpdateS(self, timeLeft):
        if self._isDAAPIInited():
            return self.flashObject.as_timerUpdate(timeLeft)

    def as_statusUpdateS(self, status, level, tooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_statusUpdate(status, level, tooltip)

    def as_setTotalLabelS(self, hasTotalLevelError, totalLevelLabel, totalLevel):
        if self._isDAAPIInited():
            return self.flashObject.as_setTotalLabel(hasTotalLevelError, totalLevelLabel, totalLevel)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\cybersportrespawnformmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:54:57 Støední Evropa (bìžný èas)

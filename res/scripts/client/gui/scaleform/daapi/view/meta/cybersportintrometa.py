# 2015.11.18 11:54:57 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CyberSportIntroMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyIntroView import BaseRallyIntroView

class CyberSportIntroMeta(BaseRallyIntroView):

    def requestVehicleSelection(self):
        self._printOverrideError('requestVehicleSelection')

    def startAutoMatching(self):
        self._printOverrideError('startAutoMatching')

    def showSelectorPopup(self):
        self._printOverrideError('showSelectorPopup')

    def showStaticTeamProfile(self):
        self._printOverrideError('showStaticTeamProfile')

    def cancelWaitingTeamRequest(self):
        self._printOverrideError('cancelWaitingTeamRequest')

    def showStaticTeamStaff(self):
        self._printOverrideError('showStaticTeamStaff')

    def joinClubUnit(self):
        self._printOverrideError('joinClubUnit')

    def as_setSelectedVehicleS(self, selectedVehicleData, selectedVehicleIsReady, warnTooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedVehicle(selectedVehicleData, selectedVehicleIsReady, warnTooltip)

    def as_setTextsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setTexts(data)

    def as_setStaticTeamDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticTeamData(data)

    def as_setNoVehiclesS(self, warnTooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_setNoVehicles(warnTooltip)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\cybersportintrometa.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:54:57 St�edn� Evropa (b�n� �as)

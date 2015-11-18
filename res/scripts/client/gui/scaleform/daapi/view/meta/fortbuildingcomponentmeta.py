# 2015.11.18 11:54:59 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortBuildingComponentMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FortBuildingComponentMeta(BaseDAAPIComponent):

    def onTransportingRequest(self, exportFrom, importTo):
        self._printOverrideError('onTransportingRequest')

    def requestBuildingProcess(self, direction, position):
        self._printOverrideError('requestBuildingProcess')

    def upgradeVisitedBuilding(self, uid):
        self._printOverrideError('upgradeVisitedBuilding')

    def requestBuildingToolTipData(self, uid, type):
        self._printOverrideError('requestBuildingToolTipData')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setBuildingDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBuildingData(data)

    def as_setBuildingToolTipDataS(self, uid, type, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setBuildingToolTipData(uid, type, value)

    def as_refreshTransportingS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_refreshTransporting()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\fortbuildingcomponentmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:54:59 St�edn� Evropa (b�n� �as)

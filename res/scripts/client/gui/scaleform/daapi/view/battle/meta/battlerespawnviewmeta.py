# 2015.11.18 11:53:15 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/meta/BattleRespawnViewMeta.py
from gui.Scaleform.daapi.view.battle.meta.BattleComponentMeta import BattleComponentMeta

class BattleRespawnViewMeta(BattleComponentMeta):

    def py_vehicleSelected(self, vehicleID):
        raise NotImplementedError

    def onPostmortemBtnClickS(self):
        raise NotImplementedError

    def as_updateRespawnViewS(self, vehicleName, slotsStatesData):
        self._flashObject.as_updateRespawnView(vehicleName, slotsStatesData)

    def as_showRespawnViewS(self, vehicleName, slotsStatesData):
        self._flashObject.as_showRespawnView(vehicleName, slotsStatesData)

    def as_hideRespawnViewS(self):
        self._flashObject.as_hideRespawnView()

    def as_respawnViewUpdateTimerS(self, mainTimer, slots):
        self._flashObject.as_respawnViewUpdateTimer(mainTimer, slots)

    def as_initializeS(self, mainData, slots, helpText):
        self._flashObject.as_initialize(mainData, slots, helpText)

    def as_showGasAtackMode(self):
        self._flashObject.as_showGasAtackMode()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\battle\meta\battlerespawnviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:53:15 Støední Evropa (bìžný èas)

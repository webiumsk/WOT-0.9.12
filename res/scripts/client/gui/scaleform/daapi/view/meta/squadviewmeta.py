# 2015.11.18 11:55:15 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SquadViewMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyRoomView import BaseRallyRoomView

class SquadViewMeta(BaseRallyRoomView):

    def leaveSquad(self):
        self._printOverrideError('leaveSquad')

    def as_updateBattleTypeInfoS(self, tooltip, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_updateBattleTypeInfo(tooltip, isVisible)

    def as_updateBattleTypeS(self, battleTypeName, isEventEnabled, isNew):
        if self._isDAAPIInited():
            return self.flashObject.as_updateBattleType(battleTypeName, isEventEnabled, isNew)

    def as_isFalloutS(self, isFallout):
        if self._isDAAPIInited():
            return self.flashObject.as_isFallout(isFallout)

    def as_updateInviteBtnStateS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_updateInviteBtnState(isEnabled)

    def as_setCoolDownForReadyButtonS(self, timer):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoolDownForReadyButton(timer)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\squadviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:55:15 Støední Evropa (bìžný èas)

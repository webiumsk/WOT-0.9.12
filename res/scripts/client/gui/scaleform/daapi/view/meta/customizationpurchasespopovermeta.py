# 2015.11.18 11:54:57 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CustomizationPurchasesPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class CustomizationPurchasesPopoverMeta(SmartPopOverView):

    def cleanAll(self):
        self._printOverrideError('cleanAll')

    def removePurchase(self, groupId, idx):
        self._printOverrideError('removePurchase')

    def as_setPurchasesInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setPurchasesInitData(data)

    def as_setPurchasesDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setPurchasesData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\customizationpurchasespopovermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:54:57 Støední Evropa (bìžný èas)

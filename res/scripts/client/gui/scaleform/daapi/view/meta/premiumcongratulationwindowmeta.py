# 2015.11.18 11:55:08 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PremiumCongratulationWindowMeta.py
from gui.Scaleform.daapi.view.meta.SimpleWindowMeta import SimpleWindowMeta

class PremiumCongratulationWindowMeta(SimpleWindowMeta):

    def onToBuyClick(self):
        self._printOverrideError('onToBuyClick')

    def as_setDataS(self, imagePath, percent, btnLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(imagePath, percent, btnLabel)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\premiumcongratulationwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:55:08 Støední Evropa (bìžný èas)

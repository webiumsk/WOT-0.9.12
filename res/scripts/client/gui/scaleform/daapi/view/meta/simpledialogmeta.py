# 2015.11.18 11:55:14 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SimpleDialogMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class SimpleDialogMeta(AbstractWindowView):

    def onButtonClick(self, buttonId):
        self._printOverrideError('onButtonClick')

    def as_setTextS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setText(text)

    def as_setTitleS(self, title):
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(title)

    def as_setButtonsS(self, buttonNames):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtons(buttonNames)

    def as_setButtonEnablingS(self, id, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtonEnabling(id, isEnabled)

    def as_setButtonFocusS(self, id):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtonFocus(id)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\simpledialogmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:55:14 St�edn� Evropa (b�n� �as)

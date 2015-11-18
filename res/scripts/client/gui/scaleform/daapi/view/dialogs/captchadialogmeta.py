# 2015.11.18 11:53:16 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/CaptchaDialogMeta.py
from gui.Scaleform.daapi.view.dialogs import IDialogMeta
from gui.shared import events

class CaptchaDialogMeta(IDialogMeta):

    def __init__(self, errorText = None):
        self.__errorText = errorText

    def hasError(self):
        return self.__errorText is not None and len(self.__errorText)

    def getErrorText(self):
        return self.__errorText

    def getEventType(self):
        return events.ShowDialogEvent.SHOW_CAPTCHA_DIALOG
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\dialogs\captchadialogmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:53:16 Støední Evropa (bìžný èas)

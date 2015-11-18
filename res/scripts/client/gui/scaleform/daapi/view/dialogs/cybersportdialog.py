# 2015.11.18 11:53:17 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/CyberSportDialog.py
from gui.Scaleform.daapi.view.dialogs.SimpleDialog import SimpleDialog

class CyberSportDialog(SimpleDialog):

    def __init__(self, meta, handler):
        super(CyberSportDialog, self).__init__(meta.getMessage(), meta.getTitle(), meta.getButtonLabels(), handler, meta.getViewScopeType())
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\dialogs\cybersportdialog.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:53:17 Støední Evropa (bìžný èas)

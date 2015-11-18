# 2015.11.18 11:53:58 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/fortifications/FortClanStatisticsWindow.py
from gui.Scaleform.daapi.view.meta.FortClanStatisticsWindowMeta import FortClanStatisticsWindowMeta

class FortClanStatisticsWindow(FortClanStatisticsWindowMeta):

    def __init__(self, ctx = None):
        super(FortClanStatisticsWindow, self).__init__()
        self.data = ctx
        self.data.onDataChanged += self.onDataChanged

    def _populate(self):
        super(FortClanStatisticsWindow, self)._populate()
        self.as_setDataS(self.data.getData())

    def _dispose(self):
        self.data.stopFortListening()
        super(FortClanStatisticsWindow, self)._dispose()

    def onDataChanged(self):
        self.as_setDataS(self.data.getData())

    def onWindowClose(self):
        self.destroy()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\fortifications\fortclanstatisticswindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:53:58 Støední Evropa (bìžný èas)

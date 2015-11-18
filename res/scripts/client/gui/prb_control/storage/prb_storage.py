# 2015.11.18 11:52:54 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/prb_control/storage/prb_storage.py
from gui.prb_control.storage.local_storage import LocalStorage

class TrainingStorage(LocalStorage):
    __slots__ = ('isObserver',)

    def __init__(self):
        super(TrainingStorage, self).__init__()
        self.isObserver = False

    def clear(self):
        self.isObserver = False

    def suspend(self):
        self.clear()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\prb_control\storage\prb_storage.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:54 Støední Evropa (bìžný èas)

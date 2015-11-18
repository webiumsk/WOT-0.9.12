# 2015.11.18 11:52:01 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/battle_results/items.py
from functools import partial
from gui.shared.utils import mapTextureToTheMemory

class TeamInfo(object):

    def __init__(self, name = '', emblemRq = None):
        self.__name = name
        self.__emblemRq = emblemRq or (lambda cb: cb(None))

    def getUserName(self):
        return self.__name

    def requestEmblemID(self, callback):

        def _cbWrapper(cb, emblem):
            if emblem is not None:
                cb(mapTextureToTheMemory(emblem))
            else:
                cb(None)
            return

        self.__emblemRq(partial(_cbWrapper, callback))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\battle_results\items.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:01 Støední Evropa (bìžný èas)

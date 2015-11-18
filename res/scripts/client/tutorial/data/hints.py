# 2015.11.18 11:58:27 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/tutorial/data/hints.py
from collections import namedtuple
HintProps = namedtuple('HintProps', ('uniqueID', 'hintID', 'itemID', 'text', 'hasBox', 'arrow', 'padding'))

class HintsData(object):

    def __init__(self):
        super(HintsData, self).__init__()
        self.__guiFilePath = None
        self.__hints = {}
        return

    def setGuiFilePath(self, filePath):
        self.__guiFilePath = filePath

    def getGuiFilePath(self):
        return self.__guiFilePath

    def addHint(self, hint):
        self.__hints[hint['itemID']] = hint

    def hintForItem(self, itemID):
        hint = None
        if itemID in self.__hints:
            hint = self.__hints[itemID]
        return hint

    def markAsShown(self, hint):
        itemID = hint['itemID']
        if itemID in self.__hints:
            del self.__hints[itemID]

    @property
    def hintsCount(self):
        return len(self.__hints)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\tutorial\data\hints.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:58:27 Støední Evropa (bìžný èas)

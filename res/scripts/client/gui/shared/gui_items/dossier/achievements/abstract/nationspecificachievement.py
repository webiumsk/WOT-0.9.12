# 2015.11.18 11:56:39 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/abstract/NationSpecificAchievement.py
from SimpleProgressAchievement import SimpleProgressAchievement
from dossiers2.custom.cache import getCache as getDossiersCache
from gui import nationCompareByIndex

class NationSpecificAchievement(SimpleProgressAchievement):

    def __init__(self, namePrefix, nationID, block, dossier, value = None):
        self._nationID = nationID
        super(NationSpecificAchievement, self).__init__(self.makeFullName(namePrefix, nationID), block, dossier, value)

    @classmethod
    def makeFullName(cls, name, nationID):
        if nationID != -1:
            name += str(nationID)
        return name

    def getNationID(self):
        return self._nationID

    def _readValue(self, dossier):
        return 0

    def _readLevelUpTotalValue(self, dossier):
        cache = getDossiersCache()
        if self._nationID != -1:
            return len(cache['vehiclesInTreesByNation'][self._nationID])
        else:
            return len(cache['vehiclesInTrees'])

    def _getDoneStatus(self, dossier):
        return bool(dossier.getRecordValue(*self.getRecordName()))

    def __cmp__(self, other):
        res = super(NationSpecificAchievement, self).__cmp__(other)
        if res:
            return res
        if isinstance(other, NationSpecificAchievement):
            if self._nationID != -1 and other._nationID != -1:
                return nationCompareByIndex(self._nationID, other._nationID)
        return 0
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\abstract\nationspecificachievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:56:39 Støední Evropa (bìžný èas)

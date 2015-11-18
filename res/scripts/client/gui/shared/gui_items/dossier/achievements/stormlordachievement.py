# 2015.11.18 11:56:37 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/StormLordAchievement.py
from abstract import ClassProgressAchievement
from debug_utils import LOG_DEBUG
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB

class StormLordAchievement(ClassProgressAchievement):

    def __init__(self, dossier, value = None):
        super(StormLordAchievement, self).__init__('stormLord', _AB.FALLOUT, dossier, value)

    def getNextLevelInfo(self):
        return ('vehiclesLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.FALLOUT, 'stormLord')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getFalloutStats().getConsumablesFragsCount()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\stormlordachievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:56:37 St�edn� Evropa (b�n� �as)

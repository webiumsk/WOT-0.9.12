# 2015.11.18 11:56:32 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/FireAndSwordAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import ClassProgressAchievement
from abstract.mixins import Fortification
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB

class FireAndSwordAchievement(Fortification, ClassProgressAchievement):

    def __init__(self, dossier, value = None):
        ClassProgressAchievement.__init__(self, 'fireAndSword', _AB.FORT, dossier, value)

    def getNextLevelInfo(self):
        return ('fortDefResLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.FORT, 'fireAndSword')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getFortMiscStats().getLootInBattles()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\fireandswordachievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:56:32 St�edn� Evropa (b�n� �as)

# 2015.11.18 11:56:39 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/WinnerLaurelsAchievement.py
from abstract import ClassProgressAchievement
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB

class WinnerLaurelsAchievement(ClassProgressAchievement):

    def __init__(self, dossier, value = None):
        super(WinnerLaurelsAchievement, self).__init__('winnerLaurels', _AB.FALLOUT, dossier, value)

    def getNextLevelInfo(self):
        return ('winPointsLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.FALLOUT, 'winnerLaurels')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getFalloutStats().getVictoryPoints()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\winnerlaurelsachievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:56:39 Støední Evropa (bìžný èas)

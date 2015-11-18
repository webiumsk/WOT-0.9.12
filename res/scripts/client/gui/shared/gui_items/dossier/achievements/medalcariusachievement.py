# 2015.11.18 11:56:34 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/MedalCariusAchievement.py
from abstract import ClassProgressAchievement
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB

class MedalCariusAchievement(ClassProgressAchievement):

    def __init__(self, dossier, value = None):
        super(MedalCariusAchievement, self).__init__('medalCarius', _AB.TOTAL, dossier, value)

    def getNextLevelInfo(self):
        return ('vehiclesLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, 'medalCarius')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getRandomStats().getFragsCount() - dossier.getClanStats().getFragsCount() + dossier.getTeam7x7Stats().getFragsCount() + dossier.getFortBattlesStats().getFragsCount() + dossier.getFortSortiesStats().getFragsCount() + dossier.getGlobalMapStats().getFragsCount()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\medalcariusachievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:56:34 Støední Evropa (bìžný èas)

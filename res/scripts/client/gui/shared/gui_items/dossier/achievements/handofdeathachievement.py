# 2015.11.18 11:56:33 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/HandOfDeathAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SeriesAchievement

class HandOfDeathAchievement(SeriesAchievement):

    def __init__(self, dossier, value = None):
        super(HandOfDeathAchievement, self).__init__('handOfDeath', _AB.SINGLE, dossier, value)

    def _getCounterRecordNames(self):
        return ((_AB.TOTAL, 'killingSeries'), (_AB.TOTAL, 'maxKillingSeries'))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\handofdeathachievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:56:33 Støední Evropa (bìžný èas)

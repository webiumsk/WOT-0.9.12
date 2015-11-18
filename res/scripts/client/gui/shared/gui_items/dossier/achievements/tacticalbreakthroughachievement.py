# 2015.11.18 11:56:37 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/TacticalBreakthroughAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SeriesAchievement

class TacticalBreakthroughAchievement(SeriesAchievement):

    def __init__(self, dossier, value = None):
        super(TacticalBreakthroughAchievement, self).__init__('tacticalBreakthrough', _AB.SINGLE, dossier, value)

    def _getCounterRecordNames(self):
        return ((_AB.TEAM_7X7, 'tacticalBreakthroughSeries'), (_AB.TEAM_7X7, 'maxTacticalBreakthroughSeries'))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\tacticalbreakthroughachievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:56:37 Støední Evropa (bìžný èas)

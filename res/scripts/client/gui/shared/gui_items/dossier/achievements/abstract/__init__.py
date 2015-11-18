# 2015.11.18 11:56:40 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/abstract/__init__.py
from mixins import Deprecated
from mixins import Quest
from mixins import HasVehiclesList as _HasVehiclesList
from ClassProgressAchievement import ClassProgressAchievement
from HistoricalAchievement import HistoricalAchievement
from NationSpecificAchievement import NationSpecificAchievement
from RareAchievement import RareAchievement
from RegularAchievement import RegularAchievement
from SeriesAchievement import SeriesAchievement
from SimpleProgressAchievement import SimpleProgressAchievement

class DeprecatedAchievement(Deprecated, RegularAchievement):
    pass


class QuestAchievement(Quest, RegularAchievement):
    pass


def isRareAchievement(achievement):
    return isinstance(achievement, RareAchievement)


def isSeriesAchievement(achievement):
    return isinstance(achievement, SeriesAchievement)


def achievementHasVehiclesList(achievement):
    return isinstance(achievement, _HasVehiclesList)


def getCompletedPotapovQuestsCount(seasonID, vehClasses):
    from gui.server_events import g_eventsCache

    def _filter(quest):
        return quest.isFullCompleted() and len(vehClasses & quest.getVehicleClasses())

    result = 0
    for tile in g_eventsCache.random.getSeasons()[seasonID].getTiles().itervalues():
        result += len(tile.getQuestsByFilter(_filter))

    return result


__all__ = ['ClassProgressAchievement',
 'HistoricalAchievement',
 'NationSpecificAchievement',
 'RareAchievement',
 'RegularAchievement',
 'SeriesAchievement',
 'SimpleProgressAchievement',
 'DeprecatedAchievement',
 'QuestAchievement',
 'isRareAchievement',
 'isSeriesAchievement',
 'achievementHasVehiclesList']
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\abstract\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:56:40 Støední Evropa (bìžný èas)

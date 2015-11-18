# 2015.11.18 11:52:01 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/battle_results/abstract.py
import weakref
from shared_utils import makeTupleByDict
from gui.battle_results import stats, items

class BattleResults(object):

    def __init__(self, results, dp):
        self._dp = weakref.proxy(dp)
        self._common = makeTupleByDict(stats.CommonInfo, results['common'])
        self._personal = makeTupleByDict(stats.PersonalInfo, results['personal'].values()[0])

    def clear(self):
        pass

    @property
    def common(self):
        return self._common

    @property
    def personal(self):
        return self._personal

    def isWin(self):
        return self._common.winnerTeam == self._personal.team

    def requestTeamInfo(self, isMy, callback):
        callback(isMy, items.TeamInfo())

    def updateViewData(self, viewData):
        pass
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\battle_results\abstract.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:01 St�edn� Evropa (b�n� �as)

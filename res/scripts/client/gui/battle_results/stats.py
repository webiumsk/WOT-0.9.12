# 2015.11.18 11:52:02 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/battle_results/stats.py
from collections import namedtuple
from constants import FINISH_REASON, ARENA_GUI_TYPE, ARENA_BONUS_TYPE
_CommonInfo = namedtuple('_CommonInfo', ['finishReason',
 'guiType',
 'arenaCreateTime',
 'duration',
 'arenaTypeID',
 'winnerTeam',
 'vehLockMode',
 'bonusType',
 'division'])
_CommonInfo.__new__.__defaults__ = (FINISH_REASON.UNKNOWN,
 ARENA_GUI_TYPE.UNKNOWN,
 0,
 0,
 0,
 0,
 0,
 ARENA_BONUS_TYPE.UNKNOWN,
 None)
_PersonalInfo = namedtuple('_PersonalInfo', ['team'])
_PersonalInfo.__new__.__defaults__ = (0,)

class CommonInfo(_CommonInfo):
    pass


class PersonalInfo(_PersonalInfo):
    pass
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\battle_results\stats.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:02 St�edn� Evropa (b�n� �as)

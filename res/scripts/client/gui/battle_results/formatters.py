# 2015.11.18 11:52:01 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/battle_results/formatters.py
from helpers import i18n
from gui.clubs.formatters import getDivisionString, getLeagueString, getDivisionWithinLeague
_UNKNOWN_TEAMMATE_NAME = i18n.makeString('#battle_results:players/teammate/unknown')
_UNKNOWN_ENEMY_NAME = i18n.makeString('#battle_results:players/enemy/unknown')

def getUnknownPlayerName(isEnemy = False):
    if isEnemy:
        return _UNKNOWN_ENEMY_NAME
    else:
        return _UNKNOWN_TEAMMATE_NAME


def getAnimationLeavesIcon(league, division):
    return '../maps/icons/library/cybersport/animation/leaves/%s%s.png' % (getLeagueString(league), getDivisionString(division).lower())


def getAnimationRibbonIcon(league, division):
    return '../maps/icons/library/cybersport/animation/bg/%s%s.png' % (getLeagueString(league), getDivisionString(division).lower())


def getAnimationDivisionIcon(league, division):
    return '../maps/icons/library/cybersport/animation/division/%s%s.png' % (getLeagueString(league), getDivisionString(division).lower())


def getAnimationLogoIcon(league, division):
    if getDivisionWithinLeague(division) == 0:
        return '../maps/icons/library/cybersport/animation/logo/%s.png' % getLeagueString(league)
    else:
        return None
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\battle_results\formatters.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:01 St�edn� Evropa (b�n� �as)

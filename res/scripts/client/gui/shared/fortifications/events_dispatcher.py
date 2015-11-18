# 2015.11.18 11:56:21 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/shared/fortifications/events_dispatcher.py
from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
from gui.Scaleform.genConsts.FORTIFICATION_ALIASES import FORTIFICATION_ALIASES

def showFortBattleRoomWindow():
    g_eventBus.handleEvent(events.LoadViewEvent(FORTIFICATION_ALIASES.FORT_BATTLE_ROOM_WINDOW_ALIAS), EVENT_BUS_SCOPE.LOBBY)


def showBattleConsumesIntro():
    g_eventBus.handleEvent(events.LoadViewEvent(FORTIFICATION_ALIASES.FORT_COMBAT_RESERVES_INTRO_ALIAS), EVENT_BUS_SCOPE.LOBBY)


def loadFortView():
    g_eventBus.handleEvent(events.LoadViewEvent(FORTIFICATION_ALIASES.FORTIFICATIONS_VIEW_ALIAS), EVENT_BUS_SCOPE.LOBBY)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\fortifications\events_dispatcher.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:56:21 Støední Evropa (bìžný èas)

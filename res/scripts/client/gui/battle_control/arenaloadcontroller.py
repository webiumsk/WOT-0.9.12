# 2015.11.18 11:51:49 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/battle_control/ArenaLoadController.py
import BigWorld
from gui import game_control
from gui.app_loader import g_appLoader
from gui.battle_control.arena_info import getArenaGuiType
from gui.battle_control.arena_info.interfaces import IArenaLoadController

class ArenaLoadController(IArenaLoadController):

    def __init__(self, isMultiTeam = False):
        super(ArenaLoadController, self).__init__()
        self.__isMultiTeam = isMultiTeam

    def spaceLoadStarted(self):
        game_control.g_instance.gameSession.incBattlesCounter()
        g_appLoader.showBattleLoading(arenaGuiType=getArenaGuiType(), isMultiTeam=self.__isMultiTeam)
        BigWorld.wg_setReducedFpsMode(True)

    def spaceLoadCompleted(self):
        BigWorld.player().onSpaceLoaded()

    def arenaLoadCompleted(self):
        BigWorld.wg_setReducedFpsMode(False)
        from messenger import MessengerEntry
        MessengerEntry.g_instance.onAvatarShowGUI()
        g_appLoader.showBattle()
        BigWorld.wg_clearTextureReuseList()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\battle_control\arenaloadcontroller.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:51:49 St�edn� Evropa (b�n� �as)

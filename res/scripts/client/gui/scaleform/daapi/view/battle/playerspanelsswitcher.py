# 2015.11.18 11:53:11 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/PlayersPanelsSwitcher.py
from account_helpers.settings_core import g_settingsCore
from debug_utils import LOG_DEBUG
from gui.battle_control.battle_period_ctrl import IPlayersPanelsSwitcher

class PlayersPanelsSwitcher(IPlayersPanelsSwitcher):

    def __init__(self, ui = None):
        super(PlayersPanelsSwitcher, self).__init__()
        self.__ui = ui
        self.__ui.addExternalCallback('Battle.playersPanelStateChange', self.__onPlayersPanelStateChange)
        self.__isChanged = False

    def destroy(self):
        if self.__ui:
            self.__ui.removeExternalCallback('Battle.playersPanelStateChange')
        self.__ui = None
        return

    def __del__(self):
        LOG_DEBUG('PlayersPanelsSwitcher is deleted')

    def setInitialMode(self):
        if not self.__isChanged:
            self.__call('setState', [g_settingsCore.getSetting('ppState')])
            self.__ui.invalidateGUI()

    def setLargeMode(self):
        self.__call('setState', ['large'])

    def __onPlayersPanelStateChange(self, _, state):
        self.__isChanged = True
        g_settingsCore.applySetting('ppState', state)

    def __call(self, funcName, args = None):
        if self.__ui:
            self.__ui.call('players_panel.{0}'.format(funcName), args)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\battle\playerspanelsswitcher.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:53:11 St�edn� Evropa (b�n� �as)

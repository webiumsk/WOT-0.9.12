# 2015.11.18 11:53:14 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/messages/VehicleErrorMessages.py
from debug_utils import LOG_DEBUG
from gui.Scaleform.daapi.view.battle.messages.FadingMessages import FadingMessages
from gui.battle_control import g_sessionProvider

class VehicleErrorMessages(FadingMessages):

    def __init__(self, parentUI):
        super(VehicleErrorMessages, self).__init__(parentUI, 'VehicleErrorsPanel', 'gui/vehicle_errors_panel.xml')

    def __del__(self):
        LOG_DEBUG('VehicleErrorMessages panel is deleted')

    def _addGameListeners(self):
        super(VehicleErrorMessages, self)._addGameListeners()
        ctrl = g_sessionProvider.getBattleMessagesCtrl()
        if ctrl:
            ctrl.onShowVehicleErrorByKey += self.__onShowVehicleErrorByKey

    def _removeGameListeners(self):
        ctrl = g_sessionProvider.getBattleMessagesCtrl()
        if ctrl:
            ctrl.onShowVehicleErrorByKey -= self.__onShowVehicleErrorByKey
        super(VehicleErrorMessages, self)._removeGameListeners()

    def __onShowVehicleErrorByKey(self, key, args = None, extra = None):
        self.showMessage(key, args, extra)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\battle\messages\vehicleerrormessages.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:53:14 Støední Evropa (bìžný èas)

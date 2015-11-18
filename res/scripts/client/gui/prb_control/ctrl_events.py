# 2015.11.18 11:52:34 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/prb_control/ctrl_events.py
import Event

class _PrbCtrlEvents(object):
    __slots__ = ('__eManager', 'onPrebattleIntroModeJoined', 'onPrebattleIntroModeLeft', 'onUnitIntroModeLeft', 'onPrebattleInited', 'onUnitIntroModeJoined', 'onPreQueueFunctionalCreated', 'onPreQueueFunctionalDestroyed', 'onPreQueueFunctionalChanged', 'onVehicleClientStateChanged')

    def __init__(self):
        super(_PrbCtrlEvents, self).__init__()
        self.__eManager = Event.EventManager()
        self.onPrebattleIntroModeJoined = Event.Event(self.__eManager)
        self.onPrebattleIntroModeLeft = Event.Event(self.__eManager)
        self.onUnitIntroModeLeft = Event.Event(self.__eManager)
        self.onPrebattleInited = Event.Event(self.__eManager)
        self.onUnitIntroModeJoined = Event.Event(self.__eManager)
        self.onUnitIntroModeLeft = Event.Event(self.__eManager)
        self.onPreQueueFunctionalCreated = Event.Event(self.__eManager)
        self.onPreQueueFunctionalDestroyed = Event.Event(self.__eManager)
        self.onPreQueueFunctionalChanged = Event.Event(self.__eManager)
        self.onVehicleClientStateChanged = Event.Event(self.__eManager)

    def clear(self):
        self.__eManager.clear()


g_prbCtrlEvents = _PrbCtrlEvents()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\prb_control\ctrl_events.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:34 St�edn� Evropa (b�n� �as)

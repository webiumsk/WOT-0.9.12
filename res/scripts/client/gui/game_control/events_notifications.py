# 2015.11.18 11:52:22 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/game_control/events_notifications.py
from collections import namedtuple
import BigWorld
import Event
from debug_utils import LOG_DEBUG
from PlayerEvents import g_playerEvents
from helpers import getLocalizedData
from gui.game_control.controllers import Controller

class EventsNotificationsController(Controller):

    def __init__(self, proxy):
        super(EventsNotificationsController, self).__init__(proxy)
        self.__eventMgr = Event.EventManager()
        self.onEventNotificationsChanged = Event.Event(self.__eventMgr)

    def fini(self):
        self.__stop()
        self.__eventMgr = None
        super(EventsNotificationsController, self).fini()
        return

    def onLobbyInited(self, event):
        g_playerEvents.onEventNotificationsChanged += self.__onEventNotification

    def onAvatarBecomePlayer(self):
        self.__stop()

    def onDisconnected(self):
        self.__stop()

    def getEventsNotifications(self, filterFunc = None):
        return filter(filterFunc or (lambda a: True), map(EventNotification.make, BigWorld.player().eventNotifications))

    def __stop(self):
        self.__eventMgr.clear()
        g_playerEvents.onEventNotificationsChanged -= self.__onEventNotification

    def __onEventNotification(self, diff):
        added = map(EventNotification.make, diff.get('added', ()))
        removed = map(EventNotification.make, diff.get('removed', ()))
        self.onEventNotificationsChanged(added, removed)


class EventNotification(namedtuple('EventNotification', 'eventType data text')):

    @classmethod
    def default(cls):
        return cls.__new__(cls, None, None, None)

    @classmethod
    def make(cls, data):
        text = getLocalizedData(data, 'text')
        return cls.__new__(cls, data['type'], data.get('data'), text)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\game_control\events_notifications.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:22 Støední Evropa (bìžný èas)

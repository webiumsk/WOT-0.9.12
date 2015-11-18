# 2015.11.18 11:55:22 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/EventSystemEntity.py
from gui.Scaleform.framework.entities.DisposableEntity import DisposableEntity
from gui.shared import g_eventBus, EVENT_BUS_SCOPE

class EventSystemEntity(DisposableEntity):

    def fireEvent(self, event, scope = EVENT_BUS_SCOPE.DEFAULT):
        g_eventBus.handleEvent(event, scope=scope)

    def addListener(self, eventType, handler, scope = EVENT_BUS_SCOPE.DEFAULT):
        g_eventBus.addListener(eventType, handler, scope=scope)

    def removeListener(self, eventType, handler, scope = EVENT_BUS_SCOPE.DEFAULT):
        g_eventBus.removeListener(eventType, handler, scope)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\framework\entities\eventsystementity.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:55:22 Støední Evropa (bìžný èas)

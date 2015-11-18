# 2015.11.18 11:52:09 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/clans/subscriptions.py
from gui.clans.interfaces import IClanListener
from gui.shared.utils.ListenersCollection import ListenersCollection

class ClansListeners(ListenersCollection):

    def __init__(self):
        super(ClansListeners, self).__init__()
        self._setListenerClass(IClanListener)

    def notify(self, eventType, *args):
        self._invokeListeners(eventType, *args)

    def clear(self):
        while len(self._listeners):
            self._listeners.pop()

    def addListener(self, listener):
        if not self.hasListener(listener):
            super(ClansListeners, self).addListener(listener)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\clans\subscriptions.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:09 Støední Evropa (bìžný èas)

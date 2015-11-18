# 2015.11.18 11:58:11 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/notification/NotificationLayoutView.py
from notification.BaseNotificationView import BaseNotificationView

class NotificationLayoutView(BaseNotificationView):

    def __init__(self, model = None):
        super(NotificationLayoutView, self).__init__(model)

    def setModel(self, value):
        if self._model is not None:
            self._model.onLayoutSettingsChanged -= self._onLayoutSettingsChanged
        BaseNotificationView.setModel(self, value)
        if self._model is not None:
            self._model.onLayoutSettingsChanged += self._onLayoutSettingsChanged
        return

    def _onLayoutSettingsChanged(self, settings):
        pass

    def cleanUp(self):
        self._model.onLayoutSettingsChanged -= self._onLayoutSettingsChanged
        self.model = None
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\notification\notificationlayoutview.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:58:11 Støední Evropa (bìžný èas)

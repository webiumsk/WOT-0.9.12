# 2015.11.18 11:54:19 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/messengerBar/NotificationListButton.py
from gui.Scaleform.daapi.view.meta.NotificationListButtonMeta import NotificationListButtonMeta
from notification import NotificationMVC

class NotificationListButton(NotificationListButtonMeta):

    def __init__(self):
        super(NotificationListButton, self).__init__()
        NotificationMVC.g_instance.getModel().onNotifiedMessagesCountChanged += self.__notifiedMessagesCountChangeHandler

    def _populate(self):
        super(NotificationListButton, self)._populate()
        self.as_setStateS(NotificationMVC.g_instance.getModel().getNotifiedMessagesCount() > 0)

    def __notifiedMessagesCountChangeHandler(self, notifyMessagesCount):
        self.as_setStateS(notifyMessagesCount > 0)

    def handleClick(self):
        NotificationMVC.g_instance.getModel().setListDisplayState()

    def _dispose(self):
        model = NotificationMVC.g_instance.getModel()
        if model:
            model.onNotifiedMessagesCountChanged -= self.__notifiedMessagesCountChangeHandler
        super(NotificationListButton, self)._dispose()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\messengerbar\notificationlistbutton.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:54:19 Støední Evropa (bìžný èas)

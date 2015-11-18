# 2015.11.18 11:58:09 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/notification/AlertController.py
from gui import DialogsInterface
from gui.Scaleform.daapi.view.dialogs.SystemMessageMeta import SystemMessageMeta
from notification.BaseMessagesController import BaseMessagesController
import Event
from adisp import process

class AlertController(BaseMessagesController):

    def __init__(self, model):
        BaseMessagesController.__init__(self, model)
        self.__actualDisplayingAlerts = 0
        self.onAllAlertsClosed = Event.Event()

    @process
    def showAlertMessage(self, notification):
        self.__actualDisplayingAlerts += 1
        yield DialogsInterface.showDialog(SystemMessageMeta(notification))
        self.__actualDisplayingAlerts -= 1
        if self.__actualDisplayingAlerts == 0:
            self.onAllAlertsClosed()

    def isAlertShowing(self):
        return self.__actualDisplayingAlerts > 0
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\notification\alertcontroller.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:58:09 Støední Evropa (bìžný èas)

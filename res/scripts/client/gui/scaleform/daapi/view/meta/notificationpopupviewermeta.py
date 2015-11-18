# 2015.11.18 11:55:07 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/NotificationPopUpViewerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class NotificationPopUpViewerMeta(BaseDAAPIComponent):

    def setListClear(self):
        self._printOverrideError('setListClear')

    def onMessageHided(self, byTimeout, wasNotified):
        self._printOverrideError('onMessageHided')

    def onClickAction(self, typeID, entityID, action):
        self._printOverrideError('onClickAction')

    def getMessageActualTime(self, msTime):
        self._printOverrideError('getMessageActualTime')

    def as_hasPopUpIndexS(self, typeID, entityID):
        if self._isDAAPIInited():
            return self.flashObject.as_hasPopUpIndex(typeID, entityID)

    def as_appendMessageS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_appendMessage(data)

    def as_updateMessageS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateMessage(data)

    def as_removeMessageS(self, typeID, entityID):
        if self._isDAAPIInited():
            return self.flashObject.as_removeMessage(typeID, entityID)

    def as_removeAllMessagesS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_removeAllMessages()

    def as_layoutInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_layoutInfo(data)

    def as_initInfoS(self, maxMessagessCount, padding):
        if self._isDAAPIInited():
            return self.flashObject.as_initInfo(maxMessagessCount, padding)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\notificationpopupviewermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:55:07 St�edn� Evropa (b�n� �as)

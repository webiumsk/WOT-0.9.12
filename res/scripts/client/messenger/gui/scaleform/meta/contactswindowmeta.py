# 2015.11.18 11:57:41 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/ContactsWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ContactsWindowMeta(AbstractWindowView):

    def searchContact(self, criteria):
        self._printOverrideError('searchContact')

    def addToFriends(self, uid, name):
        self._printOverrideError('addToFriends')

    def addToIgnored(self, uid, name):
        self._printOverrideError('addToIgnored')

    def isEnabledInRoaming(self, uid):
        self._printOverrideError('isEnabledInRoaming')

    def as_getFriendsDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getFriendsDP()

    def as_getClanDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getClanDP()

    def as_getIgnoredDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getIgnoredDP()

    def as_getMutedDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getMutedDP()

    def as_getSearchDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getSearchDP()

    def as_setSearchResultTextS(self, message):
        if self._isDAAPIInited():
            return self.flashObject.as_setSearchResultText(message)

    def as_frozenSearchActionS(self, flag):
        if self._isDAAPIInited():
            return self.flashObject.as_frozenSearchAction(flag)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\gui\scaleform\meta\contactswindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:57:41 Støední Evropa (bìžný èas)

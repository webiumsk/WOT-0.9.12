# 2015.11.18 11:55:10 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ProfileWindowMeta(AbstractWindowView):

    def userAddFriend(self):
        self._printOverrideError('userAddFriend')

    def userAddToClan(self):
        self._printOverrideError('userAddToClan')

    def userSetIgnored(self):
        self._printOverrideError('userSetIgnored')

    def userCreatePrivateChannel(self):
        self._printOverrideError('userCreatePrivateChannel')

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_addFriendAvailableS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_addFriendAvailable(value)

    def as_addToClanAvailableS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_addToClanAvailable(value)

    def as_addToClanVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_addToClanVisible(value)

    def as_setIgnoredAvailableS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setIgnoredAvailable(value)

    def as_setCreateChannelAvailableS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCreateChannelAvailable(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\profilewindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:55:10 St�edn� Evropa (b�n� �as)

# 2015.11.18 11:55:09 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileFormationsPageMeta.py
from gui.Scaleform.daapi.view.lobby.profile.ProfileSection import ProfileSection

class ProfileFormationsPageMeta(ProfileSection):

    def showFort(self):
        self._printOverrideError('showFort')

    def searchStaticTeams(self):
        self._printOverrideError('searchStaticTeams')

    def createFort(self):
        self._printOverrideError('createFort')

    def showTeam(self, teamId):
        self._printOverrideError('showTeam')

    def onClanLinkNavigate(self, code):
        self._printOverrideError('onClanLinkNavigate')

    def as_setClanInfoS(self, clanInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_setClanInfo(clanInfo)

    def as_setClubInfoS(self, clubInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_setClubInfo(clubInfo)

    def as_setFortInfoS(self, fortInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_setFortInfo(fortInfo)

    def as_setClubHistoryS(self, history):
        if self._isDAAPIInited():
            return self.flashObject.as_setClubHistory(history)

    def as_setClanEmblemS(self, clanIcon):
        if self._isDAAPIInited():
            return self.flashObject.as_setClanEmblem(clanIcon)

    def as_setClubEmblemS(self, clubIcon):
        if self._isDAAPIInited():
            return self.flashObject.as_setClubEmblem(clubIcon)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\profileformationspagemeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:55:09 St�edn� Evropa (b�n� �as)

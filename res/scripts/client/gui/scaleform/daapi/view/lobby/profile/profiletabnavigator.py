# 2015.11.18 11:54:26 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileTabNavigator.py
from gui.Scaleform.daapi.view.lobby.profile.ProfileSection import ProfileSection
from gui.Scaleform.daapi.view.meta.ProfileTabNavigatorMeta import ProfileTabNavigatorMeta

class ProfileTabNavigator(ProfileTabNavigatorMeta):

    def __init__(self, *args):
        ProfileTabNavigatorMeta.__init__(self)
        self.__userName = args[0]
        self.__userID = args[1]
        self.__databaseID = args[2]
        self.__navigatorOwnInitInfo = args[3]
        self.__selectedData = None
        if len(args) > 4 and args[4]:
            self.__selectedData = args[4]
        return

    def invokeUpdate(self):
        for component in self.components.itervalues():
            if isinstance(component, ProfileSection):
                component.invokeUpdate()

    def _populate(self):
        super(ProfileTabNavigator, self)._populate()
        self.as_setInitDataS(self.__navigatorOwnInitInfo)

    def registerFlashComponent(self, component, alias, *args):
        super(ProfileTabNavigator, self).registerFlashComponent(component, alias, self.__userName, self.__userID, self.__databaseID, self.__selectedData)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\profile\profiletabnavigator.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:54:26 Støední Evropa (bìžný èas)

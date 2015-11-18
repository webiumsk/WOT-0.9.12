# 2015.11.18 11:52:27 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/login/Manager.py
import BigWorld
import constants
from gui import SystemMessages, makeHtmlString, GUI_SETTINGS
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES
from gui.LobbyContext import g_lobbyContext
from ConnectionManager import connectionManager, CONNECTION_METHOD
from Preferences import Preferences
from Servers import Servers, DevelopmentServers
from helpers.i18n import makeString as _ms

class Manager(object):

    def __init__(self):
        self._preferences = None
        self.__servers = None
        return

    def init(self):
        self._preferences = Preferences()
        if constants.IS_DEVELOPMENT:
            self.__servers = DevelopmentServers(self._preferences)
        else:
            self.__servers = Servers(self._preferences)
        connectionManager.onLoggedOn += self._onLoggedOn

    def fini(self):
        connectionManager.onLoggedOn -= self._onLoggedOn
        self._preferences = None
        self.__servers.fini()
        self.__servers = None
        return

    def initiateLogin(self, email, password, serverName, isSocialToken2Login, rememberUser):
        authMethod = CONNECTION_METHOD.BASIC
        self._preferences['session'] = BigWorld.wg_cpsalt(self._preferences['session'])
        self._preferences['password_length'] = len(password)
        self._preferences['remember_user'] = rememberUser
        self._preferences['login'] = email
        self._preferences['server_name'] = serverName
        loginParams = {'login': self._preferences['login'],
         'session': self._preferences['session'],
         'temporary': str(int(not rememberUser)),
         'auth_method': authMethod}
        if isSocialToken2Login or self._preferences['token2']:
            loginParams['auth_method'] = CONNECTION_METHOD.TOKEN2
            loginParams['token2'] = self._preferences['token2']
        if isSocialToken2Login:
            self._preferences['login_type'] = self._preferences['login_type']
        else:
            self._preferences['login_type'] = 'credentials'
        connectionManager.initiateConnection(loginParams, password, serverName)

    def getPreference(self, key):
        return self._preferences[key]

    def clearPreferences(self):
        self._preferences.clear()

    def clearToken2Preference(self):
        self._preferences['token2'] = ''

    def writePreferences(self):
        self._preferences.writeLoginInfo()

    @property
    def servers(self):
        return self.__servers

    def _onLoggedOn(self, responseData):
        name = responseData.get('name', 'UNKNOWN')
        token2 = responseData.get('token2', '')
        g_lobbyContext.setCredentials(name, token2)
        if self._preferences['remember_user']:
            self._preferences['name'] = name
            self._preferences['token2'] = token2
            if not constants.IS_DEVELOPMENT and 'server_name' in self._preferences:
                del self._preferences['server_name']
        else:
            email = self._preferences['login']
            serverName = self._preferences['server_name']
            session = self._preferences['session']
            self._preferences.clear()
            if not constants.IS_SINGAPORE and not GUI_SETTINGS.igrCredentialsReset:
                self._preferences['login'] = email
            if constants.IS_DEVELOPMENT:
                self._preferences['server_name'] = serverName
            self._preferences['session'] = session
        self._preferences.writeLoginInfo()
        self._showSecurityMessage(responseData)

    def _showSecurityMessage(self, responseData):
        securityWarningType = responseData.get('security_msg')
        if securityWarningType is not None:
            securityLink = ''
            if not GUI_SETTINGS.isEmpty('securitySettingsURL'):
                securityLink = makeHtmlString('html_templates:lobby/system_messages', 'link', {'text': _ms(SYSTEM_MESSAGES.SECURITYMESSAGE_CHANGE_SETINGS),
                 'linkType': 'securityLink'})
            SystemMessages.pushI18nMessage('#system_messages:securityMessage/%s' % securityWarningType, type=SystemMessages.SM_TYPE.Warning, link=securityLink)
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\login\manager.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:27 St�edn� Evropa (b�n� �as)

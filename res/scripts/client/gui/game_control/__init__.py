# 2015.11.18 11:52:26 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/game_control/__init__.py
import constants
from gui.game_control.BoostersController import BoostersController
from gui.game_control.ExternalLinksHandler import ExternalLinksHandler
from gui.game_control.InternalLinksHandler import InternalLinksHandler
from gui.shared import g_eventBus, events
from gui.game_control.BrowserController import BrowserController
from gui.game_control.PromoController import PromoController
from gui.game_control.RefSystem import RefSystem
from gui.game_control.RentalsController import RentalsController
from gui.game_control.controllers import ControllersCollection
from gui.game_control.events_notifications import EventsNotificationsController
from gui.game_control.gc_constants import CONTROLLER
from gui.game_control.relogin_controller import ReloginController
from gui.game_control.AOGAS import AOGASController
from gui.game_control.captcha_control import CaptchaController
from gui.game_control.GameSessionController import GameSessionController
from gui.game_control.IGR import IGRController
from gui.game_control.wallet import WalletController
from gui.game_control.NotifyController import NotifyController
from gui.game_control.SoundEventChecker import SoundEventChecker
from gui.game_control.ServerStats import ServerStats
from gui.game_control.ChinaController import ChinaController
from gui.game_control.AwardController import AwardController
from gui.game_control.fallout_controller import FalloutController

class _GameControllers(ControllersCollection):

    def __init__(self):
        super(_GameControllers, self).__init__({CONTROLLER.RELOGIN: ReloginController,
         CONTROLLER.AOGAS: AOGASController,
         CONTROLLER.GAME_SESSION: GameSessionController,
         CONTROLLER.CAPTCHA: CaptchaController,
         CONTROLLER.RENTALS: RentalsController,
         CONTROLLER.IGR: IGRController,
         CONTROLLER.WALLET: WalletController,
         CONTROLLER.NOTIFIER: NotifyController,
         CONTROLLER.LINKS: ExternalLinksHandler,
         CONTROLLER.INTERNAL_LINKS: InternalLinksHandler,
         CONTROLLER.SOUND_CHECKER: SoundEventChecker,
         CONTROLLER.SERVER_STATS: ServerStats,
         CONTROLLER.REF_SYSTEM: RefSystem,
         CONTROLLER.BROWSER: BrowserController,
         CONTROLLER.PROMO: PromoController,
         CONTROLLER.EVENTS_NOTIFICATION: EventsNotificationsController,
         CONTROLLER.AWARD: AwardController,
         CONTROLLER.BOOSTERS: BoostersController,
         CONTROLLER.FALLOUT: FalloutController})
        if constants.IS_CHINA:
            self._addController(CONTROLLER.CHINA, ChinaController)
        self.__collectUiStats = True
        self.__logUXEvents = False

    def init(self):
        super(_GameControllers, self).init()
        g_eventBus.addListener(events.GUICommonEvent.LOBBY_VIEW_LOADED, self.onLobbyInited)

    def fini(self):
        g_eventBus.removeListener(events.GUICommonEvent.LOBBY_VIEW_LOADED, self.onLobbyInited)
        super(_GameControllers, self).fini()

    @property
    def collectUiStats(self):
        return self.__collectUiStats

    @property
    def needLogUXEvents(self):
        return self.__logUXEvents

    def onAccountShowGUI(self, ctx):
        self.onLobbyStarted(ctx)
        self.__collectUiStats = ctx.get('collectUiStats', True)
        self.__logUXEvents = ctx.get('logUXEvents', False)


g_instance = _GameControllers()

def getEventsNotificationCtrl():
    return _getController(CONTROLLER.EVENTS_NOTIFICATION)


def getBrowserCtrl():
    return _getController(CONTROLLER.BROWSER)


def getChinaCtrl():
    raise constants.IS_CHINA or AssertionError('China controller only available if IS_CHINA = True')
    return _getController(CONTROLLER.CHINA)


def getIGRCtrl():
    return _getController(CONTROLLER.IGR)


def getRefSysCtrl():
    return _getController(CONTROLLER.REF_SYSTEM)


def getRoamingCtrl():
    return _getController(CONTROLLER.RELOGIN)


def getWalletCtrl():
    return _getController(CONTROLLER.WALLET)


def getFalloutCtrl():
    return _getController(CONTROLLER.FALLOUT)


def _getController(controller):
    return g_instance.getController(controller)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\game_control\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:26 St�edn� Evropa (b�n� �as)

# 2015.11.18 11:52:23 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/game_control/gc_constants.py
from shared_utils import CONST_CONTAINER

class CONTROLLER(CONST_CONTAINER):
    RELOGIN = 'relogin'
    AOGAS = 'aogas'
    GAME_SESSION = 'gameSession'
    CAPTCHA = 'captcha'
    RENTALS = 'rentals'
    IGR = 'igr'
    WALLET = 'wallet'
    LANGUAGE = 'language'
    NOTIFIER = 'notifier'
    LINKS = 'links'
    INTERNAL_LINKS = 'internalLinks'
    SOUND_CHECKER = 'soundChecker'
    SERVER_STATS = 'serverStats'
    REF_SYSTEM = 'refSystem'
    BROWSER = 'browser'
    PROMO = 'promo'
    EVENTS_NOTIFICATION = 'eventsNotifications'
    CHINA = 'china'
    AWARD = 'award'
    BOOSTERS = 'boosters'
    FALLOUT = 'fallout'


class BROWSER(CONST_CONTAINER):
    CHINA_BROWSER_COUNT = 999
    SIZE = (990, 550)
    BACKGROUND = 'file:///gui/maps/bg.png'
    PROMO_SIZE = (780, 470)
    CLUB_SIZE = (780, 470)
    VIDEO_SIZE = (864, 486)
    PROMO_BACKGROUND = 'file:///gui/maps/promo_bg.png'


class PROMO(CONST_CONTAINER):

    class TEMPLATE(CONST_CONTAINER):
        PATCH = 'promo_patchnote'
        ACTION = 'promo_action'
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\game_control\gc_constants.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:23 Støední Evropa (bìžný èas)

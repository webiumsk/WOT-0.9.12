# 2015.11.18 11:58:13 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/notification/settings.py
LIST_SCROLL_STEP_FACTOR = 10
DEF_ICON_PATH = '../maps/icons/library/{0:>s}-1.png'

class NOTIFICATION_STATE(object):
    POPUPS = 0
    LIST = 1


class NOTIFICATION_TYPE(object):
    UNDEFINED = 0
    MESSAGE = 1
    INVITE = 2
    FRIENDSHIP_RQ = 3
    WGNC_POP_UP = 4
    CLUB_INVITE = 5
    CLUB_APPS = 6
    CLAN_INVITES = 7
    CLAN_APPS = 8
    CLAN_APP_ACTION = 9
    CLAN_INVITE_ACTION = 10
    CLAN_INVITE = 11
    CLAN_APP = 12
    RANGE = (MESSAGE,
     INVITE,
     FRIENDSHIP_RQ,
     WGNC_POP_UP,
     CLUB_INVITE,
     CLUB_APPS,
     CLAN_INVITES,
     CLAN_APPS,
     CLAN_APP_ACTION,
     CLAN_INVITE_ACTION,
     CLAN_INVITE,
     CLAN_APP)


ITEMS_MAX_LENGTHS = {NOTIFICATION_TYPE.MESSAGE: 250,
 NOTIFICATION_TYPE.INVITE: 100,
 NOTIFICATION_TYPE.FRIENDSHIP_RQ: 100,
 NOTIFICATION_TYPE.CLUB_INVITE: 100,
 NOTIFICATION_TYPE.CLUB_APPS: 1,
 NOTIFICATION_TYPE.WGNC_POP_UP: 500,
 NOTIFICATION_TYPE.CLAN_APPS: 1,
 NOTIFICATION_TYPE.CLAN_INVITES: 1,
 NOTIFICATION_TYPE.CLAN_APP_ACTION: 500,
 NOTIFICATION_TYPE.CLAN_INVITE_ACTION: 500,
 NOTIFICATION_TYPE.CLAN_INVITE: 500,
 NOTIFICATION_TYPE.CLAN_APP: 500}

class NOTIFICATION_BUTTON_STATE(object):
    HIDDEN = 0
    VISIBLE = 1
    ENABLED = 2
    DEFAULT = VISIBLE | ENABLED


class LAYOUT_PADDING(object):
    HANGAR = (4, 235)
    OTHER = (0, 35)
    LIST = (45, 34)
    CUSTOMIZATION = (4, 210)


def makePathToIcon(iconName):
    result = ''
    if iconName and len(iconName):
        result = DEF_ICON_PATH.format(iconName)
    return result
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\notification\settings.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:58:13 St�edn� Evropa (b�n� �as)

# 2015.11.18 11:52:08 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/clans/settings.py
import re
from adisp import async
from collections import namedtuple
from constants import CLAN_MEMBER_FLAGS
from gui.Scaleform.daapi.view.dialogs import I18nConfirmDialogMeta
from gui.Scaleform.locale.DIALOGS import DIALOGS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.shared.formatters import icons, text_styles
from shared_utils import CONST_CONTAINER
from helpers import i18n
DEFAULT_COOLDOWN = 1.0
SEND_INVITES_COOLDOWN = 5.0
MAX_ACCOUNT_APPLICATIONS_COUNT = 100
MAX_CLAN_INVITES_COUNT = 100
MAX_CLAN_MEMBERS_COUNT = 100
COUNT_THRESHOLD = 2000
PERSONAL_INVITES_COUNT_THRESHOLD = 500
DATA_UNAVAILABLE_PLACEHOLDER = '--'
ACTIVE_INVITE_LIFE_TIME = 259200
INVITE_LIMITS_LIFE_TIME = 300
CLAN_DOSSIER_LIFE_TIME = 3600
DEFAULT_EMBLEM_PATH = 'gui/maps/icons/clans'
DEFAULT_EMBLEM_NAME_PREFIX = 'default_clan_icon'
NO_EMBLEM_NAME_PREFIX = 'no_clan_icon'
CLAN_MEMBERS = {CLAN_MEMBER_FLAGS.LEADER: 'leader',
 CLAN_MEMBER_FLAGS.VICE_LEADER: 'vice_leader',
 CLAN_MEMBER_FLAGS.RECRUITER: 'recruiter',
 CLAN_MEMBER_FLAGS.TREASURER: 'treasurer',
 CLAN_MEMBER_FLAGS.DIPLOMAT: 'diplomat',
 CLAN_MEMBER_FLAGS.COMMANDER: 'commander',
 CLAN_MEMBER_FLAGS.PRIVATE: 'private',
 CLAN_MEMBER_FLAGS.RECRUIT: 'recruit',
 CLAN_MEMBER_FLAGS.STAFF: 'staff',
 CLAN_MEMBER_FLAGS.JUNIOR: 'junior',
 CLAN_MEMBER_FLAGS.RESERVIST: 'reservist'}
_RE_SEARCH_CLANS = re.compile('^(\\[|\\])*[\\S]{2,}', re.IGNORECASE)

def isValidPattern(pattern):
    return pattern and _RE_SEARCH_CLANS.match(pattern)


class LOGIN_STATE(CONST_CONTAINER):
    LOGGED_OFF = 0
    LOGGING_IN = 1
    LOGGED_ON = 2

    @classmethod
    def canDoLogin(cls, state):
        return state == cls.LOGGED_OFF


class CLAN_CONTROLLER_STATES(CONST_CONTAINER):
    STATE_NOT_DEFINED = 0
    STATE_AVAILABLE = 1
    STATE_UNAVAILABLE = 2
    STATE_ROAMING = 3
    STATE_DISABLED = 4


class CLAN_INVITE_STATES(CONST_CONTAINER):
    ACTIVE = 'active'
    DECLINED = 'declined'
    DECLINED_RESENT = 'declined_resent'
    ACCEPTED = 'accepted'
    EXPIRED = 'expired'
    ERROR = 'error'
    DELETED = 'deleted'
    EXPIRED_RESENT = 'expired_resent'
    PROCESSED = (ACCEPTED, DECLINED)
    ALL = (ACTIVE,
     DECLINED,
     ACCEPTED,
     EXPIRED)

    @classmethod
    def isActive(cls, status):
        return status == cls.ACTIVE


class CLAN_APPLICATION_STATES(CONST_CONTAINER):
    ACTIVE = 'active'
    DECLINED = 'declined'
    ACCEPTED = 'accepted'
    ALL = (ACTIVE, DECLINED, ACCEPTED)


CLAN_INVITE_STATES_SORT_RULES = {CLAN_INVITE_STATES.ACTIVE: 0,
 CLAN_INVITE_STATES.ACCEPTED: 1,
 CLAN_INVITE_STATES.DECLINED: 2,
 CLAN_INVITE_STATES.DECLINED_RESENT: 2,
 CLAN_INVITE_STATES.EXPIRED: 4,
 CLAN_INVITE_STATES.EXPIRED_RESENT: 4,
 CLAN_INVITE_STATES.ERROR: 5,
 CLAN_INVITE_STATES.DELETED: 6}

class CLAN_REQUESTED_DATA_TYPE(CONST_CONTAINER):
    LOGIN = 1
    LOGOUT = 2
    CLAN_INFO = 3
    CLAN_RATINGS = 4
    CLAN_GLOBAL_MAP_STATS = 5
    CLAN_ACCOUNTS = 6
    STRONGHOLD_INFO = 7
    STRONGHOLD_STATISTICS = 8
    ACCOUNT_APPLICATIONS_COUNT = 9
    CLAN_INVITATIONS_COUNT = 10
    CLAN_MEMBERS = 11
    CLAN_MEMBERS_RATING = 12
    SEARCH_CLANS = 13
    CLAN_PROVINCES = 14
    CLAN_APPLICATIONS = 15
    CLAN_INVITES = 16
    ACCOUNT_INVITES = 17
    ACCEPT_APPLICATION = 18
    ACCEPT_INVITE = 19
    CREATE_APPLICATIONS = 20
    CREATE_INVITES = 213
    DECLINE_APPLICATION = 22
    DECLINE_INVITE = 23
    DECLINE_INVITES = 24
    GET_RECOMMENDED_CLANS = 25
    GET_ACCOUNT_APPLICATIONS = 26
    CLANS_INFO = 27
    CLAN_FAVOURITE_ATTRS = 28
    PING = 29
    CLAN_GM_FRONTS = 30


class CLIENT_CLAN_RESTRICTIONS(CONST_CONTAINER):
    NO_RESTRICTIONS = 'NO_RESTRICTIONS'
    DEFAULT = 'HAVE_NO_RIGHTS'
    OWN_CLAN = 'OWN_CLAN'
    RESYNCHRONIZE = 'RESYNCHRONIZE'
    ALREADY_IN_CLAN = 'ALREADY_IN_CLAN'
    FORBIDDEN_ACCOUNT_TYPE = 'FORBIDDEN_ACCOUNT_TYPE'
    CLAN_LEAVE_COOLDOWN = 'CLAN_LEAVE_COOLDOWN'
    CLAN_APPLICATION_ALREADY_SENT = 'CLAN_APPLICATION_ALREADY_SENT'
    CLAN_INVITE_ALREADY_RECEIVED = 'CLAN_INVITE_ALREADY_RECEIVED'
    SENT_INVITES_LIMIT_REACHED = 'SENT_INVITES_LIMIT_REACHED'
    CLAN_SEND_INVITES_LIMIT_REACHED = 'CLAN_SEND_INVITES_LIMIT_REACHED'
    CLAN_CONSCRIPTION_CLOSED = 'CLAN_CONSCRIPTION_CLOSED'
    CANT_SEE_TREASURY = 'HAVE_NO_RIGHTS_TO_SEE_TREASURY'
    CANT_HANDLE_INVITES = 'CANT_HANDLE_INVITES'
    CANT_SEND_INVITES = 'HAVE_NO_RIGHTS_TO_SEND_INVITES'
    SEARCH_PATTERN_INVALID = 'SEARCH_PATTERN_INVALID'
    CLAN_IS_FULL = 'CLAN_IS_FULL'


_RestrResult = namedtuple('_RestrResult', 'success reason')

@async
def showAcceptClanInviteDialog(clanName, clanAbbrev, callback):
    from gui import DialogsInterface
    DialogsInterface.showDialog(I18nConfirmDialogMeta('clanConfirmJoining', messageCtx={'icon': icons.makeImageTag(RES_ICONS.MAPS_ICONS_LIBRARY_ATTENTIONICON, 16, 16, -4, 0),
     'clanName': text_styles.stats(i18n.makeString(DIALOGS.CLANCONFIRMJOINING_MESSAGE_CLANNAME, clanAbbr=clanAbbrev, clanName=clanName)),
     'clanExit': text_styles.standard(i18n.makeString(DIALOGS.CLANCONFIRMJOINING_MESSAGE_CLANEXIT))}), callback)


def error(reason):
    return _RestrResult(False, reason)


def success():
    return _RestrResult(True, CLIENT_CLAN_RESTRICTIONS.NO_RESTRICTIONS)


def getDefaultEmblem16x16():
    return _getDefaultEmblemPath(16)


def getDefaultEmblem32x32():
    return _getDefaultEmblemPath(32)


def getDefaultEmblem64x64():
    return _getDefaultEmblemPath(64)


def getDefaultEmblem128x128():
    return _getDefaultEmblemPath(128)


def getDefaultEmblem256x256():
    return _getDefaultEmblemPath(256)


def getNoClanEmblem32x32():
    return _getNoClanEmblemPath(32)


def _getDefaultEmblemPath(size):
    return '%s/%s%dx%d.png' % (DEFAULT_EMBLEM_PATH,
     DEFAULT_EMBLEM_NAME_PREFIX,
     size,
     size)


def _getNoClanEmblemPath(size):
    return '%s/%s%dx%d.png' % (DEFAULT_EMBLEM_PATH,
     NO_EMBLEM_NAME_PREFIX,
     size,
     size)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\clans\settings.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:08 St�edn� Evropa (b�n� �as)

# 2015.11.18 11:58:46 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client_common/shared_utils/account_helpers/ClientInvitations.py
import operator
from functools import partial
import BigWorld
import AccountCommands
from constants import INVITATION_STATUS
from helpers.time_utils import getCurrentTimestamp
from debug_utils import LOG_DEBUG, LOG_ERROR, LOG_CURRENT_EXCEPTION

class ClientInvitations(object):

    def __init__(self, playerEvents):
        self.__proxy = None
        self.__expCbID = None
        self.__invitations = {}
        self.__playerEvents = playerEvents
        return

    def __del__(self):
        self._clearExpiryCallback()

    def getInvites(self):
        return self.__invitations

    def setProxy(self, proxy):
        self.__proxy = proxy

    def onProxyBecomePlayer(self):
        pass

    def onProxyBecomeNonPlayer(self):
        pass

    def processInvitations(self, invitations):
        LOG_DEBUG('ClientInvitations::processInvitations', invitations)
        self.__invitations.update(dict(((inv['id'], inv) for inv in invitations)))
        self._loadExpiryCallback()
        self.__playerEvents.onPrebattleInvitationsChanged(self.__invitations)

    def sendInvitation(self, accountsToInvite, comment = '', callback = None):
        if self.__playerEvents.isPlayerEntityChanging:
            return
        self.__proxy._doCmdIntArrStrArr(AccountCommands.CMD_INVITATION_SEND, accountsToInvite, [comment], callback)

    def acceptInvitation(self, invitationID, senderDBID, callback = None):
        if self.__playerEvents.isPlayerEntityChanging:
            return
        proxy = partial(self._onInvitationResponseReceived, INVITATION_STATUS.ACCEPTED, invitationID, callback)
        self.__proxy._doCmdInt3(AccountCommands.CMD_INVITATION_ACCEPT, invitationID, senderDBID, 0, proxy)

    def declineInvitation(self, invitationID, senderDBID, callback = None):
        if self.__playerEvents.isPlayerEntityChanging:
            return
        proxy = partial(self._onInvitationResponseReceived, INVITATION_STATUS.DECLINED, invitationID, callback)
        self.__proxy._doCmdInt3(AccountCommands.CMD_INVITATION_DECLINE, invitationID, senderDBID, 0, proxy)

    def _onInvitationResponseReceived(self, newStatus, invID, callback, requestID, code, errStr):
        if AccountCommands.isCodeValid(code):
            try:
                self.__invitations[invID]['status'] = newStatus
                self.__playerEvents.onPrebattleInvitationsChanged(self.__invitations)
            except KeyError:
                LOG_ERROR('Unknown invitation', self.__invitations, invID, callback, code, errStr)

        if callback is not None:
            callback(code, errStr)
        return

    def _cancelInvitations(self, predicate):
        for inv in self.__invitations.itervalues():
            if predicate(inv):
                inv['status'] = INVITATION_STATUS.ERROR

    def _loadExpiryCallback(self):
        self._clearExpiryCallback()
        if len(self.__invitations):
            invite = min(self.__invitations.values(), key=operator.itemgetter('expiresAt'))
            if invite:
                expTime = max(invite['expiresAt'] - getCurrentTimestamp(), 0.0)
                self.__expCbID = BigWorld.callback(expTime, partial(self.__onInviteExpired, invite))
                LOG_DEBUG('Invite expiration callback has been loaded', invite['id'], expTime)

    def _clearExpiryCallback(self):
        if self.__expCbID is not None:
            BigWorld.cancelCallback(self.__expCbID)
            self.__expCbID = None
        return

    def __onInviteExpired(self, invite):
        try:
            del self.__invitations[invite['id']]
            self.__playerEvents.onPrebattleInvitationsChanged(self.__invitations)
        except KeyError:
            LOG_ERROR('There is error while removing expired invite')
            LOG_CURRENT_EXCEPTION()

        self._loadExpiryCallback()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client_common\shared_utils\account_helpers\clientinvitations.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:58:47 St�edn� Evropa (b�n� �as)

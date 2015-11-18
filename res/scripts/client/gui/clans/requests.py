# 2015.11.18 11:52:07 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/clans/requests.py
from functools import partial
import types
import weakref
from debug_utils import LOG_WARNING, LOG_DEBUG
from gui.clans.contexts import GetFrontsCtx
from shared_utils import makeTupleByDict
from client_request_lib.exceptions import ResponseCodes
from gui.clans import formatters as clan_fmts, contexts, items
from gui.clans.settings import DEFAULT_COOLDOWN, CLAN_REQUESTED_DATA_TYPE
from gui.clubs.settings import REQUEST_TIMEOUT
from gui.shared.rq_cooldown import RequestCooldownManager, REQUEST_SCOPE
from gui.shared.utils.requesters.RequestsController import RequestsController
from gui.shared.utils.requesters.abstract import Response, ClientRequestsByIDProcessor

class ClanRequestResponse(Response):

    def isSuccess(self):
        return self.getCode() in (ResponseCodes.NO_ERRORS, ResponseCodes.STRONGHOLD_NOT_FOUND)

    def getCode(self):
        return self.code

    def clone(self, data = None):
        return ClanRequestResponse(self.code, self.errStr, data or self.data)


class ClanRequester(ClientRequestsByIDProcessor):

    def __init__(self, sender):
        super(ClanRequester, self).__init__(sender, ClanRequestResponse)

    def doRequestEx(self, ctx, callback, methodName, *args, **kwargs):
        LOG_DEBUG('ClanRequester, do request:')
        LOG_DEBUG('   ctx        :', ctx)
        LOG_DEBUG('   methodName :', methodName)
        LOG_DEBUG('   Args       :', args)
        LOG_DEBUG('   Kwargs     :', kwargs)
        return super(ClanRequester, self).doRequestEx(ctx, callback, methodName, *args, **kwargs)

    def _getSenderMethod(self, sender, methodName):
        if isinstance(methodName, types.TupleType):
            storageName, methodName = methodName
            sender = getattr(sender, storageName, None)
        return super(ClanRequester, self)._getSenderMethod(sender, methodName)

    def _doCall(self, method, *args, **kwargs):
        requestID = self._idsGenerator.next()

        def _callback(data, statusCode, responseCode):
            if not requestID in self._requests:
                raise AssertionError('There is no context has been registered for given request. Probably you call callback at the same frame as request')
                ctx = self._requests[requestID]
                response = responseCode == ResponseCodes.NO_ERRORS and self._makeResponse(responseCode, '', data, ctx, extraCode=statusCode)
            else:
                errStr = data.pop('description', '')
                data = None
                response = self._makeResponse(responseCode, errStr, data, ctx, extraCode=statusCode)
            self._onResponseReceived(requestID, response)
            return

        method(_callback, *args, **kwargs)
        return requestID

    def makeInternalError(self, code, ctx):
        self._makeResponse(code, 'Internal error {}'.format(code), None, ctx)
        return


class ClanCooldownManager(RequestCooldownManager):

    def __init__(self):
        super(ClanCooldownManager, self).__init__(REQUEST_SCOPE.CLAN, DEFAULT_COOLDOWN)

    def lookupName(self, rqTypeID):
        if CLAN_REQUESTED_DATA_TYPE.hasValue(rqTypeID):
            requestName = clan_fmts.getRequestUserName(rqTypeID)
        else:
            requestName = str(rqTypeID)
            LOG_WARNING('Request type is not found', rqTypeID)
        return requestName

    def getDefaultCoolDown(self):
        return DEFAULT_COOLDOWN


class ClanRequestsController(RequestsController):

    def __init__(self, clansCtrl, requester, cooldown = ClanCooldownManager()):
        super(ClanRequestsController, self).__init__(requester, cooldown)
        self.__clansCtrl = weakref.proxy(clansCtrl)
        self.__handlers = {CLAN_REQUESTED_DATA_TYPE.LOGIN: self.__login,
         CLAN_REQUESTED_DATA_TYPE.LOGOUT: self.__logout,
         CLAN_REQUESTED_DATA_TYPE.CLAN_INFO: self.__getClanInfo,
         CLAN_REQUESTED_DATA_TYPE.CLAN_RATINGS: self.__getClanRatings,
         CLAN_REQUESTED_DATA_TYPE.CLAN_GLOBAL_MAP_STATS: self.__getClanGlobalMapStats,
         CLAN_REQUESTED_DATA_TYPE.CLAN_ACCOUNTS: self.__getClanAccounts,
         CLAN_REQUESTED_DATA_TYPE.STRONGHOLD_INFO: self.__getStronholdInfo,
         CLAN_REQUESTED_DATA_TYPE.ACCOUNT_APPLICATIONS_COUNT: self.__accountApplications,
         CLAN_REQUESTED_DATA_TYPE.CLAN_INVITATIONS_COUNT: self.__getClanInvitations,
         CLAN_REQUESTED_DATA_TYPE.CLAN_MEMBERS: self.__getClanMembers,
         CLAN_REQUESTED_DATA_TYPE.CLAN_MEMBERS_RATING: self.__getClanMembersRating,
         CLAN_REQUESTED_DATA_TYPE.STRONGHOLD_STATISTICS: self.__getClanFort,
         CLAN_REQUESTED_DATA_TYPE.CLAN_PROVINCES: self.__getProvinces,
         CLAN_REQUESTED_DATA_TYPE.SEARCH_CLANS: self.__searchClans,
         CLAN_REQUESTED_DATA_TYPE.GET_RECOMMENDED_CLANS: self.__getRecommendedClans,
         CLAN_REQUESTED_DATA_TYPE.CLAN_APPLICATIONS: self.__getClanApplications,
         CLAN_REQUESTED_DATA_TYPE.CLAN_INVITES: self.__getClanInvites,
         CLAN_REQUESTED_DATA_TYPE.ACCOUNT_INVITES: self.__getAccountInvites,
         CLAN_REQUESTED_DATA_TYPE.ACCEPT_APPLICATION: self.__acceptApplication,
         CLAN_REQUESTED_DATA_TYPE.ACCEPT_INVITE: self.__acceptInvite,
         CLAN_REQUESTED_DATA_TYPE.CREATE_APPLICATIONS: self.__createApplications,
         CLAN_REQUESTED_DATA_TYPE.CREATE_INVITES: self.__createInvites,
         CLAN_REQUESTED_DATA_TYPE.DECLINE_APPLICATION: self.__declineApplication,
         CLAN_REQUESTED_DATA_TYPE.DECLINE_INVITE: self.__declineInvite,
         CLAN_REQUESTED_DATA_TYPE.DECLINE_INVITES: self.__declineInvites,
         CLAN_REQUESTED_DATA_TYPE.GET_ACCOUNT_APPLICATIONS: self.__getAccountApplications,
         CLAN_REQUESTED_DATA_TYPE.CLANS_INFO: self.__getClansInfo,
         CLAN_REQUESTED_DATA_TYPE.CLAN_FAVOURITE_ATTRS: self.__getClanFavoriteAttributes,
         CLAN_REQUESTED_DATA_TYPE.PING: self.__ping}

    def fini(self):
        super(ClanRequestsController, self).fini()
        self.__handlers = None
        return

    def _getHandlerByRequestType(self, requestTypeID):
        if self.__handlers:
            return self.__handlers.get(requestTypeID)
        else:
            return None

    def _getRequestTimeOut(self):
        return REQUEST_TIMEOUT

    def _onClansReceived(self, clansResponse, callback):
        if clansResponse.isSuccess() and clansResponse.data and len(clansResponse.data['items']) > 0:
            dataRef = clansResponse.data['items']
            clanIDs = [ item['clan_id'] for item in dataRef ]
            clanRatingsCtx = contexts.ClanRatingsCtx(clanIDs)

            def _onRatingsReceived(ratingsResponse):
                if ratingsResponse.isSuccess():
                    ratings = clanRatingsCtx.getDataObj(ratingsResponse.data)
                    ratings = dict(((item.getClanDbID(), item) for item in ratings))
                    for clan in dataRef:
                        clan['clan_ratings_data'] = ratings.get(clan['clan_id'], items.ClanRatingsData())

                else:
                    for clan in dataRef:
                        clan['clan_ratings_data'] = items.ClanRatingsData()

                callback(clansResponse)

            self.__getClanRatings(clanRatingsCtx, _onRatingsReceived)
        else:
            callback(clansResponse)

    def __login(self, ctx, callback = None):
        return self._requester.doRequestEx(ctx, callback, 'login', ctx.getUserDatabaseID(), ctx.getTokenID())

    def __logout(self, ctx, callback = None):
        return self._requester.doRequestEx(ctx, callback, 'logout')

    def __ping(self, ctx, callback = None):
        return self._requester.doRequestEx(ctx, callback, 'get_alive_status')

    def __getClanInfo(self, ctx, callback = None):
        return self._requester.doRequestEx(ctx, callback, ('clans', 'get_clans_info'), (ctx.getClanID(),), fields=ctx.getFields())

    def __getClansInfo(self, ctx, callback = None):
        return self._requester.doRequestEx(ctx, callback, ('clans', 'get_clans_info'), ctx.getClanIDs(), fields=ctx.getFields())

    def __getClanRatings(self, ctx, callback = None):
        return self._requester.doRequestEx(ctx, callback, ('ratings', 'get_clans_ratings'), ctx.getClanIDs())

    def __getClanGlobalMapStats(self, ctx, callback = None):
        return self.__doClanRequest(ctx, callback, ('global_map', 'get_statistics'))

    def __getClanFort(self, ctx, callback = None):
        return self.__doClanRequest(ctx, callback, ('strongholds', 'get_statistics'))

    def __getProvinces(self, ctx, callback = None):

        def __onProvincesReceived(response):
            if response.isSuccess() and response.data:
                frontsCtx = GetFrontsCtx(map(lambda v: v['front_name'], response.data))

                def __onFrontsReceived(frontsResponse):
                    if frontsResponse.isSuccess():
                        fronts = frontsCtx.getDataObj(frontsResponse.data)
                    else:
                        fronts = {}
                    for province in response.data:
                        province['frontInfo'] = fronts.get(province['front_name'], frontsCtx.getDefDataObj())

                    callback(response)

                self.__getGMFronts(frontsCtx, __onFrontsReceived)
            else:
                callback(response)

        return self.__doClanRequest(ctx, __onProvincesReceived, ('global_map', 'get_provinces'))

    def __getGMFronts(self, ctx, callback = None):
        return self._requester.doRequestEx(ctx, callback, ('global_map', 'get_fronts_info'), ctx.getProvincesIDs())

    def __getClanAccounts(self, ctx, callback = None):
        return self._requester.doRequestEx(ctx, callback, ('clans', 'get_accounts_clans'), ctx.getAccountsIDs())

    def __getClanMembers(self, ctx, callback = None):

        def _onMembersReceived(membersResponse):
            if membersResponse.isSuccess():
                ctx = contexts.AccountClanRatingsCtx(map(lambda v: v['account_id'], membersResponse.data))

                def _onRatingsReceived(ratingsResponse):
                    if ratingsResponse.isSuccess():
                        ratings = ctx.getDataObj(ratingsResponse.data)
                    else:
                        ratings = {}
                    for m in membersResponse.data:
                        m['ratings'] = ratings.get(m['account_id'], items.AccountClanRatingsData(account_id=m['account_id']))

                    callback(membersResponse)

                self.__getClanMembersRating(ctx, _onRatingsReceived)
            else:
                callback(membersResponse)

        return self.__doClanRequest(ctx, _onMembersReceived, ('clans', 'get_clan_members'))

    def __getClanMembersRating(self, ctx, callback = None):
        return self._requester.doRequestEx(ctx, callback, ('exporter', 'get_accounts_info'), ctx.getAccountsIDs())

    def __getStronholdInfo(self, ctx, callback = None):
        return self.__doClanRequest(ctx, callback, ('strongholds', 'get_info'))

    def __accountApplications(self, ctx, callback):
        return self.__doTotalRequest(ctx, callback, ('clans', 'get_account_applications_count_since'))

    def __getClanInvitations(self, ctx, callback):
        return self.__doTotalRequest(ctx, callback, ('clans', 'get_clan_invites_count_since'))

    def __searchClans(self, ctx, callback):
        limits = self.__clansCtrl.getLimits()
        isValid, reason = limits.canSearchClans(ctx.getSearchCriteria())
        if not isValid:
            return self.__doFail(ctx, reason, callback)
        return self._requester.doRequestEx(ctx, partial(self._onClansReceived, callback=callback), ('clans', 'search_clans'), search=ctx.getSearchCriteria(), get_total_count=ctx.isGetTotalCount(), fields=ctx.getFields(), offset=ctx.getOffset(), limit=ctx.getLimit())

    def __getRecommendedClans(self, ctx, callback):
        return self._requester.doRequestEx(ctx, partial(self._onClansReceived, callback=callback), ('clans', 'get_recommended_clans'), get_total_count=ctx.isGetTotalCount(), fields=ctx.getFields(), offset=ctx.getOffset(), limit=ctx.getLimit())

    def __getClanApplications(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('clans', 'get_clan_applications'), clan_id=ctx.getClanDbID(), fields=ctx.getFields(), statuses=ctx.getStatuses(), offset=ctx.getOffset(), limit=ctx.getLimit(), get_total_count=ctx.isGetTotalCount())

    def __getClanInvites(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('clans', 'get_clan_invites'), clan_id=ctx.getClanDbID(), fields=ctx.getFields(), statuses=ctx.getStatuses(), offset=ctx.getOffset(), limit=ctx.getLimit(), get_total_count=ctx.isGetTotalCount())

    def __getAccountInvites(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('clans', 'get_account_invites'), fields=ctx.getFields(), statuses=ctx.getStatuses(), offset=ctx.getOffset(), limit=ctx.getLimit(), get_total_count=ctx.isGetTotalCount())

    def __getAccountApplications(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('clans', 'get_account_applications'), fields=ctx.getFields(), statuses=ctx.getStatuses(), offset=ctx.getOffset(), limit=ctx.getLimit(), get_total_count=ctx.isGetTotalCount())

    def __doTotalRequest(self, ctx, callback, methodName):
        return self._requester.doRequestEx(ctx, callback, methodName, ctx.getID())

    def __doClanRequest(self, ctx, callback, methodName):
        return self._requester.doRequestEx(ctx, callback, methodName, ctx.getClanID())

    def __acceptApplication(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('clans', 'accept_application'), application_id=ctx.getApplicationDbID())

    def __acceptInvite(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('clans', 'accept_invite'), invite_id=ctx.getInviteDbID())

    def __createApplications(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('clans', 'create_applications'), clan_ids=ctx.getClanDbIDs(), comment=ctx.getComment())

    def __createInvites(self, ctx, callback):
        limits = self.__clansCtrl.getLimits()
        isValid, reason = limits.canSendInvite(self.__clansCtrl.getClanDossier(ctx.getClanDbID()))
        if not isValid:
            return self.__doFail(ctx, reason, callback)
        return self._requester.doRequestEx(ctx, callback, ('clans', 'create_invites'), clan_id=ctx.getClanDbID(), account_ids=ctx.getAccountDbIDs(), comment=ctx.getComment())

    def __declineApplication(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('clans', 'decline_application'), application_id=ctx.getApplicationDbID())

    def __declineInvite(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('clans', 'decline_invite'), invite_id=ctx.getInviteDbID())

    def __declineInvites(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('clans', 'bulk_decline_invites'), invite_ids=ctx.getInviteDbIDs())

    def __getClanFavoriteAttributes(self, ctx, callback = None):
        return self._requester.doRequestEx(ctx, callback, ('clans', 'get_clan_favorite_attributes'), ctx.getClanID())

    def __doFail(self, ctx, reason, callback):
        self._requester._stopProcessing(ctx, reason, callback)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\clans\requests.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:08 St�edn� Evropa (b�n� �as)

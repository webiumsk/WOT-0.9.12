# 2015.11.18 11:53:30 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/clans/invites/ClanInvitesViewWithTable.py
import weakref
import math
from debug_utils import LOG_ERROR
from gui.clans.settings import CLAN_INVITE_STATES, ACTIVE_INVITE_LIFE_TIME
from gui.clans.items import isValueAvailable, formatField
from gui.Scaleform.daapi.view.meta.ClanInvitesViewWithTableMeta import ClanInvitesViewWithTableMeta
from gui.Scaleform.framework.entities.DAAPIDataProvider import SortableDAAPIDataProvider
from gui.Scaleform.genConsts.CLANS_ALIASES import CLANS_ALIASES
from gui.Scaleform.locale.CLANS import CLANS
from gui.shared.formatters import text_styles
from helpers import time_utils
from helpers.i18n import makeString as _ms
from gui.shared.utils.functions import makeTooltip

class ClanInvitesViewWithTable(ClanInvitesViewWithTableMeta):

    def __init__(self):
        super(ClanInvitesViewWithTable, self).__init__()
        self._parentWnd = None
        return

    @property
    def dataProvider(self):
        return self._searchDP

    def setParentWindow(self, wnd):
        self._parentWnd = weakref.proxy(wnd)
        self._onAttachedToWindow()

    def _populate(self):
        super(ClanInvitesViewWithTable, self)._populate()
        self._searchDP = self._createSearchDP()
        self._searchDP.setFlashObject(self.as_getTableDPS())
        self._searchDP.buildList(None)
        return

    def _onAttachedToWindow(self):
        self.as_setDataS(self._makeData())

    def _updateSortField(self, sort):
        if sort is not None and len(sort):
            order = 'ascending' if sort[0][1] else 'descending'
            self.as_updateDefaultSortFieldS(defaultSortField=sort[0][0], defaultSortDirection=order)
        else:
            self.as_updateDefaultSortFieldS(defaultSortField=None, defaultSortDirection=None)
        return

    def _makeData(self):
        return {'tableHeaders': self._makeHeaders(),
         'texts': self._makeTexts()}

    def _getDefaultSortFields(self):
        return tuple()

    def _createSearchDP(self):
        raise NotImplementedError

    def _makeHeaders(self):
        raise NotImplementedError

    def _makeTexts(self):
        return [{'alias': CLANS_ALIASES.INVITE_WINDOW_DUMMY_SERVER_ERROR,
          'title': CLANS.CLANINVITESWINDOW_DUMMY_SERVERERROR_TITLE,
          'text': CLANS.CLANINVITESWINDOW_DUMMY_SERVERERROR_TEXT}]

    @staticmethod
    def _packHeaderColumnData(headerId, label, buttonWidth, tooltip, icon = '', sortOrder = -1, showSeparator = True, textAlign = 'center', enabled = True):
        return {'id': headerId,
         'label': _ms(label),
         'iconSource': icon,
         'buttonWidth': buttonWidth,
         'toolTip': tooltip,
         'sortOrder': sortOrder,
         'defaultSortDirection': 'ascending',
         'buttonHeight': 34,
         'showSeparator': showSeparator,
         'textAlign': textAlign,
         'enabled': enabled}


class ClanInvitesAbstractDataProvider(SortableDAAPIDataProvider):

    def __init__(self, proxy):
        super(ClanInvitesAbstractDataProvider, self).__init__()
        self.__list = []
        self.__listMapping = {}
        self.__selectedID = None
        self.__proxy = weakref.proxy(proxy)
        self.__showMoreBtn = False
        self.__isActionsAllowed = True
        self.__extraData = {}
        return

    @property
    def sortedCollection(self):
        return self.collection

    @property
    def collection(self):
        return self.__list

    @property
    def proxy(self):
        return self.__proxy

    def itemsCount(self):
        return len(self.__list)

    def isActionsAllowed(self):
        return self.__isActionsAllowed

    def emptyItem(self):
        return None

    def clear(self, clearExtra = True):
        self.__list = []
        self.__listMapping.clear()
        self.__selectedID = None
        if clearExtra:
            self.__extraData.clear()
        return

    def fini(self):
        self.clear()
        self._dispose()

    def getSelectedIdx(self):
        if self.__selectedID in self.__listMapping:
            return self.__listMapping[self.__selectedID]
        return -1

    def setSelectedID(self, id):
        self.__selectedID = id

    def getVO(self, index):
        vo = None
        if index > -1:
            try:
                vo = self.sortedCollection[index]
            except IndexError:
                LOG_ERROR('Item not found', index)

        return vo

    def pySortOn(self, fields, order):
        sort = tuple(zip(fields, order))
        if sort != self._sort:
            self._sort = sort
            self.__proxy.onSortChanged(self, self._sort)

    def getExtraData(self, dbID):
        return self.__extraData.get(dbID, None)

    def buildList(self, cache, showMoreButton = False):
        self.clear(clearExtra=False)
        cache = cache or []
        newExtra = {}
        for index, item in enumerate(cache):
            extra = self._buildExtraData(item, self.getExtraData(item.getDbID()))
            if extra:
                newExtra[item.getDbID()] = extra
            self.__list.append(self._makeVO(item, extra))
            self.__listMapping[item.getDbID()] = index

        self.__extraData = newExtra
        if showMoreButton:
            self.__list.append({'hasShowMoreButton': True,
             'showMoreButtonEnabled': True})

    def rebuildList(self, cache, showMoreButton = False):
        self.__showMoreBtn = showMoreButton
        self.buildList(cache, showMoreButton)
        self.refresh()

    def allowActions(self, allowed):
        if self.__isActionsAllowed != allowed:
            self.__isActionsAllowed = allowed
            self.invalidateItems()
            self.refresh()

    def invalidateItems(self):
        pass

    def getVOByDbID(self, dbID):
        return self.__list[self.__listMapping[dbID]]

    def refreshItems(self, items):
        needRefresh = False
        for item in items:
            if item.getDbID() in self.__listMapping:
                needRefresh = True
                self.__extraData[item.getDbID()] = self._buildExtraData(item, self.getExtraData(item.getDbID()))
                vo = self._makeVO(item, self.getExtraData(item.getDbID()))
                self.__list[self.__listMapping[item.getDbID()]] = vo

        if needRefresh:
            self.refresh()

    def pyGetSelectedIdx(self):
        return self.getSelectedIdx()

    def _buildExtraData(self, item, prevExtra):
        return None

    def _isDataRow(self, vo):
        return 'dbID' in vo

    def _makeVO(self, item, extraData):
        return []

    def _makeTooltip(self, body):
        if body is not None and len(body):
            return makeTooltip(body=body)
        else:
            return

    def _makeRequestTooltip(self, status, date, user = None):
        if status == CLAN_INVITE_STATES.ACCEPTED:
            return text_styles.concatStylesToMultiLine(text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_REQUEST_REQUESTACCEPTED)), text_styles.main(date), text_styles.main(''), text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_REQUEST_BYUSER)), text_styles.stats(user))
        if status == CLAN_INVITE_STATES.DECLINED or status == CLAN_INVITE_STATES.DECLINED_RESENT:
            return text_styles.concatStylesToMultiLine(text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_REQUEST_REQUESTDECLINED)), text_styles.main(date), text_styles.main(''), text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_REQUEST_BYUSER)), text_styles.stats(user))
        if status == CLAN_INVITE_STATES.EXPIRED or status == CLAN_INVITE_STATES.EXPIRED_RESENT:
            return text_styles.concatStylesToMultiLine(text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_REQUEST_REQUESTSENT)), text_styles.main(date))
        return ''

    def _makeInviteStateString(self, item):
        status = item.getStatus()
        if status == CLAN_INVITE_STATES.ACTIVE:
            return text_styles.standard(self.__formatActiveStateString(item))
        if status == CLAN_INVITE_STATES.ACCEPTED:
            return text_styles.success(_ms(CLANS.CLANINVITESWINDOW_STATUS_ACCEPTED))
        if status == CLAN_INVITE_STATES.DECLINED:
            return text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_STATUS_DECLINED))
        if status == CLAN_INVITE_STATES.EXPIRED:
            return text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_STATUS_EXPIRED))
        if status == CLAN_INVITE_STATES.EXPIRED_RESENT or status == CLAN_INVITE_STATES.DECLINED_RESENT:
            return text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_STATUS_SENT))
        if status == CLAN_INVITE_STATES.ERROR:
            return text_styles.error(_ms(CLANS.CLANINVITESWINDOW_STATUS_ERROR))
        return ''

    def __formatActiveStateString(self, item):
        if not isValueAvailable(getter=item.getCreatedAt):
            return _ms(CLANS.CLANINVITESWINDOW_STATUS_MINUTESLEFT, min=formatField(getter=item.getCreatedAt))
        createdAt = item.getCreatedAt()
        delta = time_utils.getTimeDeltaFromNow(createdAt + ACTIVE_INVITE_LIFE_TIME)
        if delta >= time_utils.ONE_DAY:
            state = _ms(CLANS.CLANINVITESWINDOW_STATUS_DAYSLEFT, days=int(math.ceil(float(delta) / time_utils.ONE_DAY)))
        elif delta >= time_utils.ONE_HOUR:
            state = _ms(CLANS.CLANINVITESWINDOW_STATUS_HOURSLEFT, hours=int(math.ceil(float(delta) / time_utils.ONE_HOUR)))
        else:
            mins = max(1, int(delta / time_utils.ONE_MINUTE))
            state = _ms(CLANS.CLANINVITESWINDOW_STATUS_MINUTESLEFT, min=mins)
        return state
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\clans\invites\claninvitesviewwithtable.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:53:31 St�edn� Evropa (b�n� �as)

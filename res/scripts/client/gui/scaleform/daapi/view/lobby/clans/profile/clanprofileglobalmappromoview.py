# 2015.11.18 11:53:34 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/clans/profile/ClanProfileGlobalMapPromoView.py
from helpers.i18n import makeString as _ms
from gui.Scaleform.locale.CLANS import CLANS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.shared.formatters import text_styles
from gui.shared.events import OpenLinkEvent
from gui.Scaleform.daapi.view.meta.ClanProfileGlobalMapPromoViewMeta import ClanProfileGlobalMapPromoViewMeta

class ClanProfileGlobalMapPromoView(ClanProfileGlobalMapPromoViewMeta):

    def showInfo(self):
        self.fireEvent(OpenLinkEvent(OpenLinkEvent.GLOBAL_MAP_PROMO))

    def showMap(self):
        self.fireEvent(OpenLinkEvent(OpenLinkEvent.GLOBAL_MAP_CAP))

    def _populate(self):
        super(ClanProfileGlobalMapPromoView, self)._populate()
        self.as_setDataS({'header': text_styles.promoSubTitle(_ms(CLANS.GLOBALMAPVIEW_PROMO_HEADER)),
         'description': text_styles.main(_ms(CLANS.GLOBALMAPVIEW_PROMO_DESCRIPTION)),
         'infoLinkLabel': _ms(CLANS.GLOBALMAPVIEW_PROMO_INFOLINK),
         'mapLinkLabel': _ms(CLANS.GLOBALMAPVIEW_PROMO_MAPLINK),
         'background': RES_ICONS.MAPS_ICONS_CLANS_GLOBAL_MAP_PROMO})
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\clans\profile\clanprofileglobalmappromoview.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:53:34 Støední Evropa (bìžný èas)

# 2015.11.18 11:54:18 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/messengerBar/ChannelCarousel.py
from debug_utils import LOG_DEBUG
from gui.Scaleform.daapi.view.meta.ChannelCarouselMeta import ChannelCarouselMeta
from gui.shared import EVENT_BUS_SCOPE
from gui.shared.events import ChannelCarouselEvent

class ChannelCarousel(ChannelCarouselMeta):

    def __init__(self):
        super(ChannelCarousel, self).__init__()

    def __del__(self):
        LOG_DEBUG('Channel carousel deleted:', id(self))

    def _populate(self):
        super(ChannelCarousel, self)._populate()
        self.fireEvent(ChannelCarouselEvent(self, ChannelCarouselEvent.CAROUSEL_INITED), scope=EVENT_BUS_SCOPE.LOBBY)

    def _dispose(self):
        self.fireEvent(ChannelCarouselEvent(self, ChannelCarouselEvent.CAROUSEL_DESTROYED), scope=EVENT_BUS_SCOPE.LOBBY)
        super(ChannelCarousel, self)._dispose()

    def channelOpenClick(self, itemID):
        self.fireEvent(ChannelCarouselEvent(self, ChannelCarouselEvent.OPEN_BUTTON_CLICK, itemID), scope=EVENT_BUS_SCOPE.LOBBY)

    def channelCloseClick(self, itemID):
        self.fireEvent(ChannelCarouselEvent(self, ChannelCarouselEvent.CLOSE_BUTTON_CLICK, itemID), scope=EVENT_BUS_SCOPE.LOBBY)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\messengerbar\channelcarousel.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:54:18 Støední Evropa (bìžný èas)

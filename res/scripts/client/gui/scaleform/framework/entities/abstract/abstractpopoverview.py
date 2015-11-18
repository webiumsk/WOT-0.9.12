# 2015.11.18 11:55:23 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/AbstractPopOverView.py
from debug_utils import LOG_DEBUG
from gui.Scaleform.daapi.view.meta.PopOverViewMeta import PopOverViewMeta
from gui.shared.events import HidePopoverEvent

class AbstractPopOverView(PopOverViewMeta):

    def __init__(self, ctx = None):
        super(AbstractPopOverView, self).__init__()

    def _populate(self):
        super(AbstractPopOverView, self)._populate()
        self.addListener(HidePopoverEvent.HIDE_POPOVER, self.__handlerHidePopover)

    def __handlerHidePopover(self, event):
        self.destroy()

    def _dispose(self):
        self.removeListener(HidePopoverEvent.HIDE_POPOVER, self.__handlerHidePopover)
        super(AbstractPopOverView, self)._dispose()
        self.fireEvent(HidePopoverEvent(HidePopoverEvent.POPOVER_DESTROYED))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\framework\entities\abstract\abstractpopoverview.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:55:23 St�edn� Evropa (b�n� �as)

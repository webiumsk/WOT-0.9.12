# 2015.11.18 11:52:46 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/prb_control/functional/not_supported.py
from debug_utils import LOG_ERROR
from gui.prb_control.functional import interfaces

class NotSupportedEntry(interfaces.IPrbEntry):

    def create(self, ctx, callback = None):
        LOG_ERROR('NotSupportedEntry.create', ctx)

    def join(self, ctx, callback = None):
        LOG_ERROR('NotSupportedEntry.join', ctx)

    def select(self, ctx, callback = None):
        LOG_ERROR('NotSupportedEntry.select', ctx)


class NotSupportedFunctional(interfaces.IClientFunctional):

    def canPlayerDoAction(self):
        LOG_ERROR('Actions are disabled. Formation is not supported')
        return (False, '')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\prb_control\functional\not_supported.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:46 Støední Evropa (bìžný èas)

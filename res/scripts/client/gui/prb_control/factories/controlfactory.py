# 2015.11.18 11:52:39 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/prb_control/factories/ControlFactory.py
from debug_utils import LOG_DEBUG
from gui.prb_control.items import PlayerDecorator
from gui.prb_control.settings import FUNCTIONAL_FLAG

class ControlFactory(object):

    def __del__(self):
        LOG_DEBUG('ControlFactory is deleted', self)

    def createEntry(self, ctx):
        raise NotImplementedError()

    def createEntryByAction(self, action):
        raise NotImplementedError()

    def createFunctional(self, ctx):
        raise NotImplementedError()

    def createPlayerInfo(self, functional):
        return PlayerDecorator()

    def createStateEntity(self, functional):
        raise NotImplementedError()

    def createLeaveCtx(self, flags = FUNCTIONAL_FLAG.UNDEFINED):
        raise NotImplementedError()

    @staticmethod
    def _createEntryByAction(action, available):
        result = None
        if action in available:
            clazz, args = available[action]
            if args:
                result = clazz(*args)
            else:
                result = clazz()
        return result
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\prb_control\factories\controlfactory.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:39 Støední Evropa (bìžný èas)

# 2015.11.18 11:58:24 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/tutorial/control/quests/aspects.py
import weakref
from helpers import aop

class XpExchangeAspect(aop.Aspect):

    def __init__(self, trigger, *args, **kwargs):
        super(XpExchangeAspect, self).__init__()
        self.__triggerRef = weakref.ref(trigger)

    def atCall(self, cd):
        trigger = self.__triggerRef()
        if trigger is None:
            return
        else:
            trigger.toggle(isOn=trigger.isOn(success=True))
            return

    def clear(self):
        self.__triggerRef = None
        return


class XpExchangePointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.shared.gui_items.processors.common', 'FreeXPExchanger', '_successHandler')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\tutorial\control\quests\aspects.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:58:24 Støední Evropa (bìžný èas)

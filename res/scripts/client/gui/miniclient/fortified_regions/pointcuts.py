# 2015.11.18 11:52:30 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/miniclient/fortified_regions/pointcuts.py
import aspects
from helpers import aop

class OnViewPopulate(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.fortifications.components.FortWelcomeInfoView', 'FortWelcomeInfoView', '_populate', aspects=(aspects.OnViewPopulate,))


class OnFortifiedRegionsOpen(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.fortifications.FortificationsView', 'FortificationsView', 'loadView', aspects=(aspects.OnFortifiedRegionsOpen,))


class FortificationsViewSubscriptions(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.fortifications.FortificationsView', 'FortificationsView', 'onClientStateChanged', aspects=(aop.DummyAspect,))


class OnFortRequirementsUpdate(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.fortifications.components.FortWelcomeViewComponent', 'FortWelcomeViewComponent', '_FortWelcomeViewComponent__updateViewState|onClientStateChangedonClanMembersListChanged|onNavigate', aspects=(aop.DummyAspect,))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\miniclient\fortified_regions\pointcuts.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:30 Støední Evropa (bìžný èas)

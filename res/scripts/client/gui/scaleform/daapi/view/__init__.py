# 2015.11.18 11:53:08 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/__init__.py
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE
from gui.Scaleform.managers.context_menu import ContextMenuManager
ContextMenuManager.registerHandler(CONTEXT_MENU_HANDLER_TYPE.APPEAL_USER, 'gui.Scaleform.daapi.view.lobby.user_cm_handlers', 'AppealCMHandler')
ContextMenuManager.registerHandler(CONTEXT_MENU_HANDLER_TYPE.BASE_USER, 'gui.Scaleform.daapi.view.lobby.user_cm_handlers', 'BaseUserCMHandler')
ContextMenuManager.registerHandler(CONTEXT_MENU_HANDLER_TYPE.BASE_CLAN, 'gui.Scaleform.daapi.view.lobby.clans.clan_cm_handlers', 'BaseClanCMHandler')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:53:08 Støední Evropa (bìžný èas)

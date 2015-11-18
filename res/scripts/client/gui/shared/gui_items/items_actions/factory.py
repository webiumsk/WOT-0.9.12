# 2015.11.18 11:56:42 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/shared/gui_items/items_actions/factory.py
from debug_utils import LOG_ERROR
from gui.shared.gui_items.items_actions import actions
SELL_ITEM = 'sellItemAction'
BUY_VEHICLE = 'vehBuyAction'
BUY_MODULE = 'moduleBuyAction'
UNLOCK_ITEM = 'unlockAction'
INSTALL_ITEM = 'installItemAction'
BUY_AND_INSTALL_ITEM = 'buyAndInstallItemAction'
SET_VEHICLE_MODULE = 'setVehicleModuleAction'
_ACTION_MAP = {SELL_ITEM: actions.SellItemAction,
 UNLOCK_ITEM: actions.UnlockItemAction,
 BUY_MODULE: actions.ModuleBuyAction,
 BUY_VEHICLE: actions.VehicleBuyAction,
 INSTALL_ITEM: actions.InstallItemAction,
 BUY_AND_INSTALL_ITEM: actions.BuyAndInstallItemAction,
 SET_VEHICLE_MODULE: actions.SetVehicleModuleAction}

def doAction(actionType, *args):
    if actionType in _ACTION_MAP:
        _ACTION_MAP[actionType](*args).doAction()
    else:
        LOG_ERROR('Action typeis not found', actionType)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\items_actions\factory.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:56:42 Støední Evropa (bìžný èas)

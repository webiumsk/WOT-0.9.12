# 2015.11.18 11:52:29 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/miniclient/shop.py
from helpers import aop
from helpers.i18n import makeString as _ms
from gui.shared.gui_items import GUI_ITEM_TYPE

class _OnShopItemWrapAspect(aop.Aspect):

    def __init__(self, config):
        self.__config = config
        aop.Aspect.__init__(self)

    def atReturn(self, cd):
        original_wrapping = cd.returned
        packedItem = cd.args[0]
        module = packedItem[0]
        warnMessage = ''
        if module.itemTypeID == GUI_ITEM_TYPE.VEHICLE and not self.__config['vehicle_is_available'](module):
            warnMessage = _ms('#miniclient:shop_vehicle_item_renderer/warn_message')
        original_wrapping['warnMessage'] = warnMessage
        return original_wrapping


class OnShopItemWrapPointcut(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.store.Shop', 'Shop', 'itemWrapper', aspects=(_OnShopItemWrapAspect(config),))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\miniclient\shop.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:29 St�edn� Evropa (b�n� �as)

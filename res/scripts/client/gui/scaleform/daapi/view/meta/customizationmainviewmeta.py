# 2015.11.18 11:54:57 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CustomizationMainViewMeta.py
from gui.Scaleform.framework.entities.View import View

class CustomizationMainViewMeta(View):

    def showBuyWindow(self):
        self._printOverrideError('showBuyWindow')

    def closeWindow(self):
        self._printOverrideError('closeWindow')

    def installCustomizationElement(self, id):
        self._printOverrideError('installCustomizationElement')

    def uninstallCustomizationElement(self, id):
        self._printOverrideError('uninstallCustomizationElement')

    def selectCustomizationElement(self, id):
        self._printOverrideError('selectCustomizationElement')

    def removeFromShoppingBasket(self, slotId, groupId, id):
        self._printOverrideError('removeFromShoppingBasket')

    def changeCarouselFilter(self):
        self._printOverrideError('changeCarouselFilter')

    def setDurationType(self, id):
        self._printOverrideError('setDurationType')

    def showPurchased(self, value):
        self._printOverrideError('showPurchased')

    def removeSlot(self, groupId, id):
        self._printOverrideError('removeSlot')

    def showGroup(self, groupId, id):
        self._printOverrideError('showGroup')

    def backToSelectorGroup(self):
        self._printOverrideError('backToSelectorGroup')

    def as_showBuyingPanelS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showBuyingPanel()

    def as_hideBuyingPanelS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideBuyingPanel()

    def as_setHeaderDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderData(data)

    def as_setBonusPanelDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBonusPanelData(data)

    def as_setBuyingPanelDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBuyingPanelData(data)

    def as_setBuyingPanelInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBuyingPanelInitData(data)

    def as_setCarouselDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselData(data)

    def as_setCarouselInitS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselInit(data)

    def as_setCarouselFilterDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselFilterData(data)

    def as_setBottomPanelHeaderS(self, newHeaderText):
        if self._isDAAPIInited():
            return self.flashObject.as_setBottomPanelHeader(newHeaderText)

    def as_setSlotsPanelDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setSlotsPanelData(data)

    def as_showSelectorItemS(self, id):
        if self._isDAAPIInited():
            return self.flashObject.as_showSelectorItem(id)

    def as_showSelectorGroupS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showSelectorGroup()

    def as_updateSlotS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSlot(data)

    def as_setBottomPanelInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBottomPanelInitData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\customizationmainviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:54:57 St�edn� Evropa (b�n� �as)

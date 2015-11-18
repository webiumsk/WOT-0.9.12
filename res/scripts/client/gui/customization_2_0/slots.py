# 2015.11.18 11:52:16 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/customization_2_0/slots.py
import copy
import time
from Event import Event
from helpers.i18n import makeString as _ms
from gui import makeHtmlString
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.Scaleform.locale.VEHICLE_CUSTOMIZATION import VEHICLE_CUSTOMIZATION
from gui.shared.formatters import text_styles
from gui.shared.utils.HangarSpace import g_hangarSpace
from gui.shared.utils.functions import getAbsoluteUrl, makeTooltip
from data_aggregator import CUSTOMIZATION_TYPE, SLOT_TYPE
from cart import Cart
from bonus_panel import BonusPanel
_SLOT_TOOLTIP_MAPPING = {CUSTOMIZATION_TYPE.CAMOUFLAGE: VEHICLE_CUSTOMIZATION.CUSTOMIZATION_TOOLTIP_SLOT_CAMOUFLAGE,
 CUSTOMIZATION_TYPE.EMBLEM: VEHICLE_CUSTOMIZATION.CUSTOMIZATION_TOOLTIP_SLOT_EMBLEM,
 CUSTOMIZATION_TYPE.INSCRIPTION: VEHICLE_CUSTOMIZATION.CUSTOMIZATION_TOOLTIP_SLOT_INSCRIPTION}
_EMPTY_SLOTS_MAP = {CUSTOMIZATION_TYPE.CAMOUFLAGE: (RES_ICONS.MAPS_ICONS_CUSTOMIZATION_SLOTS_EMPTY_CAMOUFLAGE_WINTER, RES_ICONS.MAPS_ICONS_CUSTOMIZATION_SLOTS_EMPTY_CAMOUFLAGE_SUMMER, RES_ICONS.MAPS_ICONS_CUSTOMIZATION_SLOTS_EMPTY_CAMOUFLAGE_DESERT),
 CUSTOMIZATION_TYPE.EMBLEM: RES_ICONS.MAPS_ICONS_CUSTOMIZATION_SLOTS_EMPTY_EMBLEM,
 CUSTOMIZATION_TYPE.INSCRIPTION: RES_ICONS.MAPS_ICONS_CUSTOMIZATION_SLOTS_EMPTY_INSCRIPTION}

class Slots(object):

    def __init__(self, aggregatedData):
        self.cart = Cart(aggregatedData)
        self.bonusPanel = BonusPanel(aggregatedData)
        self.updated = Event()
        self.selected = Event()
        self.__aData = aggregatedData
        self.__currentType = CUSTOMIZATION_TYPE.CAMOUFLAGE
        self.__currentIdx = 0
        self.__data = None
        self.__initialData = None
        self.__updateSlotsData(False)
        self.__aData.updated += self.__updateSlotsData
        return

    def fini(self):
        self.__aData.updated -= self.__updateSlotsData
        self.__aData = None
        self.__data = None
        self.__initialData = None
        self.cart.fini()
        self.bonusPanel.fini()
        self.cart = None
        self.bonusPanel = None
        return

    def getSelectedSlotItemID(self):
        return self.__data['data'][self.__currentType]['data'][self.__currentIdx]['itemID']

    def getInstalledItem(self, idx = None, type_ = None):
        idx = self.__currentIdx if idx is None else idx
        type_ = self.__currentType if type_ is None else type_
        return self.__aData.installed[type_][idx]

    def getSlotItem(self, slotIdx = None, cType = None):
        slotIdx = self.__currentIdx if slotIdx is None else slotIdx
        cType = self.__currentType if cType is None else cType
        itemID = self.__data['data'][cType]['data'][slotIdx]['itemID']
        if itemID < 0:
            return
        else:
            return self.__aData.available[cType][itemID]
            return

    def getItemById(self, cType, itemId):
        return self.__aData.available[cType][itemId]

    def getSummaryString(self):
        totalSlotsNum = 0
        occupiedSlotsNum = 0
        for slotGroupData in self.__data['data']:
            totalSlotsNum += len(slotGroupData['data'])
            for slotData in slotGroupData['data']:
                if slotData['itemID'] >= 0:
                    occupiedSlotsNum += 1

        return text_styles.highTitle(_ms('#customization:typeSwitchScreen/slotSummary', occupiedSlotsNum=occupiedSlotsNum, totalSlotsNum=totalSlotsNum))

    def getCurrentTypeLabel(self):
        return text_styles.middleTitle(_ms('#customization:typeSwitchScreen/typeName/plural/{0}'.format(self.__currentType)))

    def getData(self):
        return self.__data

    def select(self, cType, slotIdx):
        self.__currentType = cType
        self.__currentIdx = slotIdx
        self.selected(cType, slotIdx)
        g_hangarSpace.space.updateVehicleSticker(self.__aData.viewModel[1:3])
        if cType != CUSTOMIZATION_TYPE.CAMOUFLAGE:
            slotItem = self.__data['data'][cType]['data'][slotIdx]
            g_hangarSpace.space.locateCameraOnEmblem(slotItem['spot'] == 0, SLOT_TYPE[cType], self.calculateVehicleIndex(slotIdx, cType), 0.2)
        else:
            g_hangarSpace.space.locateCameraToPreview()

    def updateSlot(self, item, cType = None, slotIdx = None, duration = 0):
        slotIdx = self.__currentIdx if slotIdx is None else slotIdx
        cType = self.__currentType if cType is None else cType
        if item['id'] < 0:
            if cType == CUSTOMIZATION_TYPE.CAMOUFLAGE:
                img = _EMPTY_SLOTS_MAP[cType][slotIdx]
            else:
                img = _EMPTY_SLOTS_MAP[cType]
            price = 0
            bonus = ''
            isInDossier = False
        else:
            img = item['object'].getTexturePath()
            price = item['object'].getPrice(duration)
            isInDossier = item['object'].isInDossier
            bonus = self.__getSlotBonusString(item['object'].qualifier, isInDossier)
        typedData = self.__data['data'][cType]['data']
        if len(typedData) == 2:
            thisItemSlotIdx = slotIdx
            anotherSlotIdx = 1 - slotIdx
            if item['id'] < 0:
                if typedData[thisItemSlotIdx]['itemID'] == typedData[anotherSlotIdx]['itemID']:
                    typedData[anotherSlotIdx]['price'] = self.getSlotItem(cType=cType, slotIdx=anotherSlotIdx).getPrice(typedData[anotherSlotIdx]['duration'])
            elif item['id'] == typedData[anotherSlotIdx]['itemID']:
                if duration == 0:
                    typedData[anotherSlotIdx]['price'] = 0
                elif typedData[anotherSlotIdx]['duration'] == 0:
                    price = 0
            else:
                itemInAnotherSlot = self.getSlotItem(cType=cType, slotIdx=anotherSlotIdx)
                if itemInAnotherSlot is not None:
                    typedData[anotherSlotIdx]['price'] = itemInAnotherSlot.getPrice(typedData[anotherSlotIdx]['duration'])
        currentSlotItem = self.__data['data'][cType]['data'][slotIdx]
        newSlotItem = {'itemID': item['id'],
         'img': img,
         'purchaseTypeIcon': RES_ICONS.MAPS_ICONS_LIBRARY_GOLDICON_2 if duration == 0 else RES_ICONS.MAPS_ICONS_LIBRARY_CREDITSICON_2,
         'bonus': bonus,
         'duration': duration,
         'spot': currentSlotItem['spot'],
         'price': price,
         'isInDossier': isInDossier,
         'slotTooltip': makeTooltip(_ms(TOOLTIPS.CUSTOMIZATION_SLOT_HEADER, groupName=_ms(_SLOT_TOOLTIP_MAPPING[self.__currentType])), TOOLTIPS.CUSTOMIZATION_SLOT_BODY),
         'removeBtnTooltip': makeTooltip(TOOLTIPS.CUSTOMIZATION_SLOTREMOVE_HEADER, TOOLTIPS.CUSTOMIZATION_SLOTREMOVE_BODY)}
        self.__updateViewModel(cType, slotIdx, newSlotItem)
        initialSlotItem = self.__initialData['data'][cType]['data'][slotIdx]
        if newSlotItem['itemID'] < 0 or initialSlotItem['itemID'] == newSlotItem['itemID']:
            if currentSlotItem['isInDossier']:
                self.cart.buyItem(cType, newSlotItem['spot'], self.calculateVehicleIndex(slotIdx, cType), currentSlotItem['itemID'], 0, price=-1)
            else:
                initialSlotItem = copy.deepcopy(initialSlotItem)
                self.__setSlotAndUpdateView(cType, slotIdx, initialSlotItem)
        elif newSlotItem['isInDossier']:
            numberOfDays = item['object'].numberOfDays
            if numberOfDays is not None:
                itemDuration = numberOfDays if numberOfDays == 30 else 7
                price = -2
            else:
                itemDuration = 0
                price = 0
            self.cart.buyItem(cType, newSlotItem['spot'], self.calculateVehicleIndex(slotIdx, cType), newSlotItem['itemID'], itemDuration, price=price)
        else:
            self.__setSlotAndUpdateView(cType, slotIdx, newSlotItem)
        return

    def calculateVehicleIndex(self, initialIndex, cType):
        if initialIndex == 1:
            slotItem = self.__data['data'][cType]['data'][initialIndex]
            adjacentSlotItem = self.__data['data'][cType]['data'][0]
            if slotItem['spot'] != adjacentSlotItem['spot']:
                return initialIndex - 1
            else:
                return initialIndex
        return initialIndex

    def __setSlotAndUpdateView(self, cType, slotIdx, itemToSet):
        self.__data['data'][cType]['data'][slotIdx] = itemToSet
        self.cart.update(self.__data)
        self.bonusPanel.update(self.__data)
        self.updated({'type': cType,
         'idx': slotIdx,
         'data': itemToSet})

    def __updateViewModel(self, cType, slotIdx, newSlotItem):
        if cType != CUSTOMIZATION_TYPE.CAMOUFLAGE:
            viewModelItem = [None if newSlotItem['itemID'] < 0 else newSlotItem['itemID'], time.time(), 0]
            if cType == CUSTOMIZATION_TYPE.INSCRIPTION:
                viewModelItem.append(0)
            self.__aData.viewModel[cType][newSlotItem['spot'] + self.calculateVehicleIndex(slotIdx, cType)] = viewModelItem
            g_hangarSpace.space.updateVehicleSticker(self.__aData.viewModel[1:3])
        return

    def __updateSlotsData(self, resetSlots):
        newSlotsData = {'data': [{'header': self.__setSlotsHeader(CUSTOMIZATION_TYPE.CAMOUFLAGE),
                   'data': self.__setSlotsData(CUSTOMIZATION_TYPE.CAMOUFLAGE)}, {'header': self.__setSlotsHeader(CUSTOMIZATION_TYPE.EMBLEM),
                   'data': self.__setSlotsData(CUSTOMIZATION_TYPE.EMBLEM)}, {'header': self.__setSlotsHeader(CUSTOMIZATION_TYPE.INSCRIPTION),
                   'data': self.__setSlotsData(CUSTOMIZATION_TYPE.INSCRIPTION)}]}
        if self.__initialData is not None and not resetSlots:
            self.__handleServerChange(newSlotsData)
            self.__initialData = newSlotsData
        else:
            self.__data = newSlotsData
            self.__initialData = copy.deepcopy(self.__data)
            if resetSlots:
                self.__resetSlots()
        self.cart.setInitialSlotsData(self.__initialData)
        self.cart.update(self.__data)
        self.bonusPanel.setInitialSlotsData(self.__initialData)
        self.bonusPanel.update(self.__data)
        return

    def __setSlotsData(self, cType):
        selectorSlotsData = []
        for slotIdx in range(0, len(self.__aData.installed[cType])):
            installedItem = self.__aData.installed[cType][slotIdx]
            itemID = installedItem.getID()
            if itemID is None or self.__aData.available[cType][itemID].getGroup() == 'auto':
                itemID = -1
            slotData = {'itemID': itemID,
             'slotTooltip': makeTooltip(_ms(TOOLTIPS.CUSTOMIZATION_SLOT_HEADER, groupName=_ms(_SLOT_TOOLTIP_MAPPING[cType])), TOOLTIPS.CUSTOMIZATION_SLOT_BODY),
             'removeBtnTooltip': makeTooltip(TOOLTIPS.CUSTOMIZATION_SLOTREMOVE_HEADER, TOOLTIPS.CUSTOMIZATION_SLOTREMOVE_BODY),
             'spot': installedItem.getSpot(),
             'isInDossier': itemID >= 0}
            if itemID < 0:
                if cType == CUSTOMIZATION_TYPE.CAMOUFLAGE:
                    slotData['img'] = _EMPTY_SLOTS_MAP[cType][slotIdx]
                else:
                    slotData['img'] = _EMPTY_SLOTS_MAP[cType]
            else:
                availableItem = self.__aData.available[cType][itemID]
                slotData['img'] = availableItem.getTexturePath()
                slotData['bonus'] = self.__getSlotBonusString(availableItem.qualifier, True)
                if self.__aData.available[cType][itemID].isInDossier:
                    purchaseTypeIcon = RES_ICONS.MAPS_ICONS_LIBRARY_GOLDICON_2
                else:
                    purchaseTypeIcon = RES_ICONS.MAPS_ICONS_LIBRARY_CREDITSICON_2
                slotData['purchaseTypeIcon'] = purchaseTypeIcon
                slotData['duration'] = installedItem.duration
                slotData['price'] = 0
            selectorSlotsData.append(slotData)

        return selectorSlotsData

    def __setSlotsHeader(self, type_):
        return text_styles.middleTitle(_ms('#customization:typeSwitchScreen/typeName/{0}'.format(type_)))

    def __getSlotBonusString(self, qualifier, isInDossier):
        bonus = makeHtmlString('html_templates:lobby/customization', 'bonusString', {'bonusIcon': getAbsoluteUrl(qualifier.getIcon16x16()),
         'bonusValue': qualifier.getValue(),
         'isConditional': '' if qualifier.getDescription() is None else '*'})
        if not isInDossier:
            bonus = text_styles.bonusAppliedText(bonus)
        return bonus

    def __handleServerChange(self, newSlotsData):
        for cType in (CUSTOMIZATION_TYPE.CAMOUFLAGE, CUSTOMIZATION_TYPE.EMBLEM, CUSTOMIZATION_TYPE.INSCRIPTION):
            for slotIdx in range(0, len(newSlotsData['data'][cType]['data'])):
                newSlotItem = newSlotsData['data'][cType]['data'][slotIdx]
                currentSlotItem = self.__data['data'][cType]['data'][slotIdx]
                initialSlotItem = self.__initialData['data'][cType]['data'][slotIdx]
                if newSlotItem['itemID'] != initialSlotItem['itemID']:
                    self.__data['data'][cType]['data'][slotIdx] = newSlotItem
                    self.updated({'type': cType,
                     'idx': slotIdx,
                     'data': newSlotItem})
                elif initialSlotItem['itemID'] != currentSlotItem['itemID']:
                    self.updated({'type': cType,
                     'idx': slotIdx,
                     'data': currentSlotItem})

    def __resetSlots(self):
        for cType in (CUSTOMIZATION_TYPE.CAMOUFLAGE, CUSTOMIZATION_TYPE.EMBLEM, CUSTOMIZATION_TYPE.INSCRIPTION):
            for slotIdx in range(0, len(self.__data['data'][cType]['data'])):
                self.updated({'type': cType,
                 'idx': slotIdx,
                 'data': self.__data['data'][cType]['data'][slotIdx]})
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\customization_2_0\slots.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:17 St�edn� Evropa (b�n� �as)

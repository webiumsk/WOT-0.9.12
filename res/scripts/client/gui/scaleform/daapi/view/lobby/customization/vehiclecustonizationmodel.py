# 2015.11.18 11:53:43 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/customization/VehicleCustonizationModel.py
import time

class VehicleCustomizationModel:
    _playerEmblems = None
    _playerInscriptions = None
    _playerEmblemsInit = None
    _playerInscriptionsInit = None

    @classmethod
    def setVehicleDescriptor(cls, vehicleDescriptor):
        VehicleCustomizationModel._playerEmblemsInit = list(vehicleDescriptor.playerEmblems)
        VehicleCustomizationModel._playerInscriptionsInit = list(vehicleDescriptor.playerInscriptions)
        VehicleCustomizationModel._playerEmblems = list(vehicleDescriptor.playerEmblems)
        VehicleCustomizationModel._playerInscriptions = list(vehicleDescriptor.playerInscriptions)

    @classmethod
    def resetVehicleDescriptor(cls, vehicleDescriptor):
        VehicleCustomizationModel._playerEmblems = list(vehicleDescriptor.playerEmblems)
        VehicleCustomizationModel._playerInscriptions = list(vehicleDescriptor.playerInscriptions)

    @classmethod
    def updateVehicleSticker(cls, itemType, itemID = None, itemPosition = 0, duration = 0):
        if itemType == 'player':
            list = VehicleCustomizationModel._playerEmblems
            sticker = (itemID, round(time.time()), duration)
        else:
            list = VehicleCustomizationModel._playerInscriptions
            sticker = (itemID,
             round(time.time()),
             duration,
             0)
        list[itemPosition] = sticker

    @classmethod
    def getVehicleModel(cls):
        return (tuple(VehicleCustomizationModel._playerEmblems), tuple(VehicleCustomizationModel._playerInscriptions))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\customization\vehiclecustonizationmodel.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:53:43 Støední Evropa (bìžný èas)

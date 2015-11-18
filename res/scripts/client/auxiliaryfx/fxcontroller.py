# 2015.11.18 11:51:29 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/AuxiliaryFx/FxController.py


class IAuxiliaryVehicleFx:

    def __init__(self, vehicle, fxManager):
        self._vehicle = vehicle
        self._fxManager = fxManager

    def destroy(self):
        pass

    def executeShotEffect(self):
        pass

    def executeHitEffect(self):
        pass

    def update(self, vehicle):
        pass


class AuxiliaryFxController:

    def __init__(self, fxControllers):
        self.__controllers = fxControllers

    def destroy(self):
        for controller in self.__controllers:
            controller.destroy()

        self.__controllers = None
        return

    def executeShotEffect(self):
        for controller in self.__controllers:
            controller.executeShotEffect()

    def executeHitEffect(self):
        for controller in self.__controllers:
            controller.executeHitEffect()

    def update(self, vehicle):
        for controller in self.__controllers:
            controller.update(vehicle)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\auxiliaryfx\fxcontroller.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:51:29 Støední Evropa (bìžný èas)

# 2015.11.18 11:52:32 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/miniclient/lobby/tank_carousel/pointcuts.py
from helpers import aop
import aspects

class MakeTankUnavailableInCarousel(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.hangar.TankCarousel', 'TankCarousel', '_getVehicleData', aspects=(aspects.MakeTankUnavailableInCarousel(config),))


class VehicleTooltipStatus(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'gui.shared.tooltips.vehicle', 'VehicleStatusField', '_VehicleStatusField__getVehicleStatus', aspects=(aspects.VehicleTooltipStatus(config),))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\miniclient\lobby\tank_carousel\pointcuts.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:32 Støední Evropa (bìžný èas)

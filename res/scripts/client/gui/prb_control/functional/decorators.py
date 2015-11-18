# 2015.11.18 11:52:43 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/prb_control/functional/decorators.py
from adisp import process
from constants import QUEUE_TYPE
from gui.prb_control.storage import prequeue_storage_getter
from gui.shared.utils import functions

def vehicleAmmoCheck(func):
    from CurrentVehicle import g_currentVehicle

    @process
    def wrapper(*args, **kwargs):
        res = yield functions.checkAmmoLevel((g_currentVehicle.item,))
        if res:
            func(*args, **kwargs)
        elif kwargs.get('callback') is not None:
            kwargs.get('callback')(False)
        return

    return wrapper


class falloutQueueAmmoCheck(object):

    @prequeue_storage_getter(QUEUE_TYPE.EVENT_BATTLES)
    def storage(self):
        return None

    def __call__(self, func):

        @process
        def wrapper(*args, **kwargs):
            vehicles = self.storage.getSelectedVehicles()
            res = yield functions.checkAmmoLevel(vehicles)
            if res:
                func(*args, **kwargs)
            elif kwargs.get('callback') is not None:
                kwargs.get('callback')(False)
            return

        return wrapper
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\prb_control\functional\decorators.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:44 Støední Evropa (bìžný èas)

# 2015.11.18 11:58:39 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/Vibroeffects/Controllers/SwitchController.py
import BigWorld
from Vibroeffects import VibroManager
from debug_utils import *

class SwitchController:

    def __init__(self, effectName):
        self.__effect = VibroManager.g_instance.getEffect(effectName)

    def destroy(self):
        VibroManager.g_instance.stopEffect(self.__effect)
        self.__effect = None
        return

    def switch(self, turnOn):
        if turnOn:
            VibroManager.g_instance.startEffect(self.__effect)
        else:
            VibroManager.g_instance.stopEffect(self.__effect)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\vibroeffects\controllers\switchcontroller.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:58:39 Støední Evropa (bìžný èas)

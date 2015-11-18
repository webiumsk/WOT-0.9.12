# 2015.11.18 11:58:38 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/Vibroeffects/Controllers/OnceController.py
import BigWorld
from Vibroeffects import VibroManager
from debug_utils import *

class OnceController:

    def __init__(self, effectName, gain = 100):
        VibroManager.g_instance.launchQuickEffect(effectName, 1, gain)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\vibroeffects\controllers\oncecontroller.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:58:38 Støední Evropa (bìžný èas)

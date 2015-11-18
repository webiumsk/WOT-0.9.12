# 2015.11.18 11:58:38 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/Vibroeffects/Controllers/ShootingController.py
import BigWorld
from OnceController import OnceController
from debug_utils import *

class ShootingController:

    def __init__(self, caliber):
        if caliber < 50:
            OnceController('shot_small_veff')
        elif caliber < 57:
            OnceController('shot_medium_veff')
        elif caliber < 107:
            OnceController('shot_large_veff')
        else:
            OnceController('shot_main_veff')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\vibroeffects\controllers\shootingcontroller.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:58:38 Støední Evropa (bìžný èas)

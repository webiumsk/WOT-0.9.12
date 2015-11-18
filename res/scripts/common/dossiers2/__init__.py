# 2015.11.18 11:59:13 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/dossiers2/__init__.py
from dossiers2.common.utils import getDossierVersion
from dossiers2.custom import updaters
from dossiers2.custom.builders import *

def init():
    from dossiers2.custom import init as custom_init
    custom_init()
    from dossiers2.ui import init as ui_init
    ui_init()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\dossiers2\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:13 Støední Evropa (bìžný èas)

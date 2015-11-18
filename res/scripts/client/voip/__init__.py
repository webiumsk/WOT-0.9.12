# 2015.11.18 11:58:40 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/VOIP/__init__.py
import BigWorld
from VOIPManager import VOIPManager

def getVOIPManager():
    if not globals().has_key('__handler'):
        globals()['__handler'] = VOIPManager()
        BigWorld.VOIP.setHandler(__handler)
    return __handler
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\voip\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:58:40 Støední Evropa (bìžný èas)

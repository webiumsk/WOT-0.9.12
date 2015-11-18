# 2015.11.18 11:59:58 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/FX/__init__.py
"""
The FX module implements a data-driven special effects framework.

For more information, please refer to bigworld/docs/howto_SFX
"""
s_sectionProcessors = {}

def typeCheck(self, listOrType):
    return 1


import Actors
import Events
import Joints
from Effects._Effect import prerequisites
from Effects.OneShot import OneShot
from Effects.Persistent import Persistent
from Effects.Buffered import getBufferedOneShotEffect
from Effects.Buffered import bufferedOneShotEffect
from Effects.Buffered import cleanupBufferedEffects
from Effects.Buffered import outputOverruns
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\fx\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:58 Støední Evropa (bìžný èas)

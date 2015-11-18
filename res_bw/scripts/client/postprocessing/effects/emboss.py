# 2015.11.18 12:00:08 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/PostProcessing/Effects/Emboss.py
from PostProcessing.RenderTargets import *
from PostProcessing import Effect
from PostProcessing.Phases import build9TapFilterPhase
from PostProcessing.Phases import buildBackBufferCopyPhase
from PostProcessing.Phases import buildGreyscalePhase
from PostProcessing.FilterKernels import *
from PostProcessing.Effects import implementEffectFactory

@implementEffectFactory('Emboss', 'Run an emboss filter over the scene.')
def emboss():
    """This method creates and returns a post-process effect that performs
    greyscale embossing using a simple filter-kernel."""
    backBufferCopy = rt('PostProcessing/backBufferCopy')
    c = buildBackBufferCopyPhase(backBufferCopy)
    g = buildGreyscalePhase(backBufferCopy.texture, None)
    s = build9TapFilterPhase(backBufferCopy.texture, None, embossFilter)
    e = Effect()
    e.name = 'Emboss'
    e.phases = [c,
     g,
     c,
     s]
    return e
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\postprocessing\effects\emboss.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:00:08 St�edn� Evropa (b�n� �as)

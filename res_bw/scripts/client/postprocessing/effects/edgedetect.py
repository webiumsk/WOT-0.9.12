# 2015.11.18 12:00:07 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/PostProcessing/Effects/EdgeDetect.py
import BigWorld
from PostProcessing.RenderTargets import *
from PostProcessing import Effect
from PostProcessing.Phases import *
from PostProcessing.FilterKernels import *
from PostProcessing.Effects import implementEffectFactory

@implementEffectFactory('Edge detect', 'Detect and draw the edges in the scene.')
def edgeDetect():
    """This method creates and returns a post-process effect that performs
    edge detection and dilation of the resultant edges."""
    backBufferCopy = rt('PostProcessing/backBufferCopy')
    c = buildBackBufferCopyPhase(backBufferCopy)
    s = build9TapFilterPhase(backBufferCopy.texture, None, edgeDetectFilter)
    d = buildEdgeDilationPhase(backBufferCopy.texture, None)
    e = Effect()
    e.name = 'Edge Detect'
    e.phases = [c,
     s,
     c,
     d]
    return e
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\postprocessing\effects\edgedetect.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:00:07 St�edn� Evropa (b�n� �as)

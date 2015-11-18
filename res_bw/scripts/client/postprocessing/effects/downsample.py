# 2015.11.18 12:00:07 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/PostProcessing/Effects/DownSample.py
from PostProcessing.RenderTargets import *
from PostProcessing.Phases import *
from PostProcessing import Effect
from PostProcessing.Effects import implementEffectFactory

@implementEffectFactory('Down sample', 'Create 3 down-sampled copies of the scene and store them in intermediate textures.')
def downSample():
    """This method creates and returns an effect that down-samples the back-
    buffer.  This effect by itself doesn't achieve anything on its own,
    however having downsampled versions of the scene are usually for other
    effects.  It fills the downSample1/2/3 render targets and also leaves
    a copy of the back buffer in the backBufferCopy render target."""
    backBufferCopy = rt('PostProcessing/backBufferCopy')
    downSample1 = rt('PostProcessing/downSample1')
    downSample2 = rt('PostProcessing/downSample2')
    downSample3 = rt('PostProcessing/downSample3')
    pre = buildBackBufferCopyPhase(backBufferCopy)
    d0 = buildDownSamplePhase(backBufferCopy.texture, downSample1)
    d1 = buildDownSamplePhase(downSample1.texture, downSample2)
    d2 = buildDownSamplePhase(downSample2.texture, downSample3)
    e = Effect()
    e.name = 'Down Sample'
    phases = [pre,
     d0,
     d1,
     d2]
    e.phases = phases
    return e
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\postprocessing\effects\downsample.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:00:07 Støední Evropa (bìžný èas)

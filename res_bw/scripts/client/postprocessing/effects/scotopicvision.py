# 2015.11.18 12:00:09 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/PostProcessing/Effects/ScotopicVision.py
from PostProcessing.RenderTargets import *
from PostProcessing.Phases import *
from PostProcessing import Effect
from PostProcessing import chain
from PostProcessing.Effects.Properties import *
from PostProcessing.Effects import implementEffectFactory
import Math
noiseLevel = MaterialFloatProperty('Scotopic Vision', -1, 'noiseLevel')
noiseThreshold = MaterialFloatProperty('Scotopic Vision', -1, 'noiseThreshold')
textureScale = MaterialFloatProperty('Scotopic Vision', -1, 'noiseScale', 1)

@implementEffectFactory('Scotopic vision', 'Simulate human night vision, via tone-map desaturation and added noise.')
def scotopicVision(colName = 'system/maps/post_processing/scotopic_vision.dds', noiseName = 'system/maps/post_processing/noise.texanim'):
    """This method creates and returns a post-process effect that simulates
    scotopic vision, or human night vision.
    """
    backBufferCopy = rt('PostProcessing/backBufferCopy')
    backBufferCopyB = rt('PostProcessing/backBufferCopyB')
    e = Effect()
    e.name = 'Scotopic Vision'
    c = buildBackBufferCopyPhase(backBufferCopy)
    p = buildColourCorrectionPhase(backBufferCopy.texture, colName, backBufferCopyB)
    t = buildPhase(backBufferCopy.texture, None, 'shaders/post_processing/legacy/scotopic_vision.fx')
    t.name = 'scotopic vision'
    t.material.noiseTexture = noiseName
    t.material.colouredTexture = backBufferCopyB.texture
    v = buildVignettePhase()
    e.phases = [c,
     p,
     t,
     v]
    return e
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\postprocessing\effects\scotopicvision.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:00:09 St�edn� Evropa (b�n� �as)

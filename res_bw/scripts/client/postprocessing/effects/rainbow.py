# 2015.11.18 12:00:09 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/PostProcessing/Effects/Rainbow.py
from PostProcessing.RenderTargets import *
from PostProcessing import Effect
from PostProcessing.Phases import *
from PostProcessing.FilterKernels import *
from PostProcessing.Effects.Properties import *
from PostProcessing.Effects import implementEffectFactory
import Math
amount = MaterialFloatProperty('Rainbow', -1, 'rainbowAmount', primary=True)
dropletSize = MaterialFloatProperty('Rainbow', -1, 'dropSize')

@implementEffectFactory('Rainbow', 'Rainbow simulation.  Look directly away from the sun to see the effect.')
def rainbow():
    """This method creates and returns a post-process effect that draws
    a rainbow, using the angle between the camera and the sun and a MIE
    scattering diagram lookup texture.
    """
    backBufferCopy = rt('PostProcessing/backBufferCopy')
    c = buildBackBufferCopyPhase(backBufferCopy)
    r = buildPhase(backBufferCopy.texture, None, 'shaders/post_processing/legacy/rainbow.fx', straightTransfer4Tap, BW_BLEND_ONE, BW_BLEND_ONE)
    r.name = 'decode lee diagram'
    r.material.lookupTexture = 'system/maps/post_processing/lee_diagram.bmp'
    e = Effect()
    e.name = 'Rainbow'
    e.phases = [c, r]
    return e
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\postprocessing\effects\rainbow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:00:09 Støední Evropa (bìžný èas)

# 2015.11.18 12:00:09 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/PostProcessing/Effects/RegistrationTest.py
from PostProcessing.RenderTargets import *
from PostProcessing.Phases import *
from PostProcessing import Effect

def registrationTest():
    """This method creates and returns an effect that tests
    whether or not the transfer registration is correct.  It
    copies the back buffer and transfers it back over itself
    a few times in order to see if any pixels are shifted. In
    theory this should produce no visual effect at all"""
    c = buildBackBufferCopyPhase(backBufferCopy)
    t = buildTransferPhase(backBufferCopy.texture)
    e = Effect()
    e.name = 'Test Registration'
    phases = [c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t,
     c,
     t]
    e.phases = phases
    import Math
    e.bypass = Math.Vector4LFO()
    e.bypass.period = 2.0
    e.bypass.waveform = 'SQUARE'
    return e
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\postprocessing\effects\registrationtest.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:00:09 Støední Evropa (bìžný èas)

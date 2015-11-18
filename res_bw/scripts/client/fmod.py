# 2015.11.18 11:59:43 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/FMOD.py
enabled = True
try:
    from _FMOD import *
    import _FMOD
except ImportError:
    print 'WARNING: FMOD support is not enabled.'
    enabled = False

if enabled:
    import BigWorld
    BigWorld.getSound = getSound
    BigWorld.getSoundBanks = getSoundBanks
    BigWorld.playSound = playSound
    BigWorld.setDefaultSoundProject = setDefaultSoundProject
    BigWorld.loadSoundBankIntoMemory = loadSoundBankIntoMemory
    BigWorld.loadSoundBank = loadEventProject
    BigWorld.loadSoundGroup = loadSoundGroup
    BigWorld.reloadSoundBank = reloadEventProject
    BigWorld.unloadSoundBankFromMemory = unloadSoundBankFromMemory
    BigWorld.unloadSoundBank = unloadEventProject
    BigWorld.unloadSoundGroup = unloadSoundGroup
    BigWorld.setMasterVolume = setMasterVolume
    del BigWorld
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\fmod.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:43 Støední Evropa (bìžný èas)

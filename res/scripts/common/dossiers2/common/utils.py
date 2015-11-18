# 2015.11.18 11:59:15 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/dossiers2/common/utils.py
import struct

def getDossierVersion(dossierCompDescr, versionFormat, latestVersion):
    if dossierCompDescr == '':
        return latestVersion
    return struct.unpack_from(versionFormat, dossierCompDescr)[0]
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\dossiers2\common\utils.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:15 Støední Evropa (bìžný èas)

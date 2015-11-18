# 2015.11.18 12:01:31 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/sha.py
import warnings
warnings.warn('the sha module is deprecated; use the hashlib module instead', DeprecationWarning, 2)
from hashlib import sha1 as sha
new = sha
blocksize = 1
digest_size = 20
digestsize = 20
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\sha.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:01:31 Støední Evropa (bìžný èas)

# 2015.11.18 12:01:01 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/md5.py
import warnings
warnings.warn('the md5 module is deprecated; use hashlib instead', DeprecationWarning, 2)
from hashlib import md5
new = md5
blocksize = 1
digest_size = 16
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\md5.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:01:01 Støední Evropa (bìžný èas)

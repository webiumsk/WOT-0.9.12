# 2015.11.18 12:01:40 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/statvfs.py
"""Constants for interpreting the results of os.statvfs() and os.fstatvfs()."""
from warnings import warnpy3k
warnpy3k('the statvfs module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
F_BSIZE = 0
F_FRSIZE = 1
F_BLOCKS = 2
F_BFREE = 3
F_BAVAIL = 4
F_FILES = 5
F_FFREE = 6
F_FAVAIL = 7
F_FLAG = 8
F_NAMEMAX = 9
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\statvfs.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:01:40 Støední Evropa (bìžný èas)

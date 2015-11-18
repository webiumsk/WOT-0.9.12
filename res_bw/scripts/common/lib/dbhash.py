# 2015.11.18 12:00:32 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/dbhash.py
"""Provide a (g)dbm-compatible interface to bsddb.hashopen."""
import sys
import warnings
warnings.warnpy3k('in 3.x, the dbhash module has been removed', stacklevel=2)
try:
    import bsddb
except ImportError:
    del sys.modules[__name__]
    raise

__all__ = ['error', 'open']
error = bsddb.error

def open(file, flag = 'r', mode = 438):
    return bsddb.hashopen(file, flag, mode)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\dbhash.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:00:32 Støední Evropa (bìžný èas)

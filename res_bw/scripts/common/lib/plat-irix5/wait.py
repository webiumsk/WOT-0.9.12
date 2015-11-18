# 2015.11.18 12:05:37 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/plat-irix5/WAIT.py
from warnings import warnpy3k
warnpy3k('the WAIT module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
_WSTOPPED = 127
WNOHANG = 64
WEXITED = 1
WTRAPPED = 2
WSTOPPED = 4
WCONTINUED = 8
WNOWAIT = 128
WOPTMASK = WEXITED | WTRAPPED | WSTOPPED | WCONTINUED | WNOHANG | WNOWAIT
WSTOPFLG = 127
WCONTFLG = 65535
WCOREFLAG = 128
WSIGMASK = 127
WUNTRACED = 4
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\plat-irix5\wait.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:05:37 Støední Evropa (bìžný èas)

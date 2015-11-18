# 2015.11.18 12:05:45 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/plat-mac/appletrunner.py
from warnings import warnpy3k
warnpy3k('In 3.x, the appletrunner module is removed.', stacklevel=2)
import os
import sys
for name in ['__rawmain__.py',
 '__rawmain__.pyc',
 '__main__.py',
 '__main__.pyc']:
    realmain = os.path.join(os.path.dirname(os.path.dirname(sys.argv[0])), 'Resources', name)
    if os.path.exists(realmain):
        break
else:
    sys.stderr.write('%s: cannot find applet main program\n' % sys.argv[0])
    sys.exit(1)

sys.argv.insert(1, realmain)
os.execve(sys.executable, sys.argv, os.environ)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\plat-mac\appletrunner.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:05:45 Støední Evropa (bìžný èas)

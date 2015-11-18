# 2015.11.18 12:04:52 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_getcwdu.py
"""
Fixer that changes os.getcwdu() to os.getcwd().
"""
from .. import fixer_base
from ..fixer_util import Name

class FixGetcwdu(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n              power< 'os' trailer< dot='.' name='getcwdu' > any* >\n              "

    def transform(self, node, results):
        name = results['name']
        name.replace(Name(u'getcwd', prefix=name.prefix))
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\lib2to3\fixes\fix_getcwdu.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:04:52 Støední Evropa (bìžný èas)

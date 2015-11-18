# 2015.11.18 12:04:54 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_input.py
"""Fixer that changes input(...) into eval(input(...))."""
from .. import fixer_base
from ..fixer_util import Call, Name
from .. import patcomp
context = patcomp.compile_pattern("power< 'eval' trailer< '(' any ')' > >")

class FixInput(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n              power< 'input' args=trailer< '(' [any] ')' > >\n              "

    def transform(self, node, results):
        if context.match(node.parent.parent):
            return
        new = node.clone()
        new.prefix = u''
        return Call(Name(u'eval'), [new], prefix=node.prefix)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\lib2to3\fixes\fix_input.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:04:54 Støední Evropa (bìžný èas)

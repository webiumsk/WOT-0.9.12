# 2015.11.18 12:04:57 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_repr.py
"""Fixer that transforms `xyzzy` into repr(xyzzy)."""
from .. import fixer_base
from ..fixer_util import Call, Name, parenthesize

class FixRepr(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n              atom < '`' expr=any '`' >\n              "

    def transform(self, node, results):
        expr = results['expr'].clone()
        if expr.type == self.syms.testlist1:
            expr = parenthesize(expr)
        return Call(Name(u'repr'), [expr], prefix=node.prefix)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\lib2to3\fixes\fix_repr.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:04:57 St�edn� Evropa (b�n� �as)

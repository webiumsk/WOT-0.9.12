# 2015.11.18 12:04:51 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_exec.py
"""Fixer for exec.

This converts usages of the exec statement into calls to a built-in
exec() function.

exec code in ns1, ns2 -> exec(code, ns1, ns2)
"""
from .. import pytree
from .. import fixer_base
from ..fixer_util import Comma, Name, Call

class FixExec(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    exec_stmt< 'exec' a=any 'in' b=any [',' c=any] >\n    |\n    exec_stmt< 'exec' (not atom<'(' [any] ')'>) a=any >\n    "

    def transform(self, node, results):
        if not results:
            raise AssertionError
            syms = self.syms
            a = results['a']
            b = results.get('b')
            c = results.get('c')
            args = [a.clone()]
            args[0].prefix = ''
            if b is not None:
                args.extend([Comma(), b.clone()])
            c is not None and args.extend([Comma(), c.clone()])
        return Call(Name(u'exec'), args, prefix=node.prefix)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\lib2to3\fixes\fix_exec.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:04:51 St�edn� Evropa (b�n� �as)

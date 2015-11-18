# 2015.11.18 12:04:51 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_callable.py
"""Fixer for callable().

This converts callable(obj) into isinstance(obj, collections.Callable), adding a
collections import if needed."""
from lib2to3 import fixer_base
from lib2to3.fixer_util import Call, Name, String, Attr, touch_import

class FixCallable(fixer_base.BaseFix):
    BM_compatible = True
    order = 'pre'
    PATTERN = "\n    power< 'callable'\n           trailer< lpar='('\n                    ( not(arglist | argument<any '=' any>) func=any\n                      | func=arglist<(not argument<any '=' any>) any ','> )\n                    rpar=')' >\n           after=any*\n    >\n    "

    def transform(self, node, results):
        func = results['func']
        touch_import(None, u'collections', node=node)
        args = [func.clone(), String(u', ')]
        args.extend(Attr(Name(u'collections'), Name(u'Callable')))
        return Call(Name(u'isinstance'), args, prefix=node.prefix)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\lib2to3\fixes\fix_callable.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:04:51 St�edn� Evropa (b�n� �as)

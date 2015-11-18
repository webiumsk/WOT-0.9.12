# 2015.11.18 12:04:56 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_numliterals.py
"""Fixer that turns 1L into 1, 0755 into 0o755.
"""
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Number

class FixNumliterals(fixer_base.BaseFix):
    _accept_type = token.NUMBER

    def match(self, node):
        return node.value.startswith(u'0') or node.value[-1] in u'Ll'

    def transform(self, node, results):
        val = node.value
        if val[-1] in u'Ll':
            val = val[:-1]
        elif val.startswith(u'0') and val.isdigit() and len(set(val)) > 1:
            val = u'0o' + val[1:]
        return Number(val, prefix=node.prefix)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\lib2to3\fixes\fix_numliterals.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:04:56 St�edn� Evropa (b�n� �as)

# 2015.11.18 12:04:55 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_ne.py
"""Fixer that turns <> into !=."""
from .. import pytree
from ..pgen2 import token
from .. import fixer_base

class FixNe(fixer_base.BaseFix):
    _accept_type = token.NOTEQUAL

    def match(self, node):
        return node.value == u'<>'

    def transform(self, node, results):
        new = pytree.Leaf(token.NOTEQUAL, u'!=', prefix=node.prefix)
        return new
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\lib2to3\fixes\fix_ne.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:04:55 Støední Evropa (bìžný èas)

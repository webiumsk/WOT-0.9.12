# 2015.11.18 12:04:56 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_print.py
"""Fixer for print.

Change:
    'print'          into 'print()'
    'print ...'      into 'print(...)'
    'print ... ,'    into 'print(..., end=" ")'
    'print >>x, ...' into 'print(..., file=x)'

No changes are applied if print_function is imported from __future__

"""
from .. import patcomp
from .. import pytree
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Name, Call, Comma, String, is_tuple
parend_expr = patcomp.compile_pattern("atom< '(' [atom|STRING|NAME] ')' >")

class FixPrint(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n              simple_stmt< any* bare='print' any* > | print_stmt\n              "

    def transform(self, node, results):
        if not results:
            raise AssertionError
            bare_print = results.get('bare')
            bare_print and bare_print.replace(Call(Name(u'print'), [], prefix=bare_print.prefix))
            return
        else:
            if not node.children[0] == Name(u'print'):
                raise AssertionError
                args = node.children[1:]
                if len(args) == 1 and parend_expr.match(args[0]):
                    return
                sep = end = file = None
                if args and args[-1] == Comma():
                    args = args[:-1]
                    end = ' '
                if args and args[0] == pytree.Leaf(token.RIGHTSHIFT, u'>>'):
                    if not len(args) >= 2:
                        raise AssertionError
                        file = args[1].clone()
                        args = args[3:]
                    l_args = [ arg.clone() for arg in args ]
                    if l_args:
                        l_args[0].prefix = u''
                    if sep is not None or end is not None or file is not None:
                        if sep is not None:
                            self.add_kwarg(l_args, u'sep', String(repr(sep)))
                        end is not None and self.add_kwarg(l_args, u'end', String(repr(end)))
                    file is not None and self.add_kwarg(l_args, u'file', file)
            n_stmt = Call(Name(u'print'), l_args)
            n_stmt.prefix = node.prefix
            return n_stmt

    def add_kwarg(self, l_nodes, s_kwd, n_expr):
        n_expr.prefix = u''
        n_argument = pytree.Node(self.syms.argument, (Name(s_kwd), pytree.Leaf(token.EQUAL, u'='), n_expr))
        if l_nodes:
            l_nodes.append(Comma())
            n_argument.prefix = u' '
        l_nodes.append(n_argument)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\lib2to3\fixes\fix_print.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:04:56 St�edn� Evropa (b�n� �as)

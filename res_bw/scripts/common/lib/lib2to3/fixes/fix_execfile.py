# 2015.11.18 12:04:52 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_execfile.py
"""Fixer for execfile.

This converts usages of the execfile function into calls to the built-in
exec() function.
"""
from .. import fixer_base
from ..fixer_util import Comma, Name, Call, LParen, RParen, Dot, Node, ArgList, String, syms

class FixExecfile(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    power< 'execfile' trailer< '(' arglist< filename=any [',' globals=any [',' locals=any ] ] > ')' > >\n    |\n    power< 'execfile' trailer< '(' filename=any ')' > >\n    "

    def transform(self, node, results):
        if not results:
            raise AssertionError
            filename = results['filename']
            globals = results.get('globals')
            locals = results.get('locals')
            execfile_paren = node.children[-1].children[-1].clone()
            open_args = ArgList([filename.clone()], rparen=execfile_paren)
            open_call = Node(syms.power, [Name(u'open'), open_args])
            read = [Node(syms.trailer, [Dot(), Name(u'read')]), Node(syms.trailer, [LParen(), RParen()])]
            open_expr = [open_call] + read
            filename_arg = filename.clone()
            filename_arg.prefix = u' '
            exec_str = String(u"'exec'", u' ')
            compile_args = open_expr + [Comma(),
             filename_arg,
             Comma(),
             exec_str]
            compile_call = Call(Name(u'compile'), compile_args, u'')
            args = [compile_call]
            if globals is not None:
                args.extend([Comma(), globals.clone()])
            locals is not None and args.extend([Comma(), locals.clone()])
        return Call(Name(u'exec'), args, prefix=node.prefix)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\lib2to3\fixes\fix_execfile.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:04:52 St�edn� Evropa (b�n� �as)

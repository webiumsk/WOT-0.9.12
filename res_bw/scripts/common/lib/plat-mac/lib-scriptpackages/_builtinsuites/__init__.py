# 2015.11.18 12:06:21 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/plat-mac/lib-scriptpackages/_builtinSuites/__init__.py
"""
Manually generated suite used as base class for StdSuites Required and Standard
suites. This is needed because the events and enums in this suite belong
in the Required suite according to the Apple docs, but they often seem to be
in the Standard suite.
"""
from warnings import warnpy3k
warnpy3k('In 3.x, the _builtinSuites module is removed.', stacklevel=2)
import aetools
import builtin_Suite
_code_to_module = {'reqd': builtin_Suite,
 'core': builtin_Suite}
_code_to_fullname = {'reqd': ('_builtinSuites.builtin_Suite', 'builtin_Suite'),
 'core': ('_builtinSuites.builtin_Suite', 'builtin_Suite')}
from builtin_Suite import *

class _builtinSuites(builtin_Suite_Events, aetools.TalkTo):
    _signature = 'ascr'
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\plat-mac\lib-scriptpackages\_builtinsuites\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:06:21 St�edn� Evropa (b�n� �as)

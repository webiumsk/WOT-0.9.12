# 2015.11.18 12:01:05 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/new.py
"""Create new objects of various types.  Deprecated.

This module is no longer required except for backward compatibility.
Objects of most types can now be created by calling the type object.
"""
from warnings import warnpy3k
warnpy3k("The 'new' module has been removed in Python 3.0; use the 'types' module instead.", stacklevel=2)
del warnpy3k
from types import ClassType as classobj
from types import FunctionType as function
from types import InstanceType as instance
from types import MethodType as instancemethod
from types import ModuleType as module
from types import CodeType as code
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\new.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:01:05 Støední Evropa (bìžný èas)

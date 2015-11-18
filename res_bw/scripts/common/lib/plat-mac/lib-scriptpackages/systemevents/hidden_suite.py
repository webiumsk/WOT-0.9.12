# 2015.11.18 12:06:18 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/plat-mac/lib-scriptpackages/SystemEvents/Hidden_Suite.py
"""Suite Hidden Suite: Hidden Terms and Events for controlling the System Events application
Level 1, version 1

Generated from /System/Library/CoreServices/System Events.app
AETE/AEUT resource version 1/0, language 0, script 0
"""
import aetools
import MacOS
_code = 'tpnm'
from StdSuites.Type_Names_Suite import *

class Hidden_Suite_Events(Type_Names_Suite_Events):

    def do_script(self, _object, _attributes = {}, **_arguments):
        """do script: Execute an OSA script.
        Required argument: the object for the command
        Keyword argument _attributes: AppleEvent attribute dictionary
        """
        _code = 'misc'
        _subcode = 'dosc'
        if _arguments:
            raise TypeError, 'No optional args expected'
        _arguments['----'] = _object
        _reply, _arguments, _attributes = self.send(_code, _subcode, _arguments, _attributes)
        if _arguments.get('errn', 0):
            raise aetools.Error, aetools.decodeerror(_arguments)
        if _arguments.has_key('----'):
            return _arguments['----']


_classdeclarations = {}
_propdeclarations = {}
_compdeclarations = {}
_enumdeclarations = {}
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\plat-mac\lib-scriptpackages\systemevents\hidden_suite.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:06:18 Støední Evropa (bìžný èas)

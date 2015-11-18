# 2015.11.18 12:06:09 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/plat-mac/lib-scriptpackages/CodeWarrior/Required.py
"""Suite Required: Terms that every application should support
Level 1, version 1

Generated from /Volumes/Sap/Applications (Mac OS 9)/Metrowerks CodeWarrior 7.0/Metrowerks CodeWarrior/CodeWarrior IDE 4.2.5
AETE/AEUT resource version 1/0, language 0, script 0
"""
import aetools
import MacOS
_code = 'reqd'
from StdSuites.Required_Suite import *

class Required_Events(Required_Suite_Events):
    _argmap_open = {'converting': 'Conv'}

    def open(self, _object, _attributes = {}, **_arguments):
        """open: Open the specified object(s)
        Required argument: list of objects to open
        Keyword argument converting: Whether to convert project to latest version (yes/no; default is ask).
        Keyword argument _attributes: AppleEvent attribute dictionary
        """
        _code = 'aevt'
        _subcode = 'odoc'
        aetools.keysubst(_arguments, self._argmap_open)
        _arguments['----'] = _object
        aetools.enumsubst(_arguments, 'Conv', _Enum_Conv)
        _reply, _arguments, _attributes = self.send(_code, _subcode, _arguments, _attributes)
        if _arguments.get('errn', 0):
            raise aetools.Error, aetools.decodeerror(_arguments)
        if _arguments.has_key('----'):
            return _arguments['----']


_Enum_Conv = {'yes': 'yes ',
 'no': 'no  '}
_classdeclarations = {}
_propdeclarations = {}
_compdeclarations = {}
_enumdeclarations = {'Conv': _Enum_Conv}
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\plat-mac\lib-scriptpackages\codewarrior\required.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:06:09 St�edn� Evropa (b�n� �as)

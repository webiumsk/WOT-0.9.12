# 2015.11.18 12:06:13 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/plat-mac/lib-scriptpackages/Netscape/PowerPlant.py
"""Suite PowerPlant:
Level 0, version 0

Generated from /Volumes/Sap/Applications (Mac OS 9)/Netscape Communicator\xe2\x84\xa2 Folder/Netscape Communicator\xe2\x84\xa2
AETE/AEUT resource version 1/0, language 0, script 0
"""
import aetools
import MacOS
_code = 'ppnt'

class PowerPlant_Events:
    _argmap_SwitchTellTarget = {'to': 'data'}

    def SwitchTellTarget(self, _no_object = None, _attributes = {}, **_arguments):
        """SwitchTellTarget: Makes an object the \xd2focus\xd3 of AppleEvents
        Keyword argument to: reference to new focus of AppleEvents
        Keyword argument _attributes: AppleEvent attribute dictionary
        """
        _code = 'ppnt'
        _subcode = 'sttg'
        aetools.keysubst(_arguments, self._argmap_SwitchTellTarget)
        if _no_object is not None:
            raise TypeError, 'No direct arg expected'
        _reply, _arguments, _attributes = self.send(_code, _subcode, _arguments, _attributes)
        if _arguments.get('errn', 0):
            raise aetools.Error, aetools.decodeerror(_arguments)
        if _arguments.has_key('----'):
            return _arguments['----']
        else:
            return

    _argmap_select = {'data': 'data'}

    def select(self, _object, _attributes = {}, **_arguments):
        """select: Sets the present selection
        Required argument: object to select or container of sub-objects to select
        Keyword argument data: sub-object(s) to select
        Keyword argument _attributes: AppleEvent attribute dictionary
        """
        _code = 'misc'
        _subcode = 'slct'
        aetools.keysubst(_arguments, self._argmap_select)
        _arguments['----'] = _object
        _reply, _arguments, _attributes = self.send(_code, _subcode, _arguments, _attributes)
        if _arguments.get('errn', 0):
            raise aetools.Error, aetools.decodeerror(_arguments)
        if _arguments.has_key('----'):
            return _arguments['----']


_Enum_dbac = {'DoNothing': '\x00\x00\x00\x00',
 'PostAlert': '\x00\x00\x00\x01',
 'LowLevelDebugger': '\x00\x00\x00\x02',
 'SourceDebugger': '\x00\x00\x00\x03'}
_classdeclarations = {}
_propdeclarations = {}
_compdeclarations = {}
_enumdeclarations = {'dbac': _Enum_dbac}
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\plat-mac\lib-scriptpackages\netscape\powerplant.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:06:13 St�edn� Evropa (b�n� �as)

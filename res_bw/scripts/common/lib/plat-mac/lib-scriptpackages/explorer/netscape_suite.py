# 2015.11.18 12:06:10 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/plat-mac/lib-scriptpackages/Explorer/Netscape_Suite.py
"""Suite Netscape Suite: Events defined by Netscape
Level 1, version 1

Generated from /Applications/Internet Explorer.app
AETE/AEUT resource version 1/0, language 0, script 0
"""
import aetools
import MacOS
_code = 'MOSS'

class Netscape_Suite_Events:

    def Open_bookmark(self, _object = None, _attributes = {}, **_arguments):
        """Open bookmark: Opens a bookmark file
        Required argument: If not available, reloads the current bookmark file
        Keyword argument _attributes: AppleEvent attribute dictionary
        """
        _code = 'MOSS'
        _subcode = 'book'
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
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\plat-mac\lib-scriptpackages\explorer\netscape_suite.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:06:10 St�edn� Evropa (b�n� �as)

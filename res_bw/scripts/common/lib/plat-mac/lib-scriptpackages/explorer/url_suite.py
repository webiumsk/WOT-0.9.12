# 2015.11.18 12:06:10 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/plat-mac/lib-scriptpackages/Explorer/URL_Suite.py
"""Suite URL Suite: Standard suite for Uniform Resource Locators
Level 1, version 1

Generated from /Applications/Internet Explorer.app
AETE/AEUT resource version 1/0, language 0, script 0
"""
import aetools
import MacOS
_code = 'GURL'

class URL_Suite_Events:
    _argmap_GetURL = {'to': 'dest'}

    def GetURL(self, _object, _attributes = {}, **_arguments):
        """GetURL: Open the URL (and optionally save it to disk)
        Required argument: URL to open
        Keyword argument to: File into which to save resource located at URL.
        Keyword argument _attributes: AppleEvent attribute dictionary
        """
        _code = 'GURL'
        _subcode = 'GURL'
        aetools.keysubst(_arguments, self._argmap_GetURL)
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
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\plat-mac\lib-scriptpackages\explorer\url_suite.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:06:10 St�edn� Evropa (b�n� �as)

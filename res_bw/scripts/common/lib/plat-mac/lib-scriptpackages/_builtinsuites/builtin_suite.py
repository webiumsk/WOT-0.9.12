# 2015.11.18 12:06:20 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/plat-mac/lib-scriptpackages/_builtinSuites/builtin_Suite.py
"""Suite builtin_Suite: Every application supports open, reopen, print, run, and quit
Level 1, version 1
"""
import aetools
import MacOS
_code = 'aevt'

class builtin_Suite_Events:

    def open(self, _object, _attributes = {}, **_arguments):
        """open: Open the specified object(s)
        Required argument: list of objects to open
        Keyword argument _attributes: AppleEvent attribute dictionary
        """
        _code = 'aevt'
        _subcode = 'odoc'
        if _arguments:
            raise TypeError, 'No optional args expected'
        _arguments['----'] = _object
        _reply, _arguments, _attributes = self.send(_code, _subcode, _arguments, _attributes)
        if _arguments.get('errn', 0):
            raise aetools.Error, aetools.decodeerror(_arguments)
        if _arguments.has_key('----'):
            return _arguments['----']

    def run(self, _no_object = None, _attributes = {}, **_arguments):
        """run: Run an application.      Most applications will open an empty, untitled window.
        Keyword argument _attributes: AppleEvent attribute dictionary
        """
        _code = 'aevt'
        _subcode = 'oapp'
        if _arguments:
            raise TypeError, 'No optional args expected'
        if _no_object is not None:
            raise TypeError, 'No direct arg expected'
        _reply, _arguments, _attributes = self.send(_code, _subcode, _arguments, _attributes)
        if _arguments.get('errn', 0):
            raise aetools.Error, aetools.decodeerror(_arguments)
        if _arguments.has_key('----'):
            return _arguments['----']
        else:
            return

    def reopen(self, _no_object = None, _attributes = {}, **_arguments):
        """reopen: Reactivate a running application.  Some applications will open a new untitled window if no window is open.
        Keyword argument _attributes: AppleEvent attribute dictionary
        """
        _code = 'aevt'
        _subcode = 'rapp'
        if _arguments:
            raise TypeError, 'No optional args expected'
        if _no_object is not None:
            raise TypeError, 'No direct arg expected'
        _reply, _arguments, _attributes = self.send(_code, _subcode, _arguments, _attributes)
        if _arguments.get('errn', 0):
            raise aetools.Error, aetools.decodeerror(_arguments)
        if _arguments.has_key('----'):
            return _arguments['----']
        else:
            return

    def _print(self, _object, _attributes = {}, **_arguments):
        """print: Print the specified object(s)
        Required argument: list of objects to print
        Keyword argument _attributes: AppleEvent attribute dictionary
        """
        _code = 'aevt'
        _subcode = 'pdoc'
        if _arguments:
            raise TypeError, 'No optional args expected'
        _arguments['----'] = _object
        _reply, _arguments, _attributes = self.send(_code, _subcode, _arguments, _attributes)
        if _arguments.get('errn', 0):
            raise aetools.Error, aetools.decodeerror(_arguments)
        if _arguments.has_key('----'):
            return _arguments['----']

    _argmap_quit = {'saving': 'savo'}

    def quit(self, _no_object = None, _attributes = {}, **_arguments):
        """quit: Quit an application
        Keyword argument saving: specifies whether to save currently open documents
        Keyword argument _attributes: AppleEvent attribute dictionary
        """
        _code = 'aevt'
        _subcode = 'quit'
        aetools.keysubst(_arguments, self._argmap_quit)
        if _no_object is not None:
            raise TypeError, 'No direct arg expected'
        aetools.enumsubst(_arguments, 'savo', _Enum_savo)
        _reply, _arguments, _attributes = self.send(_code, _subcode, _arguments, _attributes)
        if _arguments.get('errn', 0):
            raise aetools.Error, aetools.decodeerror(_arguments)
        if _arguments.has_key('----'):
            return _arguments['----']
        else:
            return

    _argmap_close = {'saving': 'savo',
     'saving_in': 'kfil'}


_Enum_savo = {'yes': 'yes ',
 'no': 'no      ',
 'ask': 'ask '}
_classdeclarations = {}
_propdeclarations = {}
_compdeclarations = {}
_enumdeclarations = {'savo': _Enum_savo}
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\plat-mac\lib-scriptpackages\_builtinsuites\builtin_suite.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:06:20 St�edn� Evropa (b�n� �as)

# 2015.11.18 12:06:19 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/plat-mac/lib-scriptpackages/SystemEvents/System_Events_Suite.py
"""Suite System Events Suite: Terms and Events for controlling the System Events application
Level 1, version 1

Generated from /System/Library/CoreServices/System Events.app
AETE/AEUT resource version 1/0, language 0, script 0
"""
import aetools
import MacOS
_code = 'sevs'

class System_Events_Suite_Events:

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


class application(aetools.ComponentItem):
    """application - The System Events application """
    want = 'capp'


class _Prop__3c_Inheritance_3e_(aetools.NProperty):
    """<Inheritance> - All of the properties of the superclass. """
    which = 'c@#^'
    want = 'capp'


_3c_Inheritance_3e_ = _Prop__3c_Inheritance_3e_()

class _Prop_folder_actions_enabled(aetools.NProperty):
    """folder actions enabled - Are Folder Actions currently being processed? """
    which = 'faen'
    want = 'bool'


folder_actions_enabled = _Prop_folder_actions_enabled()

class _Prop_properties(aetools.NProperty):
    """properties - every property of the System Events application """
    which = 'pALL'
    want = '****'


properties = _Prop_properties()
applications = application
application._superclassnames = []
import Disk_Folder_File_Suite
import Standard_Suite
import Folder_Actions_Suite
import Login_Items_Suite
import Processes_Suite
application._privpropdict = {'_3c_Inheritance_3e_': _Prop__3c_Inheritance_3e_,
 'folder_actions_enabled': _Prop_folder_actions_enabled,
 'properties': _Prop_properties}
application._privelemdict = {'application_process': Processes_Suite.application_process,
 'desk_accessory_process': Processes_Suite.desk_accessory_process,
 'disk': Disk_Folder_File_Suite.disk,
 'document': Standard_Suite.document,
 'file': Disk_Folder_File_Suite.file,
 'folder': Disk_Folder_File_Suite.folder,
 'folder_action': Folder_Actions_Suite.folder_action,
 'item': Disk_Folder_File_Suite.item,
 'login_item': Login_Items_Suite.login_item,
 'process': Processes_Suite.process,
 'window': Standard_Suite.window}
_classdeclarations = {'capp': application}
_propdeclarations = {'c@#^': _Prop__3c_Inheritance_3e_,
 'faen': _Prop_folder_actions_enabled,
 'pALL': _Prop_properties}
_compdeclarations = {}
_enumdeclarations = {}
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\plat-mac\lib-scriptpackages\systemevents\system_events_suite.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:06:19 St�edn� Evropa (b�n� �as)

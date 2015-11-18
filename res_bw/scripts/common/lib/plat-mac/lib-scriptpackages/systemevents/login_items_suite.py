# 2015.11.18 12:06:18 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/plat-mac/lib-scriptpackages/SystemEvents/Login_Items_Suite.py
"""Suite Login Items Suite: Terms and Events for controlling the Login Items application
Level 1, version 1

Generated from /System/Library/CoreServices/System Events.app
AETE/AEUT resource version 1/0, language 0, script 0
"""
import aetools
import MacOS
_code = 'logi'

class Login_Items_Suite_Events:
    pass


class login_item(aetools.ComponentItem):
    """login item - an item to be launched or opened at login """
    want = 'logi'


class _Prop__3c_Inheritance_3e_(aetools.NProperty):
    """<Inheritance> - All of the properties of the superclass. """
    which = 'c@#^'
    want = 'cobj'


class _Prop_hidden(aetools.NProperty):
    """hidden - Is the Login Item hidden when launched? """
    which = 'hidn'
    want = 'bool'


class _Prop_kind(aetools.NProperty):
    """kind - the file type of the Login Item """
    which = 'kind'
    want = 'utxt'


class _Prop_name(aetools.NProperty):
    """name - the name of the Login Item """
    which = 'pnam'
    want = 'utxt'


class _Prop_path(aetools.NProperty):
    """path - the file system path to the Login Item """
    which = 'ppth'
    want = 'utxt'


login_items = login_item
import Standard_Suite
login_item._superclassnames = ['item']
login_item._privpropdict = {'_3c_Inheritance_3e_': _Prop__3c_Inheritance_3e_,
 'hidden': _Prop_hidden,
 'kind': _Prop_kind,
 'name': _Prop_name,
 'path': _Prop_path}
login_item._privelemdict = {}
_classdeclarations = {'logi': login_item}
_propdeclarations = {'c@#^': _Prop__3c_Inheritance_3e_,
 'hidn': _Prop_hidden,
 'kind': _Prop_kind,
 'pnam': _Prop_name,
 'ppth': _Prop_path}
_compdeclarations = {}
_enumdeclarations = {}
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\plat-mac\lib-scriptpackages\systemevents\login_items_suite.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:06:18 St�edn� Evropa (b�n� �as)

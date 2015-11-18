# 2015.11.18 12:04:58 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_types.py
"""Fixer for removing uses of the types module.

These work for only the known names in the types module.  The forms above
can include types. or not.  ie, It is assumed the module is imported either as:

    import types
    from types import ... # either * or specific types

The import statements are not modified.

There should be another fixer that handles at least the following constants:

   type([]) -> list
   type(()) -> tuple
   type('') -> str

"""
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Name
_TYPE_MAPPING = {'BooleanType': 'bool',
 'BufferType': 'memoryview',
 'ClassType': 'type',
 'ComplexType': 'complex',
 'DictType': 'dict',
 'DictionaryType': 'dict',
 'EllipsisType': 'type(Ellipsis)',
 'FloatType': 'float',
 'IntType': 'int',
 'ListType': 'list',
 'LongType': 'int',
 'ObjectType': 'object',
 'NoneType': 'type(None)',
 'NotImplementedType': 'type(NotImplemented)',
 'SliceType': 'slice',
 'StringType': 'bytes',
 'StringTypes': 'str',
 'TupleType': 'tuple',
 'TypeType': 'type',
 'UnicodeType': 'str',
 'XRangeType': 'range'}
_pats = [ "power< 'types' trailer< '.' name='%s' > >" % t for t in _TYPE_MAPPING ]

class FixTypes(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = '|'.join(_pats)

    def transform(self, node, results):
        new_value = unicode(_TYPE_MAPPING.get(results['name'].value))
        if new_value:
            return Name(new_value, prefix=node.prefix)
        else:
            return None
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\lib2to3\fixes\fix_types.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:04:58 St�edn� Evropa (b�n� �as)

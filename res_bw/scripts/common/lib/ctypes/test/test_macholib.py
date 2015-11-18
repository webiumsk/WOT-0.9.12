# 2015.11.18 12:02:44 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/ctypes/test/test_macholib.py
import os
import sys
import unittest
from ctypes.macholib.dyld import dyld_find

def find_lib(name):
    possible = ['lib' + name + '.dylib', name + '.dylib', name + '.framework/' + name]
    for dylib in possible:
        try:
            return os.path.realpath(dyld_find(dylib))
        except ValueError:
            pass

    raise ValueError('%s not found' % (name,))


class MachOTest(unittest.TestCase):
    if sys.platform == 'darwin':

        def test_find(self):
            self.assertEqual(find_lib('pthread'), '/usr/lib/libSystem.B.dylib')
            result = find_lib('z')
            self.assertRegexpMatches(result, '.*/lib/libz\\..*.*\\.dylib')
            self.assertEqual(find_lib('IOKit'), '/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit')


if __name__ == '__main__':
    unittest.main()
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\ctypes\test\test_macholib.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:02:44 Støední Evropa (bìžný èas)

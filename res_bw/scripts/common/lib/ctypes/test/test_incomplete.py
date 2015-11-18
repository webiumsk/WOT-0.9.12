# 2015.11.18 12:02:42 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/ctypes/test/test_incomplete.py
import unittest
from ctypes import *

class MyTestCase(unittest.TestCase):

    def test_incomplete_example(self):
        lpcell = POINTER('cell')

        class cell(Structure):
            _fields_ = [('name', c_char_p), ('next', lpcell)]

        SetPointerType(lpcell, cell)
        c1 = cell()
        c1.name = 'foo'
        c2 = cell()
        c2.name = 'bar'
        c1.next = pointer(c2)
        c2.next = pointer(c1)
        p = c1
        result = []
        for i in range(8):
            result.append(p.name)
            p = p.next[0]

        self.assertEqual(result, ['foo', 'bar'] * 4)
        from ctypes import _pointer_type_cache
        del _pointer_type_cache[cell]


if __name__ == '__main__':
    unittest.main()
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\ctypes\test\test_incomplete.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:02:42 Støední Evropa (bìžný èas)

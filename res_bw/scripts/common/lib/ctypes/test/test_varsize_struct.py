# 2015.11.18 12:02:49 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/ctypes/test/test_varsize_struct.py
from ctypes import *
import unittest

class VarSizeTest(unittest.TestCase):

    def test_resize(self):

        class X(Structure):
            _fields_ = [('item', c_int), ('array', c_int * 1)]

        self.assertEqual(sizeof(X), sizeof(c_int) * 2)
        x = X()
        x.item = 42
        x.array[0] = 100
        self.assertEqual(sizeof(x), sizeof(c_int) * 2)
        new_size = sizeof(X) + sizeof(c_int) * 1
        resize(x, new_size)
        self.assertEqual(sizeof(x), new_size)
        self.assertEqual((x.item, x.array[0]), (42, 100))
        new_size = sizeof(X) + sizeof(c_int) * 9
        resize(x, new_size)
        self.assertEqual(sizeof(x), new_size)
        self.assertEqual((x.item, x.array[0]), (42, 100))
        new_size = sizeof(X) + sizeof(c_int) * 1
        resize(x, new_size)
        self.assertEqual(sizeof(x), new_size)
        self.assertEqual((x.item, x.array[0]), (42, 100))

    def test_array_invalid_length(self):
        self.assertRaises(ValueError, lambda : c_int * -1)
        self.assertRaises(ValueError, lambda : c_int * -3)

    def test_zerosized_array(self):
        array = (c_int * 0)()
        self.assertRaises(IndexError, array.__setitem__, 0, None)
        self.assertRaises(IndexError, array.__getitem__, 0)
        self.assertRaises(IndexError, array.__setitem__, 1, None)
        self.assertRaises(IndexError, array.__getitem__, 1)
        self.assertRaises(IndexError, array.__setitem__, -1, None)
        self.assertRaises(IndexError, array.__getitem__, -1)
        return


if __name__ == '__main__':
    unittest.main()
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\ctypes\test\test_varsize_struct.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:02:49 St�edn� Evropa (b�n� �as)

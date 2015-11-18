# 2015.11.18 12:02:47 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/ctypes/test/test_sizes.py
from ctypes import *
import sys
import unittest

class SizesTestCase(unittest.TestCase):

    def test_8(self):
        self.assertEqual(1, sizeof(c_int8))
        self.assertEqual(1, sizeof(c_uint8))

    def test_16(self):
        self.assertEqual(2, sizeof(c_int16))
        self.assertEqual(2, sizeof(c_uint16))

    def test_32(self):
        self.assertEqual(4, sizeof(c_int32))
        self.assertEqual(4, sizeof(c_uint32))

    def test_64(self):
        self.assertEqual(8, sizeof(c_int64))
        self.assertEqual(8, sizeof(c_uint64))

    def test_size_t(self):
        self.assertEqual(sizeof(c_void_p), sizeof(c_size_t))

    def test_ssize_t(self):
        self.assertEqual(sizeof(c_void_p), sizeof(c_ssize_t))


if __name__ == '__main__':
    unittest.main()
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\ctypes\test\test_sizes.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:02:47 Støední Evropa (bìžný èas)

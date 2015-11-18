# 2015.11.18 12:02:41 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/ctypes/test/test_delattr.py
import unittest
from ctypes import *

class X(Structure):
    _fields_ = [('foo', c_int)]


class TestCase(unittest.TestCase):

    def test_simple(self):
        self.assertRaises(TypeError, delattr, c_int(42), 'value')

    def test_chararray(self):
        self.assertRaises(TypeError, delattr, (c_char * 5)(), 'value')

    def test_struct(self):
        self.assertRaises(TypeError, delattr, X(), 'foo')


if __name__ == '__main__':
    unittest.main()
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\ctypes\test\test_delattr.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:02:41 Støední Evropa (bìžný èas)

# 2015.11.18 12:02:38 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/ctypes/test/test_anon.py
import unittest
from ctypes import *

class AnonTest(unittest.TestCase):

    def test_anon(self):

        class ANON(Union):
            _fields_ = [('a', c_int), ('b', c_int)]

        class Y(Structure):
            _fields_ = [('x', c_int), ('_', ANON), ('y', c_int)]
            _anonymous_ = ['_']

        self.assertEqual(Y.a.offset, sizeof(c_int))
        self.assertEqual(Y.b.offset, sizeof(c_int))
        self.assertEqual(ANON.a.offset, 0)
        self.assertEqual(ANON.b.offset, 0)

    def test_anon_nonseq(self):
        self.assertRaises(TypeError, lambda : type(Structure)('Name', (Structure,), {'_fields_': [],
         '_anonymous_': 42}))

    def test_anon_nonmember(self):
        self.assertRaises(AttributeError, lambda : type(Structure)('Name', (Structure,), {'_fields_': [],
         '_anonymous_': ['x']}))

    def test_nested(self):

        class ANON_S(Structure):
            _fields_ = [('a', c_int)]

        class ANON_U(Union):
            _fields_ = [('_', ANON_S), ('b', c_int)]
            _anonymous_ = ['_']

        class Y(Structure):
            _fields_ = [('x', c_int), ('_', ANON_U), ('y', c_int)]
            _anonymous_ = ['_']

        self.assertEqual(Y.x.offset, 0)
        self.assertEqual(Y.a.offset, sizeof(c_int))
        self.assertEqual(Y.b.offset, sizeof(c_int))
        self.assertEqual(Y._.offset, sizeof(c_int))
        self.assertEqual(Y.y.offset, sizeof(c_int) * 2)


if __name__ == '__main__':
    unittest.main()
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\ctypes\test\test_anon.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:02:38 Støední Evropa (bìžný èas)

# 2015.11.18 12:02:41 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/ctypes/test/test_checkretval.py
import unittest
from ctypes import *

class CHECKED(c_int):

    def _check_retval_(value):
        return str(value.value)

    _check_retval_ = staticmethod(_check_retval_)


class Test(unittest.TestCase):

    def test_checkretval(self):
        import _ctypes_test
        dll = CDLL(_ctypes_test.__file__)
        self.assertEqual(42, dll._testfunc_p_p(42))
        dll._testfunc_p_p.restype = CHECKED
        self.assertEqual('42', dll._testfunc_p_p(42))
        dll._testfunc_p_p.restype = None
        self.assertEqual(None, dll._testfunc_p_p(42))
        del dll._testfunc_p_p.restype
        self.assertEqual(42, dll._testfunc_p_p(42))
        return

    try:
        oledll
    except NameError:
        pass
    else:

        def test_oledll(self):
            self.assertRaises(WindowsError, oledll.oleaut32.CreateTypeLib2, 0, None, None)
            return


if __name__ == '__main__':
    unittest.main()
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\ctypes\test\test_checkretval.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:02:41 Støední Evropa (bìžný èas)

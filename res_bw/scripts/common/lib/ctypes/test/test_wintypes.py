# 2015.11.18 12:02:50 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/ctypes/test/test_wintypes.py
import sys
import unittest
if not sys.platform.startswith('win'):
    raise unittest.SkipTest('Windows-only test')
from ctypes import *
from ctypes import wintypes

class WinTypesTest(unittest.TestCase):

    def test_variant_bool(self):
        for true_value in (1, 32767, 32768, 65535, 65537):
            true = POINTER(c_int16)(c_int16(true_value))
            value = cast(true, POINTER(wintypes.VARIANT_BOOL))
            self.assertEqual(repr(value.contents), 'VARIANT_BOOL(True)')
            vb = wintypes.VARIANT_BOOL()
            self.assertIs(vb.value, False)
            vb.value = True
            self.assertIs(vb.value, True)
            vb.value = true_value
            self.assertIs(vb.value, True)

        for false_value in (0,
         65536,
         262144,
         8589934592L):
            false = POINTER(c_int16)(c_int16(false_value))
            value = cast(false, POINTER(wintypes.VARIANT_BOOL))
            self.assertEqual(repr(value.contents), 'VARIANT_BOOL(False)')

        for set_value in (65536, 262144, 8589934592L):
            vb = wintypes.VARIANT_BOOL()
            vb.value = set_value
            self.assertIs(vb.value, True)

        vb = wintypes.VARIANT_BOOL()
        vb.value = [2, 3]
        self.assertIs(vb.value, True)
        vb.value = []
        self.assertIs(vb.value, False)


if __name__ == '__main__':
    unittest.main()
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\ctypes\test\test_wintypes.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:02:50 Støední Evropa (bìžný èas)

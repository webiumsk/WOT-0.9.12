# 2015.11.18 12:04:22 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/json/tests/test_check_circular.py
from json.tests import PyTest, CTest

def default_iterable(obj):
    return list(obj)


class TestCheckCircular(object):

    def test_circular_dict(self):
        dct = {}
        dct['a'] = dct
        self.assertRaises(ValueError, self.dumps, dct)

    def test_circular_list(self):
        lst = []
        lst.append(lst)
        self.assertRaises(ValueError, self.dumps, lst)

    def test_circular_composite(self):
        dct2 = {}
        dct2['a'] = []
        dct2['a'].append(dct2)
        self.assertRaises(ValueError, self.dumps, dct2)

    def test_circular_default(self):
        self.dumps([set()], default=default_iterable)
        self.assertRaises(TypeError, self.dumps, [set()])

    def test_circular_off_default(self):
        self.dumps([set()], default=default_iterable, check_circular=False)
        self.assertRaises(TypeError, self.dumps, [set()], check_circular=False)


class TestPyCheckCircular(TestCheckCircular, PyTest):
    pass


class TestCCheckCircular(TestCheckCircular, CTest):
    pass
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\json\tests\test_check_circular.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:04:23 Støední Evropa (bìžný èas)

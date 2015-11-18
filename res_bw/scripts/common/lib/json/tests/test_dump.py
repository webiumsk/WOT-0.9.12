# 2015.11.18 12:04:23 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/json/tests/test_dump.py
from cStringIO import StringIO
from json.tests import PyTest, CTest

class TestDump(object):

    def test_dump(self):
        sio = StringIO()
        self.json.dump({}, sio)
        self.assertEqual(sio.getvalue(), '{}')

    def test_dumps(self):
        self.assertEqual(self.dumps({}), '{}')

    def test_encode_truefalse(self):
        self.assertEqual(self.dumps({True: False,
         False: True}, sort_keys=True), '{"false": true, "true": false}')
        self.assertEqual(self.dumps({2: 3.0,
         4.0: 5L,
         False: 1,
         6L: True}, sort_keys=True), '{"false": 1, "2": 3.0, "4.0": 5, "6": true}')

    def test_encode_mutated(self):
        a = [object()] * 10

        def crasher(obj):
            del a[-1]

        self.assertEqual(self.dumps(a, default=crasher), '[null, null, null, null, null]')


class TestPyDump(TestDump, PyTest):
    pass


class TestCDump(TestDump, CTest):
    pass
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\json\tests\test_dump.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:04:23 St�edn� Evropa (b�n� �as)

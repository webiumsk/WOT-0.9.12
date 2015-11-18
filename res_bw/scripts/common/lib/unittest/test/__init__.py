# 2015.11.18 12:06:37 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/unittest/test/__init__.py
import os
import sys
import unittest
here = os.path.dirname(__file__)
loader = unittest.defaultTestLoader

def suite():
    suite = unittest.TestSuite()
    for fn in os.listdir(here):
        if fn.startswith('test') and fn.endswith('.py'):
            modname = 'unittest.test.' + fn[:-3]
            __import__(modname)
            module = sys.modules[modname]
            suite.addTest(loader.loadTestsFromModule(module))

    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\unittest\test\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:06:37 Støední Evropa (bìžný èas)

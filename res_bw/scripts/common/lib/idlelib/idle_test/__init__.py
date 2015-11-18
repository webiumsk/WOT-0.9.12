# 2015.11.18 12:04:20 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/idlelib/idle_test/__init__.py
from os.path import dirname

def load_tests(loader, standard_tests, pattern):
    this_dir = dirname(__file__)
    top_dir = dirname(dirname(this_dir))
    package_tests = loader.discover(start_dir=this_dir, pattern='test*.py', top_level_dir=top_dir)
    standard_tests.addTests(package_tests)
    return standard_tests
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\idlelib\idle_test\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:04:20 Støední Evropa (bìžný èas)

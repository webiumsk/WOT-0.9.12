# 2015.11.18 12:02:38 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/ctypes/test/runtests.py
"""Usage: runtests.py [-q] [-r] [-v] [-u resources] [mask]

Run all tests found in this directory, and print a summary of the results.
Command line flags:
  -q     quiet mode: don't print anything while the tests are running
  -r     run tests repeatedly, look for refcount leaks
  -u<resources>
         Add resources to the lits of allowed resources. '*' allows all
         resources.
  -v     verbose mode: print the test currently executed
  -x<test1[,test2...]>
         Exclude specified tests.
  mask   mask to select filenames containing testcases, wildcards allowed
"""
import sys
import ctypes.test
if __name__ == '__main__':
    sys.exit(ctypes.test.main(ctypes.test))
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\ctypes\test\runtests.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:02:38 Støední Evropa (bìžný èas)

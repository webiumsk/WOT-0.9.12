# 2015.11.18 12:03:17 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/distutils/tests/test_install_headers.py
"""Tests for distutils.command.install_headers."""
import sys
import os
import unittest
import getpass
from distutils.command.install_headers import install_headers
from distutils.tests import support
from test.test_support import run_unittest

class InstallHeadersTestCase(support.TempdirManager, support.LoggingSilencer, support.EnvironGuard, unittest.TestCase):

    def test_simple_run(self):
        header_list = self.mkdtemp()
        header1 = os.path.join(header_list, 'header1')
        header2 = os.path.join(header_list, 'header2')
        self.write_file(header1)
        self.write_file(header2)
        headers = [header1, header2]
        pkg_dir, dist = self.create_dist(headers=headers)
        cmd = install_headers(dist)
        self.assertEqual(cmd.get_inputs(), headers)
        cmd.install_dir = os.path.join(pkg_dir, 'inst')
        cmd.ensure_finalized()
        cmd.run()
        self.assertEqual(len(cmd.get_outputs()), 2)


def test_suite():
    return unittest.makeSuite(InstallHeadersTestCase)


if __name__ == '__main__':
    run_unittest(test_suite())
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\distutils\tests\test_install_headers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:03:17 St�edn� Evropa (b�n� �as)

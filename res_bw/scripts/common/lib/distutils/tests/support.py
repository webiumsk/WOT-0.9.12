# 2015.11.18 12:03:11 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/distutils/tests/support.py
"""Support code for distutils test cases."""
import os
import sys
import shutil
import tempfile
import unittest
import sysconfig
from copy import deepcopy
import warnings
from distutils import log
from distutils.log import DEBUG, INFO, WARN, ERROR, FATAL
from distutils.core import Distribution

def capture_warnings(func):

    def _capture_warnings(*args, **kw):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            return func(*args, **kw)

    return _capture_warnings


class LoggingSilencer(object):

    def setUp(self):
        super(LoggingSilencer, self).setUp()
        self.threshold = log.set_threshold(log.FATAL)
        self._old_log = log.Log._log
        log.Log._log = self._log
        self.logs = []

    def tearDown(self):
        log.set_threshold(self.threshold)
        log.Log._log = self._old_log
        super(LoggingSilencer, self).tearDown()

    def _log(self, level, msg, args):
        if level not in (DEBUG,
         INFO,
         WARN,
         ERROR,
         FATAL):
            raise ValueError('%s wrong log level' % str(level))
        self.logs.append((level, msg, args))

    def get_logs(self, *levels):

        def _format(msg, args):
            if len(args) == 0:
                return msg
            return msg % args

        return [ _format(msg, args) for level, msg, args in self.logs if level in levels ]

    def clear_logs(self):
        self.logs = []


class TempdirManager(object):
    """Mix-in class that handles temporary directories for test cases.
    
    This is intended to be used with unittest.TestCase.
    """

    def setUp(self):
        super(TempdirManager, self).setUp()
        self.old_cwd = os.getcwd()
        self.tempdirs = []

    def tearDown(self):
        os.chdir(self.old_cwd)
        super(TempdirManager, self).tearDown()
        while self.tempdirs:
            d = self.tempdirs.pop()
            shutil.rmtree(d, os.name in ('nt', 'cygwin'))

    def mkdtemp(self):
        """Create a temporary directory that will be cleaned up.
        
        Returns the path of the directory.
        """
        d = tempfile.mkdtemp()
        self.tempdirs.append(d)
        return d

    def write_file(self, path, content = 'xxx'):
        """Writes a file in the given path.
        
        
        path can be a string or a sequence.
        """
        if isinstance(path, (list, tuple)):
            path = os.path.join(*path)
        f = open(path, 'w')
        try:
            f.write(content)
        finally:
            f.close()

    def create_dist(self, pkg_name = 'foo', **kw):
        """Will generate a test environment.
        
        This function creates:
         - a Distribution instance using keywords
         - a temporary directory with a package structure
        
        It returns the package directory and the distribution
        instance.
        """
        tmp_dir = self.mkdtemp()
        pkg_dir = os.path.join(tmp_dir, pkg_name)
        os.mkdir(pkg_dir)
        dist = Distribution(attrs=kw)
        return (pkg_dir, dist)


class DummyCommand:
    """Class to store options for retrieval via set_undefined_options()."""

    def __init__(self, **kwargs):
        for kw, val in kwargs.items():
            setattr(self, kw, val)

    def ensure_finalized(self):
        pass


class EnvironGuard(object):

    def setUp(self):
        super(EnvironGuard, self).setUp()
        self.old_environ = deepcopy(os.environ)

    def tearDown(self):
        for key, value in self.old_environ.items():
            if os.environ.get(key) != value:
                os.environ[key] = value

        for key in os.environ.keys():
            if key not in self.old_environ:
                del os.environ[key]

        super(EnvironGuard, self).tearDown()


def copy_xxmodule_c(directory):
    """Helper for tests that need the xxmodule.c source file.
    
    Example use:
    
        def test_compile(self):
            copy_xxmodule_c(self.tmpdir)
            self.assertIn('xxmodule.c', os.listdir(self.tmpdir))
    
    If the source file can be found, it will be copied to *directory*.  If not,
    the test will be skipped.  Errors during copy are not caught.
    """
    filename = _get_xxmodule_path()
    if filename is None:
        raise unittest.SkipTest('cannot find xxmodule.c (test must run in the python build dir)')
    shutil.copy(filename, directory)
    return


def _get_xxmodule_path():
    srcdir = sysconfig.get_config_var('srcdir')
    candidates = [os.path.join(os.path.dirname(__file__), 'xxmodule.c'), os.path.join(srcdir, 'Modules', 'xxmodule.c'), os.path.join(srcdir, '..', '..', '..', 'Modules', 'xxmodule.c')]
    for path in candidates:
        if os.path.exists(path):
            return path


def fixup_build_ext(cmd):
    """Function needed to make build_ext tests pass.
    
    When Python was build with --enable-shared on Unix, -L. is not good
    enough to find the libpython<blah>.so.  This is because regrtest runs
    it under a tempdir, not in the top level where the .so lives.  By the
    time we've gotten here, Python's already been chdir'd to the tempdir.
    
    When Python was built with in debug mode on Windows, build_ext commands
    need their debug attribute set, and it is not done automatically for
    some reason.
    
    This function handles both of these things.  Example use:
    
        cmd = build_ext(dist)
        support.fixup_build_ext(cmd)
        cmd.ensure_finalized()
    
    Unlike most other Unix platforms, Mac OS X embeds absolute paths
    to shared libraries into executables, so the fixup is not needed there.
    """
    if os.name == 'nt':
        cmd.debug = sys.executable.endswith('_d.exe')
    elif sysconfig.get_config_var('Py_ENABLE_SHARED'):
        runshared = sysconfig.get_config_var('RUNSHARED')
        if runshared is None:
            cmd.library_dirs = ['.']
        elif sys.platform == 'darwin':
            cmd.library_dirs = []
        else:
            name, equals, value = runshared.partition('=')
            cmd.library_dirs = [ d for d in value.split(os.pathsep) if d ]
    return
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\distutils\tests\support.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:03:11 St�edn� Evropa (b�n� �as)

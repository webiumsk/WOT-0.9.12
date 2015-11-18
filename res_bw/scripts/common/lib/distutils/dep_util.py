# 2015.11.18 12:02:54 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/distutils/dep_util.py
"""distutils.dep_util

Utility functions for simple, timestamp-based dependency of files
and groups of files; also, function based entirely on such
timestamp dependency analysis."""
__revision__ = '$Id$'
import os
from stat import ST_MTIME
from distutils.errors import DistutilsFileError

def newer(source, target):
    """Tells if the target is newer than the source.
    
    Return true if 'source' exists and is more recently modified than
    'target', or if 'source' exists and 'target' doesn't.
    
    Return false if both exist and 'target' is the same age or younger
    than 'source'. Raise DistutilsFileError if 'source' does not exist.
    
    Note that this test is not very accurate: files created in the same second
    will have the same "age".
    """
    if not os.path.exists(source):
        raise DistutilsFileError("file '%s' does not exist" % os.path.abspath(source))
    if not os.path.exists(target):
        return True
    return os.stat(source)[ST_MTIME] > os.stat(target)[ST_MTIME]


def newer_pairwise(sources, targets):
    """Walk two filename lists in parallel, testing if each source is newer
    than its corresponding target.  Return a pair of lists (sources,
    targets) where source is newer than target, according to the semantics
    of 'newer()'.
    """
    if len(sources) != len(targets):
        raise ValueError, "'sources' and 'targets' must be same length"
    n_sources = []
    n_targets = []
    for source, target in zip(sources, targets):
        if newer(source, target):
            n_sources.append(source)
            n_targets.append(target)

    return (n_sources, n_targets)


def newer_group(sources, target, missing = 'error'):
    """Return true if 'target' is out-of-date with respect to any file
    listed in 'sources'.
    
    In other words, if 'target' exists and is newer
    than every file in 'sources', return false; otherwise return true.
    'missing' controls what we do when a source file is missing; the
    default ("error") is to blow up with an OSError from inside 'stat()';
    if it is "ignore", we silently drop any missing source files; if it is
    "newer", any missing source files make us assume that 'target' is
    out-of-date (this is handy in "dry-run" mode: it'll make you pretend to
    carry out commands that wouldn't work because inputs are missing, but
    that doesn't matter because you're not actually going to run the
    commands).
    """
    if not os.path.exists(target):
        return True
    target_mtime = os.stat(target)[ST_MTIME]
    for source in sources:
        if not os.path.exists(source):
            if missing == 'error':
                pass
            elif missing == 'ignore':
                continue
            elif missing == 'newer':
                return True
        if os.stat(source)[ST_MTIME] > target_mtime:
            return True

    return False
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\distutils\dep_util.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:02:54 St�edn� Evropa (b�n� �as)

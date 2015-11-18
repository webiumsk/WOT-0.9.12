# 2015.11.18 12:02:14 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/bsddb/dbutils.py
from time import sleep as _sleep
import sys
absolute_import = sys.version_info[0] >= 3
if absolute_import:
    exec 'from . import db'
else:
    import db
_deadlock_MinSleepTime = 1.0 / 128
_deadlock_MaxSleepTime = 3.14159
_deadlock_VerboseFile = None

def DeadlockWrap(function, *_args, **_kwargs):
    """DeadlockWrap(function, *_args, **_kwargs) - automatically retries
    function in case of a database deadlock.
    
    This is a function intended to be used to wrap database calls such
    that they perform retrys with exponentially backing off sleeps in
    between when a DBLockDeadlockError exception is raised.
    
    A 'max_retries' parameter may optionally be passed to prevent it
    from retrying forever (in which case the exception will be reraised).
    
        d = DB(...)
        d.open(...)
        DeadlockWrap(d.put, "foo", data="bar")  # set key "foo" to "bar"
    """
    sleeptime = _deadlock_MinSleepTime
    max_retries = _kwargs.get('max_retries', -1)
    if 'max_retries' in _kwargs:
        del _kwargs['max_retries']
    while True:
        try:
            return function(*_args, **_kwargs)
        except db.DBLockDeadlockError:
            if _deadlock_VerboseFile:
                _deadlock_VerboseFile.write('dbutils.DeadlockWrap: sleeping %1.3f\n' % sleeptime)
            _sleep(sleeptime)
            sleeptime *= 2
            if sleeptime > _deadlock_MaxSleepTime:
                sleeptime = _deadlock_MaxSleepTime
            max_retries -= 1
            if max_retries == -1:
                raise
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\bsddb\dbutils.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:02:14 St�edn� Evropa (b�n� �as)

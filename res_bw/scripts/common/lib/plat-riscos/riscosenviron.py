# 2015.11.18 12:06:22 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/plat-riscos/riscosenviron.py
"""A more or less complete dictionary like interface for the RISC OS environment."""
import riscos

class _Environ:

    def __init__(self, initial = None):
        pass

    def __repr__(self):
        return repr(riscos.getenvdict())

    def __cmp__(self, dict):
        return cmp(riscos.getenvdict(), dict)

    def __len__(self):
        return len(riscos.getenvdict())

    def __getitem__(self, key):
        ret = riscos.getenv(key)
        if ret != None:
            return ret
        else:
            raise KeyError
            return

    def __setitem__(self, key, item):
        riscos.putenv(key, item)

    def __delitem__(self, key):
        riscos.delenv(key)

    def clear(self):
        pass

    def copy(self):
        return riscos.getenvdict()

    def keys(self):
        return riscos.getenvdict().keys()

    def items(self):
        return riscos.getenvdict().items()

    def values(self):
        return riscos.getenvdict().values()

    def has_key(self, key):
        value = riscos.getenv(key)
        return value != None

    def __contains__(self, key):
        return riscos.getenv(key) is not None

    def update(self, dict):
        for k, v in dict.items():
            riscos.putenv(k, v)

    def get(self, key, failobj = None):
        value = riscos.getenv(key)
        if value != None:
            return value
        else:
            return failobj
            return
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\plat-riscos\riscosenviron.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:06:22 St�edn� Evropa (b�n� �as)

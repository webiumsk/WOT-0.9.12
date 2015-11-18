# 2015.11.18 11:59:02 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/LRUCache.py
import collections

class LRUCache(object):

    def __init__(self, limit):
        self.__cache = collections.OrderedDict()
        self.__limit = limit

    def get(self, key):
        try:
            value = self.__cache.pop(key)
            self.__cache[key] = value
            return value
        except KeyError:
            return None

        return None

    def peek(self, key):
        return self.__cache.get(key, None)

    def set(self, key, value):
        try:
            self.__cache.pop(key)
        except KeyError:
            if len(self.__cache) >= self.__limit:
                self.__cache.popitem(last=False)

        self.__cache[key] = value

    def pop(self, key):
        return self.__cache.pop(key, None)

    def clear(self):
        self.__cache.clear()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\lrucache.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:02 St�edn� Evropa (b�n� �as)

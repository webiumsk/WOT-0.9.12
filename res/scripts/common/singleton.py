# 2015.11.18 11:59:09 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Singleton.py


class Singleton(object):

    def __new__(cls, *args, **kwargs):
        singleton_instance = cls.__dict__.get('__instance__')
        if singleton_instance is not None:
            return singleton_instance
        else:
            cls.__instance__ = singleton_instance = object.__new__(cls)
            singleton_instance._singleton_init(*args, **kwargs)
            return singleton_instance

    def _singleton_init(self, *args, **kwargs):
        pass


if __name__ == '__main__':

    class MySingleton(Singleton):

        def _singleton_init(self, instanceName):
            self.instanceName = instanceName


    ins1 = MySingleton('instance1')
    print id(ins1), ins1.instanceName
    ins2 = MySingleton('instance2')
    print id(ins2), ins2.instanceName
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\singleton.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:09 St�edn� Evropa (b�n� �as)

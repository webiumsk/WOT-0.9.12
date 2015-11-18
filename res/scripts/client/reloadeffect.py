# 2015.11.18 11:51:07 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/ReloadEffect.py
import FMOD
from helpers.CallbackDelayer import CallbackDelayer
import SoundGroups

def _createReloadEffectDesc(type, dataSection):
    if len(dataSection.values()) == 0:
        return None
    elif type == 'SimpleReload':
        return _SimpleReloadDesc(dataSection)
    else:
        return None


class _ReloadDesc(object):

    def __init__(self):
        pass

    def create(self):
        return None


class _SimpleReloadDesc(_ReloadDesc):

    def __init__(self, dataSection):
        super(_SimpleReloadDesc, self).__init__()
        self.duration = dataSection.readFloat('duration', 0.0) / 1000.0
        self.soundEvent = dataSection.readString('sound', '')

    def create(self):
        return SimpleReload(self)


def effectFromSection(section):
    type = section.readString('type', '')
    return _createReloadEffectDesc(type, section)


class SimpleReload(CallbackDelayer):

    def __init__(self, effectDesc):
        CallbackDelayer.__init__(self)
        self.__desc = effectDesc

    def __del__(self):
        CallbackDelayer.destroy(self)

    def start(self, reloadTime):
        time = reloadTime - self.__desc.duration
        if time > 0.0:
            self.delayCallback(time, self.__startEvent)

    def __startEvent(self):
        pass
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\reloadeffect.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:51:07 Støední Evropa (bìžný èas)

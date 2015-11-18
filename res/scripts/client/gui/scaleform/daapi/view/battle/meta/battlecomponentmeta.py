# 2015.11.18 11:53:14 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/meta/BattleComponentMeta.py
from debug_utils import LOG_ERROR

class BattleComponentMeta(object):

    def __init__(self):
        super(BattleComponentMeta, self).__init__()
        self._flashObject = None
        return

    def _populate(self, flashObject):
        result = True
        if flashObject:
            self._flashObject = flashObject
            self._flashObject.resync()
            self._flashObject.script = self
        else:
            result = False
            LOG_ERROR('Display object is not found in the swf file.')
        return result

    def _dispose(self):
        if self._flashObject is not None:
            self._flashObject.script = None
            self._flashObject = None
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\battle\meta\battlecomponentmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:53:14 St�edn� Evropa (b�n� �as)

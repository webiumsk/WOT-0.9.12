# 2015.11.18 11:54:51 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleQueueMeta.py
from gui.Scaleform.framework.entities.View import View

class BattleQueueMeta(View):

    def startClick(self):
        self._printOverrideError('startClick')

    def exitClick(self):
        self._printOverrideError('exitClick')

    def onEscape(self):
        self._printOverrideError('onEscape')

    def as_setTimerS(self, textLabel, timeLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimer(textLabel, timeLabel)

    def as_setTypeInfoS(self, iconLabel, title, description):
        if self._isDAAPIInited():
            return self.flashObject.as_setTypeInfo(iconLabel, title, description)

    def as_setPlayersS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayers(text)

    def as_setListByTypeS(self, listData):
        if self._isDAAPIInited():
            return self.flashObject.as_setListByType(listData)

    def as_showStartS(self, vis):
        if self._isDAAPIInited():
            return self.flashObject.as_showStart(vis)

    def as_showExitS(self, vis):
        if self._isDAAPIInited():
            return self.flashObject.as_showExit(vis)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\battlequeuemeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:54:51 St�edn� Evropa (b�n� �as)

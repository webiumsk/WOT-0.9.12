# 2015.11.18 11:55:23 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/AbstractTweenMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class AbstractTweenMeta(BaseDAAPIModule):

    def initialiaze(self, props):
        self._printOverrideError('initialiaze')

    def creatTweenPY(self, tween):
        self._printOverrideError('creatTweenPY')

    def getPaused(self):
        self._printOverrideError('getPaused')

    def setPaused(self, paused):
        self._printOverrideError('setPaused')

    def getLoop(self):
        self._printOverrideError('getLoop')

    def setLoop(self, loop):
        self._printOverrideError('setLoop')

    def getDuration(self):
        self._printOverrideError('getDuration')

    def setDuration(self, duration):
        self._printOverrideError('setDuration')

    def getPosition(self):
        self._printOverrideError('getPosition')

    def setPosition(self, position):
        self._printOverrideError('setPosition')

    def getDelay(self):
        self._printOverrideError('getDelay')

    def setDelay(self, delay):
        self._printOverrideError('setDelay')

    def resetAnim(self):
        self._printOverrideError('resetAnim')

    def getTweenIdx(self):
        self._printOverrideError('getTweenIdx')

    def getIsComplete(self):
        self._printOverrideError('getIsComplete')

    def postponedCheckState(self):
        self._printOverrideError('postponedCheckState')

    def getTargetDisplayObjectS(self):
        if self._isDAAPIInited():
            return self.flashObject.getTargetDisplayObject()

    def onAnimCompleteS(self):
        if self._isDAAPIInited():
            return self.flashObject.onAnimComplete()

    def onAnimStartS(self):
        if self._isDAAPIInited():
            return self.flashObject.onAnimStart()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\framework\entities\abstract\abstracttweenmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:55:23 Støední Evropa (bìžný èas)

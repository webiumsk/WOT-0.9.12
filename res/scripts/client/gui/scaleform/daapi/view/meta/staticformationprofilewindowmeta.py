# 2015.11.18 11:55:15 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StaticFormationProfileWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class StaticFormationProfileWindowMeta(AbstractWindowView):

    def actionBtnClickHandler(self, action):
        self._printOverrideError('actionBtnClickHandler')

    def onClickHyperLink(self, value):
        self._printOverrideError('onClickHyperLink')

    def as_setWindowSizeS(self, width, height):
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowSize(width, height)

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setFormationEmblemS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setFormationEmblem(value)

    def as_updateFormationInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateFormationInfo(data)

    def as_updateActionButtonS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateActionButton(data)

    def as_showViewS(self, idx):
        if self._isDAAPIInited():
            return self.flashObject.as_showView(idx)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\staticformationprofilewindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:55:15 Støední Evropa (bìžný èas)

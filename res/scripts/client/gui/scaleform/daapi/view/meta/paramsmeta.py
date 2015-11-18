# 2015.11.18 11:55:08 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ParamsMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ParamsMeta(BaseDAAPIComponent):

    def as_setValuesS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setValues(data)

    def as_highlightParamsS(self, type):
        if self._isDAAPIInited():
            return self.flashObject.as_highlightParams(type)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\paramsmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:55:08 Støední Evropa (bìžný èas)

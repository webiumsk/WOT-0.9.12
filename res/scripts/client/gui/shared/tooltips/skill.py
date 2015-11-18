# 2015.11.18 11:56:52 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/shared/tooltips/skill.py
from gui.shared.tooltips import TOOLTIP_TYPE, ToolTipData, ToolTipAttrField

class SkillTooltipData(ToolTipData):

    def __init__(self, context):
        super(SkillTooltipData, self).__init__(context, TOOLTIP_TYPE.SKILL)
        self.fields = (ToolTipAttrField(self, 'name', 'userName'),
         ToolTipAttrField(self, 'shortDescr', 'shortDescription'),
         ToolTipAttrField(self, 'descr', 'description'),
         ToolTipAttrField(self, 'level'),
         ToolTipAttrField(self, 'type'),
         ToolTipAttrField(self, 'count'))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\tooltips\skill.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:56:52 Støední Evropa (bìžný èas)

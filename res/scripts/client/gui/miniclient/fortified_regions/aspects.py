# 2015.11.18 11:52:29 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/miniclient/fortified_regions/aspects.py
from gui.shared.formatters import text_styles
from helpers import aop
from helpers.i18n import makeString as _ms
from gui.Scaleform.genConsts.FORTIFICATION_ALIASES import FORTIFICATION_ALIASES

class OnViewPopulate(aop.Aspect):

    def atReturn(self, cd):
        cd.self.as_showMiniClientInfoS(text_styles.alert(_ms('#miniclient:fort_welcome_view/description')), _ms('#miniclient:personal_quests_welcome_view/continue_download'))


class OnFortifiedRegionsOpen(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        cd.self.as_loadViewS(FORTIFICATION_ALIASES.WELCOME_VIEW_LINKAGE, '')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\miniclient\fortified_regions\aspects.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:30 Støední Evropa (bìžný èas)

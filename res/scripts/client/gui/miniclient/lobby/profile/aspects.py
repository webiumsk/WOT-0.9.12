# 2015.11.18 11:52:32 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/miniclient/lobby/profile/aspects.py
from gui.Scaleform.locale.MINICLIENT import MINICLIENT
from gui.shared.utils.functions import makeTooltip
from helpers import aop
from helpers.i18n import makeString

class MakeClanBtnUnavailable(aop.Aspect):

    def atReturn(self, cd):
        original_return_value = cd.returned
        original_return_value['btnEnabled'] = False
        original_return_value['btnTooltip'] = makeTooltip(None, None, None, makeString(MINICLIENT.PROFILE_WARNING))
        return original_return_value
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\miniclient\lobby\profile\aspects.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:32 Støední Evropa (bìžný èas)

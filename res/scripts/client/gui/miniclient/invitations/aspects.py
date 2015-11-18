# 2015.11.18 11:52:30 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/miniclient/invitations/aspects.py
from gui import makeHtmlString
from helpers import aop
from helpers.i18n import makeString as _ms
from constants import PREBATTLE_TYPE_NAMES

class DisableAcceptButton(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        return False


class InvitationNote(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        battle_type = PREBATTLE_TYPE_NAMES[cd.args[0].type]
        return makeHtmlString('html_templates:lobby/prebattle', 'inviteNote', {'note': _ms('#miniclient:invitation/note/{0}'.format(battle_type))})
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\miniclient\invitations\aspects.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:30 Støední Evropa (bìžný èas)

# 2015.11.18 11:57:06 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/wgnc/client.py
from gui.wgnc.settings import WGNC_GUI_TYPE

class ClosePollWindowFromPopUp(object):
    __slots__ = ('_target',)

    def __init__(self, target):
        super(ClosePollWindowFromPopUp, self).__init__()
        self._target = target

    def process(self, actor, notID, actions, items):
        if actor.getType() != WGNC_GUI_TYPE.POP_UP:
            return
        submit = actor.getSubmitButton()
        if not submit:
            return
        if submit.action != actions:
            return
        item = items.getItemByName(self._target)
        if item:
            item.close(notID)


class ClientLogic(object):
    __slots__ = ('_seq',)

    def __init__(self, seq):
        super(ClientLogic, self).__init__()
        self._seq = seq

    def process(self, actor, notID, actions, items):
        for logic in self._seq:
            logic.process(actor, notID, actions, items)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\wgnc\client.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:57:06 Støední Evropa (bìžný èas)

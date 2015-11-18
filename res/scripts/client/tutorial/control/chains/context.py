# 2015.11.18 11:58:21 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/tutorial/control/chains/context.py
from tutorial.control import context, game_vars
from tutorial.control.lobby.context import LobbyBonusesRequester

class ChainsStartReqs(context.StartReqs):

    def isEnabled(self):
        return True

    def prepare(self, ctx):
        ctx.bonusCompleted = game_vars.getTutorialsCompleted()

    def process(self, descriptor, ctx):
        return True


class ChainsBonusesRequester(LobbyBonusesRequester):
    pass
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\tutorial\control\chains\context.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:58:21 Støední Evropa (bìžný èas)

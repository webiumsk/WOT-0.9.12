# 2015.11.18 11:58:25 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/tutorial/control/quests/battle/__init__.py
from tutorial.control import ControlsFactory
from tutorial.control import context as core_ctx
from tutorial.control import functional as core_func
from tutorial.control.functional import FunctionalChapterInfo
from tutorial.control.quests import functional as quests_func
from tutorial.control.quests.battle.context import FakeBonusesRequester
from tutorial.data.effects import EFFECT_TYPE

class BattleQuestsControlsFactory(ControlsFactory):

    def __init__(self):
        effects = {EFFECT_TYPE.RUN_TRIGGER: core_func.FunctionalRunTriggerEffect,
         EFFECT_TYPE.REFUSE_TRAINING: core_func.FunctionalRefuseTrainingEffect,
         EFFECT_TYPE.SAVE_TUTORIAL_SETTING: quests_func.SaveTutorialSettingEffect}
        ControlsFactory.__init__(self, effects, {})

    def createBonuses(self, completed):
        return FakeBonusesRequester(completed)

    def createSoundPlayer(self):
        return core_ctx.NoSound()

    def createFuncScene(self, sceneModel):
        return core_func.FunctionalScene(sceneModel)

    def createFuncInfo(self):
        return FunctionalChapterInfo()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\tutorial\control\quests\battle\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:58:25 Støední Evropa (bìžný èas)

# 2015.11.18 11:56:33 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/GuerrillaAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SimpleProgressAchievement

class GuerrillaAchievement(SimpleProgressAchievement):

    def __init__(self, dossier, value = None):
        super(GuerrillaAchievement, self).__init__('guerrillaMedal', _AB.TEAM_7X7, dossier, value)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, 'guerrilla')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\guerrillaachievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:56:33 St�edn� Evropa (b�n� �as)

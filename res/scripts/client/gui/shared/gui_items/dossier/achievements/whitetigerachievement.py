# 2015.11.18 11:56:38 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/WhiteTigerAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import RegularAchievement
import validators

class WhiteTigerAchievement(RegularAchievement):
    WHITE_TIGER_COMP_DESCR = 56337

    def __init__(self, dossier, value = None):
        super(WhiteTigerAchievement, self).__init__('whiteTiger', _AB.CLIENT, dossier, value)

    @classmethod
    def checkIsInDossier(cls, block, name, dossier):
        if dossier is not None:
            return bool(cls.__getWhiteTigerKillings(dossier))
        else:
            return False

    @classmethod
    def checkIsValid(cls, block, name, dossier):
        return validators.alreadyAchieved(cls, name, block, dossier) and not validators.accountIsRoaming(dossier)

    def _readValue(self, dossier):
        return self.__getWhiteTigerKillings(dossier)

    @classmethod
    def __getWhiteTigerKillings(cls, dossier):
        return dossier.getBlock('vehTypeFrags').get(cls.WHITE_TIGER_COMP_DESCR, 0)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\whitetigerachievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:56:38 Støední Evropa (bìžný èas)

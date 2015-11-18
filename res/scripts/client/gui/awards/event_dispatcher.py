# 2015.11.18 11:51:49 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/awards/event_dispatcher.py
import gui.awards.special_achievement_awards as specialAwards
from gui.shared.event_dispatcher import showAwardWindow, showPremiumCongratulationWindow

def showResearchAward(vehiclesCount, messageNumber):
    showAwardWindow(specialAwards.ResearchAward(vehiclesCount, messageNumber))


def showVictoryAward(victoriesCount, messageNumber):
    showAwardWindow(specialAwards.VictoryAward(victoriesCount, messageNumber))


def showBattleAward(battlesCount, messageNumber):
    showAwardWindow(specialAwards.BattleAward(battlesCount, messageNumber))


def showPveBattleAward(battlesCount, messageNumber):
    showAwardWindow(specialAwards.PvEBattleAward(battlesCount, messageNumber))


def showPremiumDiscountAward(researchLvl, premiumPacket, discount):
    showPremiumCongratulationWindow(specialAwards.PremiumDiscountAward(researchLvl, premiumPacket, discount))


def showBoosterAward(booster):
    showAwardWindow(specialAwards.BoosterAward(booster))


def showFalloutAward(lvls, isRequiredVehicle = False):
    showAwardWindow(specialAwards.FalloutAwardWindow(lvls, isRequiredVehicle))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\awards\event_dispatcher.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:51:49 Støední Evropa (bìžný èas)

# 2015.11.18 11:52:31 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/miniclient/lobby/header/__init__.py
import account_popover as _account_popover
import create_squad as _create_squad
import fight_button_ as _fight_button
from battle_type_selector import configure_pointcuts as _configure_selector_pointcuts

def configure_pointcuts(config):
    _configure_selector_pointcuts()
    _create_squad.OnCreateSquadClickPointcut()
    _fight_button.DisableFightButtonPointcut(config)
    _account_popover.ClanBtnsUnavailable()
    _account_popover.MyClanInvitesBtnUnavailable()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\miniclient\lobby\header\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:31 Støední Evropa (bìžný èas)

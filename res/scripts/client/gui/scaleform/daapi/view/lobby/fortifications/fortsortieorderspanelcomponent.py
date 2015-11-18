# 2015.11.18 11:54:05 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/fortifications/FortSortieOrdersPanelComponent.py
import UnitBase
from gui.Scaleform.genConsts.FORTIFICATION_ALIASES import FORTIFICATION_ALIASES
from gui.Scaleform.daapi.view.lobby.fortifications.FortBattleRoomOrdersPanelComponent import FortBattleRoomOrdersPanelComponent

class FortSortieOrdersPanelComponent(FortBattleRoomOrdersPanelComponent):

    def _isConsumablesAvailable(self):
        _, unit = self.unitFunctional.getUnit(self.unitFunctional.getUnitIdx())
        return unit.getRosterTypeID() == UnitBase.ROSTER_TYPE.SORTIE_ROSTER_10

    def _getSlotsProps(self):
        props = super(FortSortieOrdersPanelComponent, self)._getSlotsProps()
        props.update({'panelAlias': FORTIFICATION_ALIASES.FORT_SORTIE_ORDERS_PANEL_COMPONENT_ALIAS})
        return props
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\fortifications\fortsortieorderspanelcomponent.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:54:05 Støední Evropa (bìžný èas)

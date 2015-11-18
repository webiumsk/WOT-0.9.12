# 2015.11.18 11:59:35 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/items/utils.py
from VehicleDescrCrew import VehicleDescrCrew
from VehicleQualifiersApplier import VehicleQualifiersApplier
from items.qualifiers import QUALIFIER_TYPE

def updateVehicleAttrFactors(vehicleDescr, crewCompactDescrs, eqs, factors):
    crewLevelIncrease = vehicleDescr.miscAttrs['crewLevelIncrease'] + sumCrewLevelIncrease(eqs)
    factors['crewLevelIncrease'] = crewLevelIncrease
    mainSkillBonuses = VehicleQualifiersApplier({}, vehicleDescr)[QUALIFIER_TYPE.MAIN_SKILL]
    vehicleDescrCrew = VehicleDescrCrew(vehicleDescr, crewCompactDescrs, mainSkillBonuses)
    vehicleDescrCrew.onCollectFactors(factors)
    for eq in eqs:
        if eq is not None:
            eq.updateVehicleAttrFactors(factors)

    return


def sumCrewLevelIncrease(eqs):
    crewLevelIncrease = 0
    for eq in eqs:
        if eq and hasattr(eq, 'crewLevelIncrease'):
            crewLevelIncrease += eq.crewLevelIncrease

    return crewLevelIncrease
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\items\utils.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:35 Støední Evropa (bìžný èas)

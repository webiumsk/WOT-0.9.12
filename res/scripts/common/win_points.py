# 2015.11.18 11:59:12 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/win_points.py
import ResMgr
from constants import FLAG_TYPES
from items import vehicles
_CONFIG_FILE = 'scripts/item_defs/win_points.xml'

class DamageSettings:

    def __init__(self, section):
        self.pointsForKill = section['winPointsForKill'].asInt
        self.pointsForDamage = (section['winPointsForDamage']['damageToDeal'].asInt, section['winPointsForDamage']['pointsToGrant'].asInt)


class WinPointsTeamOrSoloSettings:

    def __init__(self, section):
        self.vehicleDamageSettings = DamageSettings(section['vehicle'])
        self.equipmentDamageSettings = DamageSettings(section['equipment'])
        self.pointsForFlag = [0] * len(FLAG_TYPES.RANGE)
        for name, subsection in section['winPointsForFlag'].items():
            name = name.upper()
            flagTypeId = getattr(FLAG_TYPES, name, None)
            if flagTypeId is None:
                raise Exception, 'Unknown flag type name (%s)' % (name,)
            self.pointsForFlag[flagTypeId] = subsection.asInt

        self.pointsForOneResource = section['winPointsForOneResource'].asInt
        return


WinPointsTeamSettings = WinPointsTeamOrSoloSettings
WinPointsSoloSettings = WinPointsTeamOrSoloSettings

class WinPointsSettings:

    def __init__(self, section):
        self.pointsCAP = section['winPointsCAP'].asInt
        self.teamSettings = WinPointsTeamSettings(section['team'])
        self.soloSettings = WinPointsSoloSettings(section['solo'])

    def pointsForKill(self, isSolo, forVehicle):
        settings = self.soloSettings if isSolo else self.teamSettings
        damageSettings = settings.vehicleDamageSettings if forVehicle else settings.equipmentDamageSettings
        return damageSettings.pointsForKill

    def pointsForDamage(self, isSolo, forVehicle):
        settings = self.soloSettings if isSolo else self.teamSettings
        damageSettings = settings.vehicleDamageSettings if forVehicle else settings.equipmentDamageSettings
        return damageSettings.pointsForDamage

    def __getattr__(self, item):
        if item in ('pointsForFlag', 'pointsForOneResource'):
            return lambda isSolo: (getattr(self.soloSettings, item) if isSolo else getattr(self.teamSettings, item))
        raise Exception, 'Wrong item to access from WinPointsSettings:%s' % item


g_cache = None

def init():
    global g_cache
    g_cache = settings = {}
    section = ResMgr.openSection(_CONFIG_FILE)
    for name, subsection in section.items():
        settings[name] = WinPointsSettings(subsection)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\win_points.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:12 St�edn� Evropa (b�n� �as)

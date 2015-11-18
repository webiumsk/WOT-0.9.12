# 2015.11.18 11:58:50 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/bonus_readers.py
import time
import items
import calendar
from account_shared import validateCustomizationItem
from dossiers2.custom.layouts import accountDossierLayout, vehicleDossierLayout, StaticSizeBlockBuilder, DictBlockBuilder, ListBlockBuilder, BinarySetDossierBlockBuilder
from items import vehicles, tankmen
__all__ = ['getBonusReaders', 'readUTC', 'SUPPORTED_BONUSES']

def getBonusReaders(bonusTypes):
    return dict(((k, __BONUS_READERS[k]) for k in bonusTypes))


def readUTC(section, field, default = None):
    timeData = section.readString(field, '')
    try:
        if timeData is None:
            raise Exception, 'Wrong timeData'
        if timeData != '':
            timeData = time.strptime(timeData, '%d.%m.%Y %H:%M')
            timeData = int(calendar.timegm(timeData))
        else:
            if default is None:
                raise Exception, 'Wrong default'
            return default
    except:
        raise Exception, 'Invalid %s format (%s). Format must be like %s, for example 23.01.2011 00:00.' % (field, timeData, "'%d.%m.%Y %H:%M'")

    return timeData


def __readBonus_bool(bonus, name, section):
    bonus[name] = section.asBool


def __readBonus_int(bonus, name, section):
    value = section.asInt
    if value < 0:
        raise Exception, 'Negative value (%s)' % name
    bonus[name] = section.asInt


def __readBonus_factor(bonus, name, section):
    value = section.asFloat
    if value < 0:
        raise Exception, 'Negative value (%s)' % name
    bonus[name] = value


def __readBonus_equipment(bonus, _name, section):
    eqName = section.asString
    cache = vehicles.g_cache
    eqID = cache.equipmentIDs().get(eqName)
    if eqID is None:
        raise Exception, "Unknown equipment '%s'" % eqName
    eqCompDescr = cache.equipments()[eqID].compactDescr
    count = 1
    if section.has_key('count'):
        count = section['count'].asInt
    bonus.setdefault('items', {})[eqCompDescr] = count
    return


def __readBonus_optionalDevice(bonus, _name, section):
    name = section.asString
    cache = vehicles.g_cache
    odID = cache.optionalDeviceIDs().get(name)
    if odID is None:
        raise Exception, "Unknown optional device '%s'" % name
    odCompDescr = cache.optionalDevices()[odID].compactDescr
    count = 1
    if section.has_key('count'):
        count = section['count'].asInt
    bonus.setdefault('items', {})[odCompDescr] = count
    return


def __readBonus_item(bonus, _name, section):
    compDescr = section.asInt
    try:
        descr = vehicles.getDictDescr(compDescr)
        if descr['itemTypeName'] not in items.SIMPLE_ITEM_TYPE_NAMES:
            raise Exception, 'Wrong compact descriptor (%d). Not simple item.' % compDescr
    except:
        raise Exception, 'Wrong compact descriptor (%d)' % compDescr

    count = 1
    if section.has_key('count'):
        count = section['count'].asInt
    bonus.setdefault('items', {})[compDescr] = count


def __readBonus_vehicle(bonus, _name, section):
    nationID, innationID = vehicles.g_list.getIDsByName(section.asString)
    vehTypeCompDescr = vehicles.makeIntCompactDescrByID('vehicle', nationID, innationID)
    extra = {}
    if section.has_key('tankmen'):
        __readBonus_tankmen(extra, vehTypeCompDescr, section['tankmen'])
    else:
        if section.has_key('noCrew'):
            extra['noCrew'] = True
        if section.has_key('crewLvl'):
            extra['crewLvl'] = section['crewLvl'].asInt
        if section.has_key('crewFreeXP'):
            extra['crewFreeXP'] = section['crewFreeXP'].asInt
    if section.has_key('rent'):
        __readBonus_rent(extra, None, section['rent'])
    if section.has_key('customCompensation'):
        credits = section['customCompensation'].readInt('credits', 0)
        gold = section['customCompensation'].readInt('gold', 0)
        extra['customCompensation'] = (credits, gold)
    bonus.setdefault('vehicles', {})[vehTypeCompDescr] = extra
    return


def __readBonus_tankmen(bonus, vehTypeCompDescr, section):
    lst = []
    for subsection in section.values():
        tmanDescr = subsection.asString
        if tmanDescr:
            try:
                tman = tankmen.TankmanDescr(tmanDescr)
                if type(vehTypeCompDescr) == int:
                    _, vehNationID, vehicleTypeID = vehicles.parseIntCompactDescr(vehTypeCompDescr)
                    if vehNationID != tman.nationID or vehicleTypeID != tman.vehicleTypeID:
                        raise Exception, 'Vehicle and tankman mismatch.'
            except Exception as e:
                raise Exception, 'Invalid tankmen compact descr. Error: %s' % (e,)

            lst.append(tmanDescr)
            continue
        tmanData = {'isFemale': subsection.readBool('isFemale', False),
         'firstNameID': subsection.readInt('firstNameID', -1),
         'lastNameID': subsection.readInt('lastNameID', -1),
         'role': subsection.readString('role', ''),
         'iconID': subsection.readInt('iconID', -1),
         'roleLevel': subsection.readInt('roleLevel', 50),
         'freeXP': subsection.readInt('freeXP', 0),
         'fnGroupID': subsection.readInt('fnGroupID', 0),
         'lnGroupID': subsection.readInt('lnGroupID', 0),
         'iGroupID': subsection.readInt('iGroupID', 0),
         'isPremium': subsection.readBool('isPremium', False),
         'nationID': subsection.readInt('nationID', -1),
         'vehicleTypeID': subsection.readInt('vehicleTypeID', -1),
         'skills': subsection.readString('skills', '').split(),
         'freeSkills': subsection.readString('freeSkills', '').split()}
        for record in ('firstNameID', 'lastNameID', 'iconID'):
            if tmanData[record] == -1:
                tmanData[record] = None

        try:
            if type(vehTypeCompDescr) == int:
                _, vehNationID, vehicleTypeID = vehicles.parseIntCompactDescr(vehTypeCompDescr)
                if vehNationID != tmanData['nationID'] or vehicleTypeID != tmanData['vehicleTypeID']:
                    raise Exception, 'Vehicle and tankman mismatch.'
            lst.append(tmanData)
        except Exception as e:
            raise Exception, '%s: %s' % (e, tmanData)

    bonus['tankmen'] = lst
    return


def __readBonus_rent(bonus, _name, section):
    rent = {}
    if section.has_key('expires'):
        rent['expires'] = {}
        subsection = section['expires']
        if subsection.has_key('after'):
            rent['expires']['after'] = subsection['after'].asInt
        elif subsection.has_key('at'):
            rent['expires']['at'] = subsection['at'].asInt
        elif subsection.has_key('battles'):
            rent['expires']['battles'] = subsection['battles'].asInt
        else:
            raise Exception, "'expires' section must contain 'at', 'after' or 'battles' sub-section"
    if section.has_key('compensation'):
        credits = section['compensation'].readInt('credits', 0)
        gold = section['compensation'].readInt('gold', 0)
        rent['compensation'] = (credits, gold)
    bonus['rent'] = rent


def __readBonus_customizations(bonus, _name, section):
    lst = []
    for subsection in section.values():
        custData = {'isPermanent': subsection.readBool('isPermanent', False),
         'value': subsection.readInt('value', 0),
         'custType': subsection.readString('custType', ''),
         'id': (subsection.readInt('nationID', -1), subsection.readInt('innationID', -1))}
        if subsection.has_key('boundVehicle'):
            custData['vehTypeCompDescr'] = vehicles.makeIntCompactDescrByID('vehicle', *vehicles.g_list.getIDsByName(subsection.readString('boundVehicle', '')))
        elif subsection.has_key('boundToCurrentVehicle'):
            custData['boundToCurrentVehicle'] = True
        if custData['custType'] == 'emblems':
            custData['id'] = custData['id'][1]
        isValid, reason = validateCustomizationItem(custData)
        if not isValid:
            raise Exception, reason
        if 'boundToCurrentVehicle' in custData:
            customization = vehicles.g_cache.customization
            if custData['custType'] == 'camouflages':
                nationID, innationID = custData['id']
                descr = customization(nationID)['camouflages'][innationID]
                if descr['allow'] or descr['deny']:
                    raise Exception, 'Unsupported camouflage because allow and deny tags %s, %s, %s' % (custData, descr['allow'], descr['deny'])
            elif custData['custType'] == 'inscriptions':
                nationID, innationID = custData['id']
                groupName = customization(nationID)['inscriptions'][innationID][0]
                allow, deny = customization(nationID)['inscriptionGroups'][groupName][3:5]
                if allow or deny:
                    raise Exception, 'Unsupported inscription because allow and deny tags %s, %s, %s' % (custData, allow, deny)
            elif custData['custType'] == 'emblems':
                innationID = custData['id']
                groups, emblems, _ = vehicles.g_cache.playerEmblems()
                allow, deny = groups[emblems[innationID][0]][4:6]
                if allow or deny:
                    raise Exception, 'Unsupported inscription because allow and deny tags %s, %s, %s' % (custData, allow, deny)
        lst.append(custData)

    bonus['customizations'] = lst


def __readBonus_tokens(bonus, _name, section):
    id = section['id'].asString
    token = bonus.setdefault('tokens', {})[id] = {}
    expires = token.setdefault('expires', {})
    __readBonus_expires(id, expires, section)
    if section.has_key('limit'):
        token['limit'] = section['limit'].asInt
    if section.has_key('count'):
        token['count'] = section['count'].asInt


def __readBonus_goodies(bonus, _name, section):
    id = section['id'].asInt
    goodie = bonus.setdefault('goodies', {})[id] = {}
    if section.has_key('limit'):
        goodie['limit'] = section['limit'].asInt
    if section.has_key('count'):
        goodie['count'] = section['count'].asInt
    else:
        goodie['count'] = 1


def __readBonus_expires(id, expires, section):
    if section['expires'].has_key('after'):
        expires['after'] = section['expires']['after'].asInt
    else:
        expires['at'] = readUTC(section, 'expires')


def __readBonus_dossier(bonus, _name, section):
    blockName, record = section['name'].asString.split(':')
    operation = 'add'
    if section.has_key('type'):
        operation = section['type'].asString
    if operation not in ('add', 'append', 'set'):
        raise Exception, 'Invalid dossier record %s' % operation
    value = section['value'].asInt
    unique = False
    if section.has_key('unique'):
        unique = section['unique'].asBool
    for blockBuilder in accountDossierLayout + vehicleDossierLayout:
        if blockBuilder.name == blockName:
            blockType = type(blockBuilder)
            if blockType in (StaticSizeBlockBuilder, BinarySetDossierBlockBuilder):
                if (record in blockBuilder.recordsLayout or record.startswith('tankExpert') or record.startswith('mechanicEngineer')) and operation in ('add', 'set'):
                    break
            elif blockType == DictBlockBuilder and operation == 'add':
                break
            elif blockType == ListBlockBuilder and operation == 'append':
                break
    else:
        raise Exception, 'Invalid dossier record %s or unsupported block' % (blockName + ':' + record,)

    bonus.setdefault('dossier', {})[blockName, record] = {'value': value,
     'unique': unique,
     'type': operation}


__BONUS_READERS = {'buyAllVehicles': __readBonus_bool,
 'equipGold': __readBonus_bool,
 'ultimateLoginPriority': __readBonus_bool,
 'addTankmanSkills': __readBonus_bool,
 'premiumAmmo': __readBonus_int,
 'gold': __readBonus_int,
 'credits': __readBonus_int,
 'freeXP': __readBonus_int,
 'slots': __readBonus_int,
 'berths': __readBonus_int,
 'premium': __readBonus_int,
 'xp': __readBonus_int,
 'tankmenXP': __readBonus_int,
 'trainCommander': __readBonus_int,
 'maxVehicleLevel': __readBonus_int,
 'xpFactor': __readBonus_factor,
 'creditsFactor': __readBonus_factor,
 'freeXPFactor': __readBonus_factor,
 'tankmenXPFactor': __readBonus_factor,
 'item': __readBonus_item,
 'equipment': __readBonus_equipment,
 'optionalDevice': __readBonus_optionalDevice,
 'token': __readBonus_tokens,
 'goodie': __readBonus_goodies,
 'vehicle': __readBonus_vehicle,
 'dossier': __readBonus_dossier,
 'tankmen': __readBonus_tankmen,
 'customizations': __readBonus_customizations}
SUPPORTED_BONUSES = frozenset(__BONUS_READERS.iterkeys())
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\bonus_readers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:58:50 St�edn� Evropa (b�n� �as)

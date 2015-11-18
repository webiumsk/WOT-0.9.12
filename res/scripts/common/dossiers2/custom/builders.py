# 2015.11.18 11:59:16 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/dossiers2/custom/builders.py
import time
from constants import DOSSIER_TYPE
from dossiers2.common.DossierBuilder import DossierBuilder
from dossiers2.common.utils import getDossierVersion
from layouts import *
from updaters import *
getAccountDossierVersion = lambda dossierCompDescr: getDossierVersion(dossierCompDescr, '<' + VERSION_RECORD_FORMAT, ACCOUNT_DOSSIER_VERSION)
getVehicleDossierVersion = lambda dossierCompDescr: getDossierVersion(dossierCompDescr, '<' + VERSION_RECORD_FORMAT, VEHICLE_DOSSIER_VERSION)
getTankmanDossierVersion = lambda dossierCompDescr: getDossierVersion(dossierCompDescr, '<' + VERSION_RECORD_FORMAT, TANKMAN_DOSSIER_VERSION)
getFortifiedRegionsDossierVersion = lambda dossierCompDescr: getDossierVersion(dossierCompDescr, '<' + VERSION_RECORD_FORMAT, FORT_DOSSIER_VERSION)

def _initializeNewDossier(dossierType, dossier):
    if dossierType == DOSSIER_TYPE.ACCOUNT:
        dossier['total']['creationTime'] = int(time.time())
    elif dossierType == DOSSIER_TYPE.VEHICLE:
        dossier['total']['creationTime'] = int(time.time())
    elif dossierType == DOSSIER_TYPE.FORTIFIED_REGIONS:
        dossier['total']['creationTime'] = int(time.time())
    elif dossierType == DOSSIER_TYPE.TANKMAN:
        pass


getAccountDossierDescr = DossierBuilder(accountDossierLayout, VERSION_RECORD_FORMAT, BLOCK_SIZE_RECORD_FORMAT, ACCOUNT_DOSSIER_VERSION, accountVersionUpdaters, lambda d: _initializeNewDossier(DOSSIER_TYPE.ACCOUNT, d)).build
getVehicleDossierDescr = DossierBuilder(vehicleDossierLayout, VERSION_RECORD_FORMAT, BLOCK_SIZE_RECORD_FORMAT, VEHICLE_DOSSIER_VERSION, vehicleVersionUpdaters, lambda d: _initializeNewDossier(DOSSIER_TYPE.VEHICLE, d)).build
getTankmanDossierDescr = DossierBuilder(tmanDossierLayout, VERSION_RECORD_FORMAT, BLOCK_SIZE_RECORD_FORMAT, TANKMAN_DOSSIER_VERSION, tankmanVersionUpdaters, lambda d: _initializeNewDossier(DOSSIER_TYPE.TANKMAN, d)).build
getFortifiedRegionsDossierDescr = DossierBuilder(fortDossierLayout, VERSION_RECORD_FORMAT, BLOCK_SIZE_RECORD_FORMAT, FORT_DOSSIER_VERSION, fortVersionUpdaters, lambda d: _initializeNewDossier(DOSSIER_TYPE.FORTIFIED_REGIONS, d)).build
getRated7x7DossierDescr = DossierBuilder(rated7x7DossierLayout, VERSION_RECORD_FORMAT, BLOCK_SIZE_RECORD_FORMAT, RATED7X7_DOSSIER_VERSION, rated7x7VersionUpdaters, lambda d: _initializeNewDossier(DOSSIER_TYPE.RATED7X7, d)).build
getClubDossierDescr = DossierBuilder(clubDossierLayout, VERSION_RECORD_FORMAT, BLOCK_SIZE_RECORD_FORMAT, CLUB_DOSSIER_VERSION, clubVersionUpdaters, lambda d: _initializeNewDossier(DOSSIER_TYPE.CLUB, d)).build
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\dossiers2\custom\builders.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:17 St�edn� Evropa (b�n� �as)

# 2015.11.18 11:59:15 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/dossiers2/custom/account_layout.py
from dossiers2.common.DossierBlockBuilders import *
from dossiers2.custom.dependencies import ACHIEVEMENT15X15_DEPENDENCIES
from dossiers2.custom.dependencies import ACHIEVEMENT7X7_DEPENDENCIES
from dossiers2.custom.dependencies import ACHIEVEMENTRATED7X7_DEPENDENCIES
from dossiers2.custom.dependencies import HISTORICAL_ACHIEVEMENTS_DEPENDENCIES
from dossiers2.custom.dependencies import FALLOUT_STATS_DEPENDENCIES
from dossiers2.custom.dependencies import FORT_ACHIEVEMENTS_DEPENDENCIES
from dossiers2.custom.dependencies import FORT_MISC_DEPENDENCIES
from dossiers2.custom.dependencies import GLOBAL_MAP_STATS_DEPENDENCIES
from battle_statistics_layouts import *
TOTAL_BLOCK_LAYOUT = ['creationTime',
 'lastBattleTime',
 'battleLifeTime',
 'treesCut',
 'mileage']
_totalBlockBuilder = StaticSizeBlockBuilder('total', TOTAL_BLOCK_LAYOUT, {}, [])
FORT_SORTIE_BLOCK_LAYOUT = FORT_BLOCK_LAYOUT + ['middleBattlesCount',
 'championBattlesCount',
 'absoluteBattlesCount',
 'middleWins',
 'championWins',
 'absoluteWins',
 'fortResource']
_a15x15BlockBuilder = StaticSizeBlockBuilder('a15x15', A15X15_BLOCK_LAYOUT, A15X15_STATS_DEPENDENCIES, [])
_a15x15_2BlockBuilder = StaticSizeBlockBuilder('a15x15_2', A15X15_2_BLOCK_LAYOUT, {}, [])
_clanBlockBuilder = StaticSizeBlockBuilder('clan', CLAN_BLOCK_LAYOUT, CLAN_STATS_DEPENDENCIES, [])
_clan2BlockBuilder = StaticSizeBlockBuilder('clan2', CLAN2_BLOCK_LAYOUT, {}, [])
_companyBlockBuilder = StaticSizeBlockBuilder('company', COMPANY_BLOCK_LAYOUT, {}, [])
_company2BlockBuilder = StaticSizeBlockBuilder('company2', COMPANY2_BLOCK_LAYOUT, {}, [])
_a7x7BlockBuilder = StaticSizeBlockBuilder('a7x7', A7X7_BLOCK_LAYOUT, A7X7_STATS_DEPENDENCIES, [])
_rated7x7BlockBuilder = StaticSizeBlockBuilder('rated7x7', RATED_7X7_BLOCK_LAYOUT, {}, [])
_historicalBlockBuilder = StaticSizeBlockBuilder('historical', HISTORICAL_BLOCK_LAYOUT, HISTORICAL_STATS_DEPENDENCIES, [])
_fortBattlesInClanBlockBuilder = StaticSizeBlockBuilder('fortBattlesInClan', FORT_BLOCK_LAYOUT, {}, [])
_fortSortiesInClanBlockBuilder = StaticSizeBlockBuilder('fortSortiesInClan', FORT_SORTIE_BLOCK_LAYOUT, {}, [])
_fortBattlesBlockBuilder = StaticSizeBlockBuilder('fortBattles', FORT_BLOCK_LAYOUT, FORT_BATTLES_STATS_DEPENDENCIES, [])
_fortSortiesBlockBuilder = StaticSizeBlockBuilder('fortSorties', FORT_BLOCK_LAYOUT, FORT_SORTIES_STATS_DEPENDENCIES, [])
_globalMapMiddleBlockBuilder = StaticSizeBlockBuilder('globalMapMiddle', GLOBAL_MAP_BLOCK_LAYOUT, GLOBAL_MAP_STATS_DEPENDENCIES, [])
_globalMapChampionBlockBuilder = StaticSizeBlockBuilder('globalMapChampion', GLOBAL_MAP_BLOCK_LAYOUT, GLOBAL_MAP_STATS_DEPENDENCIES, [])
_globalMapAbsoluteBlockBuilder = StaticSizeBlockBuilder('globalMapAbsolute', GLOBAL_MAP_BLOCK_LAYOUT, GLOBAL_MAP_STATS_DEPENDENCIES, [])
_falloutBlockBuilder = StaticSizeBlockBuilder('fallout', FALLOUT_BLOCK_LAYOUT, FALLOUT_STATS_DEPENDENCIES, [])
_max15x15BlockBuilder = StaticSizeBlockBuilder('max15x15', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_max7x7BlockBuilder = StaticSizeBlockBuilder('max7x7', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxRated7x7BlockBuilder = StaticSizeBlockBuilder('maxRated7x7', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxHistoricalBlockBuilder = StaticSizeBlockBuilder('maxHistorical', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxFortBattlesBlockBuilder = StaticSizeBlockBuilder('maxFortBattles', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxFortSortiesBlockBuilder = StaticSizeBlockBuilder('maxFortSorties', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxFortBattlesInClanBlockBuilder = StaticSizeBlockBuilder('maxFortBattlesInClan', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxFortSortiesInClanBlockBuilder = StaticSizeBlockBuilder('maxFortSortiesInClan', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxGlobalMapMiddleBlockBuilder = StaticSizeBlockBuilder('maxGlobalMapMiddle', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxGlobalMapChampionBlockBuilder = StaticSizeBlockBuilder('maxGlobalMapChampion', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxGlobalMapAbsoluteBlockBuilder = StaticSizeBlockBuilder('maxGlobalMapAbsolute', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxFalloutBlockBuilder = StaticSizeBlockBuilder('maxFallout', MAX_FALLOUT_BLOCK_LAYOUT_WITH_AVATAR, {}, [])
_vehTypeFragsBlockBuilder = DictBlockBuilder('vehTypeFrags', 'I', 'H', VEH_TYPE_FRAGS_DEPENDENCIES)
_a15x15CutBlockBuilder = DictBlockBuilder('a15x15Cut', 'I', 'IIII', {})
_a7x7CutBlockBuilder = DictBlockBuilder('a7x7Cut', 'I', 'IIIIIII', {})
_rated7x7CutBlockBuilder = DictBlockBuilder('rated7x7Cut', 'I', 'IIIIIII', {})
_historicalCutBlockBuilder = DictBlockBuilder('historicalCut', 'I', 'III', {})
_fortBattlesCutBlockBuilder = DictBlockBuilder('fortBattlesCut', 'I', 'III', {})
_fortSortiesCutBlockBuilder = DictBlockBuilder('fortSortiesCut', 'I', 'III', {})
_globalMapCommonCutBlockBuilder = DictBlockBuilder('globalMapCommonCut', 'I', 'III', {})
_falloutCutBlockBuilder = DictBlockBuilder('falloutCut', 'I', 'IIII', {})
_ACHIEVEMENTS15X15_BLOCK_LAYOUT = ['fragsBeast',
 'sniperSeries',
 'maxSniperSeries',
 'invincibleSeries',
 'maxInvincibleSeries',
 'diehardSeries',
 'maxDiehardSeries',
 'killingSeries',
 'fragsSinai',
 'maxKillingSeries',
 'piercingSeries',
 'maxPiercingSeries',
 'battleHeroes',
 'warrior',
 'invader',
 'sniper',
 'defender',
 'steelwall',
 'supporter',
 'scout',
 'evileye',
 'medalKay',
 'medalCarius',
 'medalKnispel',
 'medalPoppel',
 'medalAbrams',
 'medalLeClerc',
 'medalLavrinenko',
 'medalEkins',
 'medalWittmann',
 'medalOrlik',
 'medalOskin',
 'medalHalonen',
 'medalBurda',
 'medalBillotte',
 'medalKolobanov',
 'medalFadin',
 'medalRadleyWalters',
 'medalBrunoPietro',
 'medalTarczay',
 'medalPascucci',
 'medalDumitru',
 'medalLehvaslaiho',
 'medalNikolas',
 'medalLafayettePool',
 'sinai',
 'heroesOfRassenay',
 'beasthunter',
 'mousebane',
 'tankExpertStrg',
 'raider',
 'kamikaze',
 'lumberjack',
 'medalBrothersInArms',
 'medalCrucialContribution',
 'medalDeLanglade',
 'medalTamadaYoshio',
 'bombardier',
 'huntsman',
 'alaric',
 'sturdy',
 'ironMan',
 'luckyDevil',
 'pattonValley',
 'fragsPatton',
 'mechanicEngineerStrg',
 'sniper2',
 'mainGun',
 'medalMonolith',
 'medalAntiSpgFire',
 'medalGore',
 'medalCoolBlood',
 'medalStark',
 'maxWFC2014WinSeries',
 'WFC2014WinSeries',
 'impenetrable',
 'reliableComradeSeries',
 'reliableComrade',
 'maxAimerSeries',
 'shootToKill',
 'fighter',
 'duelist',
 'demolition',
 'arsonist',
 'bonecrusher',
 'charmed',
 'even',
 'maxDeathTrackWinSeries',
 'deathTrackWinSeries',
 'readyForBattleLT',
 'readyForBattleMT',
 'readyForBattleHT',
 'readyForBattleSPG',
 'readyForBattleATSPG',
 'readyForBattleALL',
 'tankwomenProgress',
 'testartilleryman']
_achievements15x15PopUps = ['warrior',
 'invader',
 'sniper',
 'defender',
 'steelwall',
 'supporter',
 'scout',
 'medalKay',
 'medalCarius',
 'medalKnispel',
 'medalPoppel',
 'medalAbrams',
 'medalLeClerc',
 'medalLavrinenko',
 'medalEkins',
 'medalWittmann',
 'medalOrlik',
 'medalOskin',
 'medalHalonen',
 'medalBurda',
 'medalBillotte',
 'medalKolobanov',
 'medalFadin',
 'beasthunter',
 'mousebane',
 'tankExpert',
 'raider',
 'kamikaze',
 'lumberjack',
 'evileye',
 'medalRadleyWalters',
 'medalLafayettePool',
 'medalBrunoPietro',
 'medalTarczay',
 'medalPascucci',
 'medalDumitru',
 'medalLehvaslaiho',
 'medalNikolas',
 'sinai',
 'pattonValley',
 'heroesOfRassenay',
 'mechanicEngineer',
 'tankExpert0',
 'tankExpert1',
 'tankExpert2',
 'tankExpert3',
 'tankExpert4',
 'tankExpert5',
 'tankExpert6',
 'tankExpert7',
 'tankExpert8',
 'tankExpert9',
 'tankExpert10',
 'tankExpert11',
 'tankExpert12',
 'tankExpert13',
 'tankExpert14',
 'mechanicEngineer0',
 'mechanicEngineer1',
 'mechanicEngineer2',
 'mechanicEngineer3',
 'mechanicEngineer4',
 'mechanicEngineer5',
 'mechanicEngineer6',
 'mechanicEngineer7',
 'mechanicEngineer8',
 'mechanicEngineer9',
 'mechanicEngineer10',
 'mechanicEngineer11',
 'mechanicEngineer12',
 'mechanicEngineer13',
 'mechanicEngineer14',
 'medalBrothersInArms',
 'medalCrucialContribution',
 'medalDeLanglade',
 'medalTamadaYoshio',
 'bombardier',
 'huntsman',
 'alaric',
 'sturdy',
 'ironMan',
 'luckyDevil',
 'sniper2',
 'mainGun',
 'medalMonolith',
 'medalAntiSpgFire',
 'medalGore',
 'medalCoolBlood',
 'medalStark',
 'impenetrable',
 'reliableComrade',
 'shootToKill',
 'fighter',
 'duelist',
 'demolition',
 'arsonist',
 'bonecrusher',
 'charmed',
 'even',
 'readyForBattleLT',
 'readyForBattleMT',
 'readyForBattleHT',
 'readyForBattleSPG',
 'readyForBattleATSPG',
 'readyForBattleALL',
 'testartilleryman']
_achievements15x15BlockBuilder = StaticSizeBlockBuilder('achievements', _ACHIEVEMENTS15X15_BLOCK_LAYOUT, ACHIEVEMENT15X15_DEPENDENCIES, _achievements15x15PopUps)
ACHIEVEMENTS7X7_BLOCK_LAYOUT = ['wolfAmongSheep',
 'wolfAmongSheepMedal',
 'geniusForWar',
 'geniusForWarMedal',
 'kingOfTheHill',
 'tacticalBreakthroughSeries',
 'maxTacticalBreakthroughSeries',
 'armoredFist',
 'godOfWar',
 'fightingReconnaissance',
 'fightingReconnaissanceMedal',
 'willToWinSpirit',
 'crucialShot',
 'crucialShotMedal',
 'forTacticalOperations',
 'promisingFighter',
 'promisingFighterMedal',
 'heavyFire',
 'heavyFireMedal',
 'ranger',
 'rangerMedal',
 'fireAndSteel',
 'fireAndSteelMedal',
 'pyromaniac',
 'pyromaniacMedal',
 'noMansLand',
 'guerrilla',
 'guerrillaMedal',
 'infiltrator',
 'infiltratorMedal',
 'sentinel',
 'sentinelMedal',
 'prematureDetonation',
 'prematureDetonationMedal',
 'bruteForce',
 'bruteForceMedal',
 'awardCount',
 'battleTested']
_achievement7x7PopUps = ['wolfAmongSheepMedal',
 'geniusForWarMedal',
 'kingOfTheHill',
 'armoredFist',
 'godOfWar',
 'forTacticalOperations',
 'crucialShotMedal',
 'willToWinSpirit',
 'fightingReconnaissanceMedal',
 'promisingFighterMedal',
 'heavyFireMedal',
 'rangerMedal',
 'fireAndSteelMedal',
 'pyromaniacMedal',
 'noMansLand',
 'guerrillaMedal',
 'infiltratorMedal',
 'sentinelMedal',
 'prematureDetonationMedal',
 'bruteForceMedal',
 'battleTested']
_achievements7x7BlockBuilder = StaticSizeBlockBuilder('achievements7x7', ACHIEVEMENTS7X7_BLOCK_LAYOUT, ACHIEVEMENT7X7_DEPENDENCIES, _achievement7x7PopUps)
ACHIEVEMENTSRATED7X7_BLOCK_LAYOUT = ['tacticalAdvantage',
 'tacticalSkill',
 'secretOperations',
 'victoryMarchClubDBID',
 'victoryMarchSeries',
 'maxVictoryMarchSeries']
_achievementRated7x7PopUps = ['tacticalAdvantage', 'tacticalSkill', 'secretOperations']
_achievementsRated7x7BlockBuilder = StaticSizeBlockBuilder('achievementsRated7x7', ACHIEVEMENTSRATED7X7_BLOCK_LAYOUT, ACHIEVEMENTRATED7X7_DEPENDENCIES, _achievementRated7x7PopUps)
HISTORICAL_ACHIEVEMENTS_BLOCK_LAYOUT = ['guardsman',
 'makerOfHistory',
 'bothSidesWins',
 'weakVehiclesWins']
_historicalAchievementsPopUps = ['guardsman', 'makerOfHistory']
_historicalAchievementsBlockBuilder = StaticSizeBlockBuilder('historicalAchievements', HISTORICAL_ACHIEVEMENTS_BLOCK_LAYOUT, HISTORICAL_ACHIEVEMENTS_DEPENDENCIES, _historicalAchievementsPopUps)
_SINGLE_ACHIEVEMENTS_VALUES = ['titleSniper',
 'invincible',
 'diehard',
 'handOfDeath',
 'armorPiercer',
 'battleCitizen',
 'WFC2014',
 'tacticalBreakthrough',
 'aimer',
 'deathTrack',
 'firstMerit',
 'tankwomen',
 'operationWinter',
 'victoryMarch',
 'fallout',
 'fallout2',
 'falloutSingleWolf',
 'falloutPackOfWolfs',
 'falloutSteelHunter',
 'falloutAlwaysInLine']
_singleAchievementsPopUps = ['titleSniper',
 'invincible',
 'diehard',
 'handOfDeath',
 'armorPiercer',
 'battleCitizen',
 'WFC2014',
 'tacticalBreakthrough',
 'aimer',
 'deathTrack',
 'firstMerit',
 'tankwomen',
 'operationWinter',
 'victoryMarch',
 'fallout',
 'fallout2',
 'falloutSingleWolf',
 'falloutPackOfWolfs',
 'falloutSteelHunter',
 'falloutAlwaysInLine']
_singleAchievementsBlockBuilder = BinarySetDossierBlockBuilder('singleAchievements', _SINGLE_ACHIEVEMENTS_VALUES, {}, _singleAchievementsPopUps)
FORT_ACHIEVEMENTS_BLOCK_LAYOUT = ['conqueror',
 'fireAndSword',
 'crusher',
 'counterblow',
 'kampfer',
 'soldierOfFortune',
 'wins',
 'capturedBasesInAttack',
 'capturedBasesInDefence']
_fortPersonalAchievementsPopUps = ['conqueror',
 'fireAndSword',
 'crusher',
 'counterblow',
 'kampfer',
 'soldierOfFortune']
_fortPersonalAchievementsBlockBuilder = StaticSizeBlockBuilder('fortAchievements', FORT_ACHIEVEMENTS_BLOCK_LAYOUT, FORT_ACHIEVEMENTS_DEPENDENCIES, _fortPersonalAchievementsPopUps)
CLAN_ACHIEVEMENTS_BLOCK_LAYOUT = ['medalRotmistrov']
_clanAchievementsPopUps = ['medalRotmistrov']
_clanAchievementsBlockBuilder = StaticSizeBlockBuilder('clanAchievements', CLAN_ACHIEVEMENTS_BLOCK_LAYOUT, {}, _clanAchievementsPopUps)
_rareAchievementsBlockBuilder = ListBlockBuilder('rareAchievements', 'I', {})
UNIQUE_ACHIEVEMENT_VALUES = ['histBattle1_battlefield',
 'histBattle1_historyLessons',
 'histBattle2_battlefield',
 'histBattle2_historyLessons',
 'histBattle3_battlefield',
 'histBattle3_historyLessons',
 'histBattle4_battlefield',
 'histBattle4_historyLessons',
 'histBattle5_battlefield',
 'histBattle5_historyLessons',
 'histBattle6_battlefield',
 'histBattle6_historyLessons']
_uniqueAchievementPopUps = ['histBattle1_battlefield',
 'histBattle1_historyLessons',
 'histBattle2_battlefield',
 'histBattle2_historyLessons',
 'histBattle3_battlefield',
 'histBattle3_historyLessons',
 'histBattle4_battlefield',
 'histBattle4_historyLessons',
 'histBattle5_battlefield',
 'histBattle5_historyLessons',
 'histBattle6_battlefield',
 'histBattle6_historyLessons']
_uniqueAchievementBlockBuilder = BinarySetDossierBlockBuilder('uniqueAchievements', UNIQUE_ACHIEVEMENT_VALUES, {}, _uniqueAchievementPopUps)
FORT_MISC_LAYOUT = ['fortResourceInBattles',
 'maxFortResourceInBattles',
 'fortResourceInSorties',
 'maxFortResourceInSorties',
 'defenceHours',
 'successfulDefenceHours',
 'attackNumber',
 'enemyBasePlunderNumber',
 'enemyBasePlunderNumberInAttack']
_fortMiscBlockBuilder = StaticSizeBlockBuilder('fortMisc', FORT_MISC_LAYOUT, FORT_MISC_DEPENDENCIES, [])
_fortMiscInClanBlockBuilder = StaticSizeBlockBuilder('fortMiscInClan', FORT_MISC_LAYOUT, {}, [])
FALLOUT_ACHIEVEMENTS_BLOCK_LAYOUT = ['shoulderToShoulder',
 'aloneInTheField',
 'fallenFlags',
 'effectiveSupport',
 'stormLord',
 'winnerLaurels',
 'predator',
 'unreachable',
 'champion',
 'bannerman',
 'falloutDieHard',
 'sauronEye']
_falloutAchievementsPopUps = ['shoulderToShoulder',
 'aloneInTheField',
 'fallenFlags',
 'effectiveSupport',
 'stormLord',
 'winnerLaurels',
 'predator',
 'unreachable',
 'champion',
 'bannerman',
 'falloutDieHard',
 'sauronEye']
_falloutAchievementsBlockBuilder = StaticSizeBlockBuilder('falloutAchievements', FALLOUT_ACHIEVEMENTS_BLOCK_LAYOUT, {}, _falloutAchievementsPopUps)
accountDossierLayout = (_a15x15BlockBuilder,
 _a15x15_2BlockBuilder,
 _clanBlockBuilder,
 _clan2BlockBuilder,
 _companyBlockBuilder,
 _company2BlockBuilder,
 _a7x7BlockBuilder,
 _achievements15x15BlockBuilder,
 _vehTypeFragsBlockBuilder,
 _a15x15CutBlockBuilder,
 _rareAchievementsBlockBuilder,
 _totalBlockBuilder,
 _a7x7CutBlockBuilder,
 _max15x15BlockBuilder,
 _max7x7BlockBuilder,
 _achievements7x7BlockBuilder,
 _historicalBlockBuilder,
 _maxHistoricalBlockBuilder,
 _historicalAchievementsBlockBuilder,
 _historicalCutBlockBuilder,
 _uniqueAchievementBlockBuilder,
 _fortBattlesBlockBuilder,
 _maxFortBattlesBlockBuilder,
 _fortBattlesCutBlockBuilder,
 _fortSortiesBlockBuilder,
 _maxFortSortiesBlockBuilder,
 _fortSortiesCutBlockBuilder,
 _fortBattlesInClanBlockBuilder,
 _maxFortBattlesInClanBlockBuilder,
 _fortSortiesInClanBlockBuilder,
 _maxFortSortiesInClanBlockBuilder,
 _fortMiscBlockBuilder,
 _fortMiscInClanBlockBuilder,
 _fortPersonalAchievementsBlockBuilder,
 _singleAchievementsBlockBuilder,
 _clanAchievementsBlockBuilder,
 _rated7x7BlockBuilder,
 _maxRated7x7BlockBuilder,
 _achievementsRated7x7BlockBuilder,
 _rated7x7CutBlockBuilder,
 _globalMapMiddleBlockBuilder,
 _globalMapChampionBlockBuilder,
 _globalMapAbsoluteBlockBuilder,
 _maxGlobalMapMiddleBlockBuilder,
 _maxGlobalMapChampionBlockBuilder,
 _maxGlobalMapAbsoluteBlockBuilder,
 _globalMapCommonCutBlockBuilder,
 _falloutBlockBuilder,
 _falloutCutBlockBuilder,
 _maxFalloutBlockBuilder,
 _falloutAchievementsBlockBuilder)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\dossiers2\custom\account_layout.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:15 St�edn� Evropa (b�n� �as)

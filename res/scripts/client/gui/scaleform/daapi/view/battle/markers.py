# 2015.11.18 11:53:10 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/markers.py
from functools import partial
import math
import weakref
from Math import Vector3, Matrix
from CTFManager import g_ctfManager
from account_helpers.settings_core import g_settingsCore
import constants
import GUI
import BigWorld
from gui.battle_control.dyn_squad_functional import IDynSquadEntityClient
from gui.battle_control.gas_attack_controller import GAS_ATTACK_STATE
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.events import GameEvent
from gui.shared.utils.plugins import PluginsCollection, IPlugin
from helpers import i18n, time_utils
from debug_utils import LOG_ERROR
from gui import DEPTH_OF_VehicleMarker, GUI_SETTINGS
from gui.Scaleform import VoiceChatInterface, ColorSchemeManager
from gui.Scaleform.Flash import Flash
from gui.Scaleform.locale.INGAME_GUI import INGAME_GUI
from gui.battle_control import g_sessionProvider, avatar_getter, arena_info
from gui.battle_control.arena_info.arena_vos import VehicleActions
from gui.battle_control.battle_constants import PLAYER_GUI_PROPS, NEUTRAL_TEAM
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as _EVENT_ID
_SCOPE = EVENT_BUS_SCOPE.BATTLE
_MARKER_POSITION_ADJUSTMENT = Vector3(0.0, 12.0, 0.0)
_MARKERS_MANAGER_SWF = 'VehicleMarkersManager.swf'

class _DAMAGE_TYPE():
    FROM_UNKNOWN = 0
    FROM_ALLY = 1
    FROM_ENEMY = 2
    FROM_SQUAD = 3
    FROM_PLAYER = 4


_EQUIPMENT_MARKER_TYPE = 'FortConsumablesMarker'
_FLAG_MARKER_TYPE = 'FlagIndicatorUI'
_FLAG_CAPTURE_MARKER_TYPE = 'CaptureIndicatorUI'

class _FLAG_TYPE():
    ALLY = 'ally'
    ENEMY = 'enemy'
    NEUTRAL = 'neutral'
    REPAIR = 'repair'
    COOLDOWN = 'cooldown'


_REPAIR_MARKER_TYPE = 'RepairPointIndicatorUI'
_SAFE_ZONE_MARKER_TYPE = 'SafeZoneIndicatorUI'
_RESOURCE_MARKER_TYPE = 'ResourcePointMarkerUI'

class _RESOURCE_STATE():
    FREEZE = 'freeze'
    COOLDOWN = 'cooldown'
    READY = 'ready'
    OWN_MINING = 'ownMining'
    ENEMY_MINING = 'enemyMining'
    OWN_MINING_FROZEN = 'ownMiningFrozen'
    ENEMY_MINING_FROZEN = 'enemyMiningFrozen'
    CONFLICT = 'conflict'


_CAPTURE_STATE_BY_TEAMS = {True: _RESOURCE_STATE.OWN_MINING,
 False: _RESOURCE_STATE.ENEMY_MINING}
_CAPTURE_FROZEN_STATE_BY_TEAMS = {True: _RESOURCE_STATE.OWN_MINING_FROZEN,
 False: _RESOURCE_STATE.ENEMY_MINING_FROZEN}

class MarkersManager(Flash, IDynSquadEntityClient):

    def __init__(self, parentUI):
        Flash.__init__(self, _MARKERS_MANAGER_SWF)
        self.component.wg_inputKeyMode = 2
        self.component.position.z = DEPTH_OF_VehicleMarker
        self.component.drawWithRestrictedViewPort = False
        self.movie.backgroundAlpha = 0
        self.colorManager = ColorSchemeManager._ColorSchemeManager()
        self.colorManager.populateUI(weakref.proxy(self))
        self.__plugins = PluginsCollection(self)
        plugins = {'equipments': _EquipmentsMarkerPlugin}
        if arena_info.hasFlags():
            plugins['flags'] = _FlagsMarkerPlugin
        if arena_info.hasRepairPoints():
            plugins['repairs'] = _RepairsMarkerPlugin
        if arena_info.hasResourcePoints():
            plugins['resources'] = _ResourceMarkerPlugin
        if arena_info.hasGasAttack():
            plugins['safe_zone'] = _GasAttackSafeZonePlugin
        self.__plugins.addPlugins(plugins)
        self.__ownUI = None
        self.__parentUI = parentUI
        self.__markers = {}
        return

    def updateSquadmanVeh(self, vID):
        if vID not in self.__markers:
            return
        marker = self.__markers[vID]
        self.invokeMarker(marker.id, 'setEntityName', [PLAYER_GUI_PROPS.squadman.name()])

    def setScaleProps(self, minScale = 40, maxScale = 100, defScale = 100, speed = 3.0):
        if constants.IS_DEVELOPMENT:
            self.__ownUI.scaleProperties = (minScale,
             maxScale,
             defScale,
             speed)

    def setAlphaProps(self, minAlpha = 40, maxAlpha = 100, defAlpha = 100, speed = 3.0):
        if constants.IS_DEVELOPMENT:
            self.__ownUI.alphaProperties = (minAlpha,
             maxAlpha,
             defAlpha,
             speed)

    def start(self):
        self.active(True)
        self.__ownUI = GUI.WGVehicleMarkersCanvasFlash(self.movie)
        self.__ownUI.wg_inputKeyMode = 2
        self.__ownUI.scaleProperties = GUI_SETTINGS.markerScaleSettings
        self.__ownUI.alphaProperties = GUI_SETTINGS.markerBgSettings
        self.__ownUIProxy = weakref.ref(self.__ownUI)
        self.__ownUIProxy().markerSetScale(g_settingsCore.interfaceScale.get())
        g_settingsCore.interfaceScale.onScaleChanged += self.updateMarkersScale
        self.__parentUI.component.addChild(self.__ownUI, 'vehicleMarkersManager')
        self.__markersCanvasUI = self.getMember('vehicleMarkersCanvas')
        self.__plugins.init()
        ctrl = g_sessionProvider.getFeedback()
        if ctrl:
            ctrl.onVehicleMarkerAdded += self.__onVehicleMarkerAdded
            ctrl.onVehicleMarkerRemoved += self.__onVehicleMarkerRemoved
            ctrl.onVehicleFeedbackReceived += self.__onVehicleFeedbackReceived
        self.__plugins.start()
        g_eventBus.addListener(GameEvent.SHOW_EXTENDED_INFO, self.__handleShowExtendedInfo, scope=_SCOPE)
        g_eventBus.addListener(GameEvent.GUI_VISIBILITY, self.__handleGUIVisibility, scope=_SCOPE)

    def destroy(self):
        g_eventBus.removeListener(GameEvent.SHOW_EXTENDED_INFO, self.__handleShowExtendedInfo, scope=_SCOPE)
        g_eventBus.removeListener(GameEvent.GUI_VISIBILITY, self.__handleGUIVisibility, scope=_SCOPE)
        self.__plugins.stop()
        g_settingsCore.interfaceScale.onScaleChanged -= self.updateMarkersScale
        ctrl = g_sessionProvider.getFeedback()
        if ctrl:
            ctrl.onVehicleMarkerAdded -= self.__onVehicleMarkerAdded
            ctrl.onVehicleMarkerRemoved -= self.__onVehicleMarkerRemoved
            ctrl.onVehicleFeedbackReceived -= self.__onVehicleFeedbackReceived
        if self.__parentUI is not None:
            setattr(self.__parentUI.component, 'vehicleMarkersManager', None)
        self.__plugins.fini()
        self.__parentUI = None
        self.__ownUI = None
        self.__markersCanvasUI = None
        self.colorManager.dispossessUI()
        self.close()
        return

    def _createVehicleMarker(self, isAlly, mProv):
        markerLinkage = 'VehicleMarkerAlly' if isAlly else 'VehicleMarkerEnemy'
        if arena_info.hasFlags():
            markerID = self.__ownUI.addFalloutMarker(mProv, markerLinkage)
        else:
            markerID = self.__ownUI.addMarker(mProv, markerLinkage)
        return markerID

    def addVehicleMarker(self, vProxy, vInfo, guiProps):
        vTypeDescr = vProxy.typeDescriptor
        maxHealth = vTypeDescr.maxHealth
        mProv = vProxy.model.node('HP_gui')
        isAlly = guiProps.isFriend
        speaking = False
        if GUI_SETTINGS.voiceChat:
            speaking = VoiceChatInterface.g_instance.isPlayerSpeaking(vInfo.player.accountDBID)
        hunting = VehicleActions.isHunting(vInfo.events)
        markerID = self._createVehicleMarker(isAlly, mProv)
        self.__markers[vInfo.vehicleID] = _VehicleMarker(markerID, vProxy, self.__ownUIProxy)
        battleCtx = g_sessionProvider.getCtx()
        fullName, pName, clanAbbrev, regionCode, vehShortName = battleCtx.getFullPlayerNameWithParts(vProxy.id)
        vType = vInfo.vehicleType
        squadIcon = ''
        if arena_info.getIsMultiteam() and vInfo.isSquadMan():
            teamIdx = g_sessionProvider.getArenaDP().getMultiTeamsIndexes()[vInfo.team]
            squadIconTemplate = '%s%d'
            if guiProps.name() == 'squadman':
                squadTeam = 'my'
            elif isAlly:
                squadTeam = 'ally'
            else:
                squadTeam = 'enemy'
            squadIcon = squadIconTemplate % (squadTeam, teamIdx)
        self.invokeMarker(markerID, 'init', [vType.classTag,
         vType.iconPath,
         vehShortName,
         vType.level,
         fullName,
         pName,
         clanAbbrev,
         regionCode,
         vProxy.health,
         maxHealth,
         guiProps.name(),
         speaking,
         hunting,
         guiProps.base,
         g_ctfManager.isFlagBearer(vInfo.vehicleID),
         squadIcon])
        return markerID

    def removeVehicleMarker(self, vehicleID):
        marker = self.__markers.pop(vehicleID, None)
        if marker is not None:
            self.__ownUI.delMarker(marker.id)
            marker.destroy()
        return

    def createStaticMarker(self, pos, symbol):
        mProv = Matrix()
        mProv.translation = pos
        handle = self.__ownUI.addMarker(mProv, symbol)
        return (mProv, handle)

    def destroyStaticMarker(self, handle):
        if self.__ownUI:
            self.__ownUI.delMarker(handle)

    def updateMarkerState(self, handle, newState, isImmediate = False):
        self.invokeMarker(handle, 'updateState', [newState, isImmediate])

    def showActionMarker(self, handle, newState):
        self.invokeMarker(handle, 'showActionMarker', [newState])

    def updateFlagbearerState(self, vehID, newState):
        marker = self.__markers.get(vehID)
        if marker is not None:
            self.invokeMarker(marker.id, 'updateFlagbearerState', [newState])
        return

    def updateVehicleHealth(self, handle, newHealth, aInfo, attackReasonID):
        if newHealth < 0 and not constants.SPECIAL_VEHICLE_HEALTH.IS_AMMO_BAY_DESTROYED(newHealth):
            newHealth = 0
        self.invokeMarker(handle, 'updateHealth', [newHealth, self.__getVehicleDamageType(aInfo), constants.ATTACK_REASONS[attackReasonID]])

    def showDynamic(self, vID, flag):
        if vID not in self.__markers:
            return
        marker = self.__markers[vID]
        self.invokeMarker(marker.id, 'setSpeaking', [flag])

    def updateMarkersScale(self, scale = None):
        if self.__ownUIProxy() is not None:
            if scale is None:
                self.__ownUIProxy().markerSetScale(g_settingsCore.interfaceScale.get())
            else:
                self.__ownUIProxy().markerSetScale(scale)
        return

    def setTeamKiller(self, vID):
        if vID not in self.__markers:
            return
        marker = self.__markers[vID]
        ctx = g_sessionProvider.getCtx()
        if not ctx.isTeamKiller(vID=vID) or ctx.isSquadMan(vID=vID) and not arena_info.isEventBattle():
            return
        self.invokeMarker(marker.id, 'setEntityName', [PLAYER_GUI_PROPS.teamKiller.name()])

    def invokeMarker(self, handle, function, args = None):
        if handle != -1:
            self.__ownUI.markerInvoke(handle, (function, args))

    def setMarkerSettings(self, settings):
        if self.__markersCanvasUI:
            self.__markersCanvasUI.setMarkerSettings(settings)

    def setMarkerDuration(self, value):
        self.__invokeCanvas('setMarkerDuration', [value])

    def updateMarkers(self):
        self.colorManager.update()
        for marker in self.__markers.itervalues():
            self.invokeMarker(marker.id, 'update')

        self.__plugins.update()

    def updateMarkerSettings(self):
        for marker in self.__markers.itervalues():
            self.invokeMarker(marker.id, 'updateMarkerSettings')

    def __invokeCanvas(self, function, args = None):
        if args is None:
            args = []
        self.call('battle.vehicleMarkersCanvas.' + function, args)
        return

    def __getVehicleDamageType(self, attackerInfo):
        if not attackerInfo:
            return _DAMAGE_TYPE.FROM_UNKNOWN
        attackerID = attackerInfo.vehicleID
        if attackerID == avatar_getter.getPlayerVehicleID():
            return _DAMAGE_TYPE.FROM_PLAYER
        entityName = g_sessionProvider.getCtx().getPlayerGuiProps(attackerID, attackerInfo.team)
        if entityName == PLAYER_GUI_PROPS.squadman:
            return _DAMAGE_TYPE.FROM_SQUAD
        if entityName == PLAYER_GUI_PROPS.ally:
            return _DAMAGE_TYPE.FROM_ALLY
        if entityName == PLAYER_GUI_PROPS.enemy:
            return _DAMAGE_TYPE.FROM_ENEMY
        return _DAMAGE_TYPE.FROM_UNKNOWN

    def __onVehicleMarkerAdded(self, vProxy, vInfo, guiProps):
        self.addVehicleMarker(vProxy, vInfo, guiProps)

    def __onVehicleMarkerRemoved(self, vehicleID):
        self.removeVehicleMarker(vehicleID)

    def __onVehicleFeedbackReceived(self, eventID, vehicleID, value):
        if vehicleID not in self.__markers:
            return
        marker = self.__markers[vehicleID]
        if eventID == _EVENT_ID.VEHICLE_HIT:
            self.updateMarkerState(marker.id, 'hit', value)
        elif eventID == _EVENT_ID.VEHICLE_ARMOR_PIERCED:
            self.updateMarkerState(marker.id, 'hit_pierced', value)
        elif eventID == _EVENT_ID.VEHICLE_DEAD:
            self.updateMarkerState(marker.id, 'dead', value)
        elif eventID == _EVENT_ID.VEHICLE_SHOW_MARKER:
            self.showActionMarker(marker.id, value)
        elif eventID == _EVENT_ID.VEHICLE_HEALTH:
            self.updateVehicleHealth(marker.id, *value)

    def __handleShowExtendedInfo(self, event):
        isDown = event.ctx['isDown']
        self.__invokeCanvas('setShowExInfoFlag', [isDown])
        for marker in self.__markers.itervalues():
            self.invokeMarker(marker.id, 'showExInfo', [isDown])

    def __handleGUIVisibility(self, event):
        self.active(event.ctx['visible'])


class _VehicleMarker(object):

    def __init__(self, markerID, vProxy, uiProxy):
        self.id = markerID
        self.vProxy = vProxy
        self.uiProxy = uiProxy
        self.vProxy.appearance.onModelChanged += self.__onModelChanged

    def destroy(self):
        self.vProxy.appearance.onModelChanged -= self.__onModelChanged
        self.vProxy = None
        self.uiProxy = None
        self.markerID = -1
        return

    def __onModelChanged(self):
        if self.uiProxy() is not None:
            self.uiProxy().markerSetMatrix(self.id, self.vProxy.model.node('HP_gui'))
        return


class _EquipmentsMarkerPlugin(IPlugin):

    def __init__(self, parentObj):
        super(_EquipmentsMarkerPlugin, self).__init__(parentObj)
        self.__markers = {}

    def init(self):
        super(_EquipmentsMarkerPlugin, self).init()
        ctrl = g_sessionProvider.getEquipmentsCtrl()
        if ctrl:
            ctrl.onEquipmentMarkerShown += self.__onShown

    def fini(self):
        ctrl = g_sessionProvider.getEquipmentsCtrl()
        if ctrl:
            ctrl.onEquipmentMarkerShown -= self.__onShown
        super(_EquipmentsMarkerPlugin, self).fini()

    def start(self):
        super(_EquipmentsMarkerPlugin, self).start()

    def stop(self):
        for handle, callbackID in self.__markers.items():
            self._parentObj.destroyStaticMarker(handle)
            if callbackID is not None:
                BigWorld.cancelCallback(callbackID)

        self.__markers = None
        super(_EquipmentsMarkerPlugin, self).stop()
        return

    def __onShown(self, item, pos, dir, time):
        _, handle = self._parentObj.createStaticMarker(pos + _MARKER_POSITION_ADJUSTMENT, _EQUIPMENT_MARKER_TYPE)
        defaultPostfix = i18n.makeString(INGAME_GUI.FORTCONSUMABLES_TIMER_POSTFIX)
        self._parentObj.invokeMarker(handle, 'init', [item.getMarker(), str(int(time)), defaultPostfix])
        self.__initTimer(int(math.ceil(time)), handle)

    def __initTimer(self, timer, handle):
        timer -= 1
        if timer < 0:
            self._parentObj.destroyStaticMarker(handle)
            if handle in self.__markers:
                del self.__markers[handle]
            return
        self._parentObj.invokeMarker(handle, 'updateTimer', [str(timer)])
        callbackId = BigWorld.callback(1, partial(self.__initTimer, timer, handle))
        self.__markers[handle] = callbackId


class _FlagsMarkerPlugin(IPlugin):

    def __init__(self, parentObj):
        super(_FlagsMarkerPlugin, self).__init__(parentObj)
        self.__markers = {}
        self.__capturePoints = []
        self.__spawnPoints = []
        self.__captureMarkers = []
        self.__playerTeam = 0
        self.__isTeamPlayer = False

    def init(self):
        super(_FlagsMarkerPlugin, self).init()
        g_ctfManager.onFlagSpawning += self.__onFlagSpawning
        g_ctfManager.onFlagSpawnedAtBase += self.__onSpawnedAtBase
        g_ctfManager.onFlagCapturedByVehicle += self.__onCapturedByVehicle
        g_ctfManager.onFlagDroppedToGround += self.__onDroppedToGround
        g_ctfManager.onFlagAbsorbed += self.__onAbsorbed
        g_ctfManager.onFlagRemoved += self.__onRemoved

    def fini(self):
        g_ctfManager.onFlagSpawning -= self.__onFlagSpawning
        g_ctfManager.onFlagSpawnedAtBase -= self.__onSpawnedAtBase
        g_ctfManager.onFlagCapturedByVehicle -= self.__onCapturedByVehicle
        g_ctfManager.onFlagDroppedToGround -= self.__onDroppedToGround
        g_ctfManager.onFlagAbsorbed -= self.__onAbsorbed
        g_ctfManager.onFlagRemoved -= self.__onRemoved
        super(_FlagsMarkerPlugin, self).fini()

    def start(self):
        player = BigWorld.player()
        playerVehicleID = player.playerVehicleID
        arena = player.arena
        arenaType = arena.arenaType
        self.__playerTeam = player.team
        self.__isTeamPlayer = self.__playerTeam in arenaType.squadTeamNumbers if arena_info.getIsMultiteam(arenaType) else True
        self.__capturePoints = arenaType.flagAbsorptionPoints
        self.__spawnPoints = arenaType.flagSpawnPoints
        isFlagBearer = False
        for flagID, flagInfo in g_ctfManager.getFlags():
            vehicleID = flagInfo['vehicle']
            if vehicleID is None:
                flagState = flagInfo['state']
                if flagState == constants.FLAG_STATE.WAITING_FIRST_SPAWN:
                    self.__onFlagSpawning(flagID, flagInfo['respawnTime'])
                elif flagState in (constants.FLAG_STATE.ON_GROUND, constants.FLAG_STATE.ON_SPAWN):
                    self.__onSpawnedAtBase(flagID, flagInfo['team'], flagInfo['minimapPos'])
            elif vehicleID == playerVehicleID:
                isFlagBearer = True

        if isFlagBearer:
            self.__addCaptureMarkers()
        super(_FlagsMarkerPlugin, self).start()
        return

    def stop(self):
        for handle, callbackID in self.__markers.values():
            self._parentObj.destroyStaticMarker(handle)
            if callbackID is not None:
                BigWorld.cancelCallback(callbackID)

        self.__markers = None
        self.__delCaptureMarkers()
        self.__capturePoints = None
        self.__spawnPoints = None
        super(_FlagsMarkerPlugin, self).stop()
        return

    def __addFlagMarker(self, flagID, flagPos, marker):
        _, handle = self._parentObj.createStaticMarker(flagPos + _MARKER_POSITION_ADJUSTMENT, _FLAG_MARKER_TYPE)
        self._parentObj.invokeMarker(handle, 'setIcon', [marker])
        self.__markers[flagID] = (handle, None)
        return

    def __delFlagMarker(self, flagID):
        handle, callbackID = self.__markers.pop(flagID, (None, None))
        if handle is not None:
            self._parentObj.destroyStaticMarker(handle)
        if callbackID is not None:
            BigWorld.cancelCallback(callbackID)
        return

    def __initTimer(self, timer, flagID):
        timer -= 1
        handle, _ = self.__markers[flagID]
        if timer < 0:
            self.__markers[flagID] = (handle, None)
            return
        else:
            self._parentObj.invokeMarker(handle, 'setLabel', [i18n.makeString(INGAME_GUI.FLAGS_TIMER, time=str(timer))])
            callbackId = BigWorld.callback(1, partial(self.__initTimer, timer, flagID))
            self.__markers[flagID] = (handle, callbackId)
            return

    def __addCaptureMarkers(self):
        for point in self.__capturePoints:
            if self.__isTeamPlayer and point['team'] in (NEUTRAL_TEAM, self.__playerTeam):
                position = point['position']
                _, handle = self._parentObj.createStaticMarker(position + _MARKER_POSITION_ADJUSTMENT, _FLAG_CAPTURE_MARKER_TYPE)
                self.__captureMarkers.append((handle, None))

        return

    def __delCaptureMarkers(self):
        for handle, callbackID in self.__captureMarkers:
            self._parentObj.destroyStaticMarker(handle)
            if callbackID is not None:
                BigWorld.cancelCallback(callbackID)

        self.__captureMarkers = []
        return

    def __onFlagSpawning(self, flagID, respawnTime):
        flagType = _FLAG_TYPE.COOLDOWN
        flagPos = self.__spawnPoints[flagID]['position']
        self.__addFlagMarker(flagID, flagPos, flagType)
        timer = respawnTime - BigWorld.serverTime()
        self.__initTimer(int(math.ceil(timer)), flagID)

    def __onSpawnedAtBase(self, flagID, flagTeam, flagPos):
        flagType = self.__getFlagMarkerType(flagID, flagTeam)
        self.__delFlagMarker(flagID)
        self.__addFlagMarker(flagID, flagPos, flagType)

    def __onCapturedByVehicle(self, flagID, flagTeam, vehicleID):
        self._parentObj.updateFlagbearerState(vehicleID, True)
        self.__delFlagMarker(flagID)
        if vehicleID == BigWorld.player().playerVehicleID:
            self.__addCaptureMarkers()

    def __onDroppedToGround(self, flagID, flagTeam, loserVehicleID, flagPos, respawnTime):
        flagType = self.__getFlagMarkerType(flagID, flagTeam)
        self._parentObj.updateFlagbearerState(loserVehicleID, False)
        self.__addFlagMarker(flagID, flagPos, flagType)
        timer = respawnTime - BigWorld.serverTime()
        self.__initTimer(int(math.ceil(timer)), flagID)
        if loserVehicleID == BigWorld.player().playerVehicleID:
            self.__delCaptureMarkers()

    def __onAbsorbed(self, flagID, flagTeam, vehicleID, respawnTime):
        self._parentObj.updateFlagbearerState(vehicleID, False)
        self.__delFlagMarker(flagID)
        if vehicleID == BigWorld.player().playerVehicleID:
            self.__delCaptureMarkers()

    def __onRemoved(self, flagID, flagTeam, vehicleID):
        self.__delFlagMarker(flagID)
        if vehicleID is not None:
            self._parentObj.updateFlagbearerState(vehicleID, False)
            if vehicleID == BigWorld.player().playerVehicleID:
                self.__delCaptureMarkers()
        return

    def __getFlagMarkerType(self, flagID, flagTeam = 0):
        player = BigWorld.player()
        currentTeam = player.team
        if flagTeam > 0:
            if flagTeam == currentTeam:
                return _FLAG_TYPE.ALLY
            return _FLAG_TYPE.ENEMY
        return _FLAG_TYPE.NEUTRAL


class _RepairsMarkerPlugin(IPlugin):

    def __init__(self, parentObj):
        super(_RepairsMarkerPlugin, self).__init__(parentObj)
        self.__markers = {}

    def init(self):
        super(_RepairsMarkerPlugin, self).init()
        g_sessionProvider.getRepairCtrl().onRepairPointStateChanged += self.__onStateChanged

    def fini(self):
        g_sessionProvider.getRepairCtrl().onRepairPointStateChanged -= self.__onStateChanged
        super(_RepairsMarkerPlugin, self).fini()

    def start(self):
        player = BigWorld.player()
        arena = player.arena
        arenaType = arena.arenaType
        for pointID, point in enumerate(arenaType.repairPoints):
            repairPos = point['position']
            isActive = True
            callbackID = None
            _, handle = self._parentObj.createStaticMarker(repairPos + _MARKER_POSITION_ADJUSTMENT, _REPAIR_MARKER_TYPE)
            self._parentObj.invokeMarker(handle, 'setIcon', ['active' if isActive else 'cooldown'])
            self.__markers[pointID] = (handle,
             callbackID,
             repairPos,
             isActive)

        super(_RepairsMarkerPlugin, self).start()
        return

    def stop(self):
        for handle, callbackID, _, _ in self.__markers.values():
            self._parentObj.destroyStaticMarker(handle)
            if callbackID is not None:
                BigWorld.cancelCallback(callbackID)

        self.__markers = None
        super(_RepairsMarkerPlugin, self).stop()
        return

    def __initTimer(self, timer, repairID):
        timer -= 1
        handle, _, repairPos, wasActive = self.__markers[repairID]
        if timer < 0:
            self.__markers[repairID] = (handle,
             None,
             repairPos,
             wasActive)
            return
        else:
            self._parentObj.invokeMarker(handle, 'setLabel', [time_utils.getTimeLeftFormat(timer)])
            callbackId = BigWorld.callback(1, partial(self.__initTimer, timer, repairID))
            self.__markers[repairID] = (handle,
             callbackId,
             repairPos,
             wasActive)
            return

    def __onStateChanged(self, repairPointID, action, timeLeft = 0):
        if repairPointID not in self.__markers:
            LOG_ERROR('Got repair point state changed for not available repair point: ', repairPointID, action, timeLeft)
            return
        else:
            if action in (constants.REPAIR_POINT_ACTION.START_REPAIR, constants.REPAIR_POINT_ACTION.COMPLETE_REPAIR, constants.REPAIR_POINT_ACTION.BECOME_READY):
                handle, callbackID, repairPos, wasActive = self.__markers[repairPointID]
                isActive = action in (constants.REPAIR_POINT_ACTION.START_REPAIR, constants.REPAIR_POINT_ACTION.BECOME_READY)
                if wasActive == isActive:
                    return
                if callbackID is not None:
                    BigWorld.cancelCallback(callbackID)
                    callbackID = None
                self._parentObj.invokeMarker(handle, 'setIcon', ['active' if isActive else 'cooldown'])
                self._parentObj.invokeMarker(handle, 'setLabel', [''])
                self.__markers[repairPointID] = (handle,
                 callbackID,
                 repairPos,
                 isActive)
                if not isActive:
                    self.__initTimer(int(math.ceil(timeLeft)), repairPointID)
            elif action == constants.REPAIR_POINT_ACTION.BECOME_DISABLED:
                handle, callbackID, _, _ = self.__markers.pop(repairPointID)
                self._parentObj.destroyStaticMarker(handle)
                if callbackID is not None:
                    BigWorld.cancelCallback(callbackID)
            return


class _ResourceMarkerPlugin(IPlugin):

    def __init__(self, parentObj):
        super(_ResourceMarkerPlugin, self).__init__(parentObj)
        self.__markers = {}

    def init(self):
        super(_ResourceMarkerPlugin, self).init()
        g_ctfManager.onResPointIsFree += self.__onIsFree
        g_ctfManager.onResPointCooldown += self.__onCooldown
        g_ctfManager.onResPointCaptured += self.__onCaptured
        g_ctfManager.onResPointCapturedLocked += self.__onCapturedLocked
        g_ctfManager.onResPointBlocked += self.__onBlocked
        g_ctfManager.onResPointAmountChanged += self.__onAmountChanged

    def fini(self):
        g_ctfManager.onResPointIsFree -= self.__onIsFree
        g_ctfManager.onResPointCooldown -= self.__onCooldown
        g_ctfManager.onResPointCaptured -= self.__onCaptured
        g_ctfManager.onResPointCapturedLocked -= self.__onCapturedLocked
        g_ctfManager.onResPointBlocked -= self.__onBlocked
        g_ctfManager.onResPointAmountChanged -= self.__onAmountChanged
        super(_ResourceMarkerPlugin, self).fini()

    def start(self):
        super(_ResourceMarkerPlugin, self).start()
        arenaDP = g_sessionProvider.getArenaDP()
        for pointID, point in g_ctfManager.getResourcePoints():
            resourcePos = point['minimapPos']
            amount = point['amount']
            pointState = point['state']
            progress = float(amount) / point['totalAmount'] * 100
            if pointState == constants.RESOURCE_POINT_STATE.FREE:
                state = _RESOURCE_STATE.READY
            elif pointState == constants.RESOURCE_POINT_STATE.COOLDOWN:
                state = _RESOURCE_STATE.COOLDOWN
            elif pointState == constants.RESOURCE_POINT_STATE.CAPTURED:
                state = _CAPTURE_STATE_BY_TEAMS[arenaDP.isAllyTeam(point['team'])]
            elif pointState == constants.RESOURCE_POINT_STATE.CAPTURED_LOCKED:
                state = _CAPTURE_FROZEN_STATE_BY_TEAMS[arenaDP.isAllyTeam(point['team'])]
            elif pointState == constants.RESOURCE_POINT_STATE.BLOCKED:
                state = _RESOURCE_STATE.CONFLICT
            else:
                state = _RESOURCE_STATE.FREEZE
            _, handle = self._parentObj.createStaticMarker(resourcePos + _MARKER_POSITION_ADJUSTMENT, _RESOURCE_MARKER_TYPE)
            self._parentObj.invokeMarker(handle, 'as_init', [pointID, state, progress])
            self.__markers[pointID] = (handle,
             None,
             resourcePos,
             state)

        return

    def stop(self):
        for handle, callbackID, _, _ in self.__markers.values():
            self._parentObj.destroyStaticMarker(handle)
            if callbackID is not None:
                BigWorld.cancelCallback(callbackID)

        self.__markers = None
        super(_ResourceMarkerPlugin, self).stop()
        return

    def update(self):
        super(_ResourceMarkerPlugin, self).update()
        for point in self.__markers.itervalues():
            handle = point[0]
            self._parentObj.invokeMarker(handle, 'as_onSettingsChanged')

    def __onIsFree(self, pointID):
        handle, _, _, _ = self.__markers[pointID]
        self._parentObj.invokeMarker(handle, 'as_setState', [_RESOURCE_STATE.READY])

    def __onCooldown(self, pointID, serverTime):
        handle, _, _, _ = self.__markers[pointID]
        self._parentObj.invokeMarker(handle, 'as_setState', [_RESOURCE_STATE.COOLDOWN])

    def __onCaptured(self, pointID, team):
        handle, _, _, _ = self.__markers[pointID]
        state = _CAPTURE_STATE_BY_TEAMS[g_sessionProvider.getArenaDP().isAllyTeam(team)]
        self._parentObj.invokeMarker(handle, 'as_setState', [state])

    def __onCapturedLocked(self, pointID, team):
        handle, _, _, _ = self.__markers[pointID]
        state = _CAPTURE_FROZEN_STATE_BY_TEAMS[g_sessionProvider.getArenaDP().isAllyTeam(team)]
        self._parentObj.invokeMarker(handle, 'as_setState', [state])

    def __onBlocked(self, pointID):
        handle, _, _, _ = self.__markers[pointID]
        self._parentObj.invokeMarker(handle, 'as_setState', [_RESOURCE_STATE.CONFLICT])

    def __onAmountChanged(self, pointID, amount, totalAmount):
        progress = float(amount) / totalAmount * 100
        handle, _, _, _ = self.__markers[pointID]
        self._parentObj.invokeMarker(handle, 'as_setProgress', [progress])


class _GasAttackSafeZonePlugin(IPlugin):

    def __init__(self, parentObj):
        super(_GasAttackSafeZonePlugin, self).__init__(parentObj)
        self.__safeZoneMarkerHandle = None
        self.__isMarkerVisible = False
        self.__settings = BigWorld.player().arena.arenaType.gasAttackSettings
        return

    def init(self):
        super(_GasAttackSafeZonePlugin, self).init()
        g_sessionProvider.getGasAttackCtrl().onUpdated += self.__onGasAttackUpdate
        self.__initMarker(self.__settings.position)

    def fini(self):
        g_sessionProvider.getGasAttackCtrl().onUpdated -= self.__onGasAttackUpdate
        super(_GasAttackSafeZonePlugin, self).fini()

    def start(self):
        super(_GasAttackSafeZonePlugin, self).start()

    def stop(self):
        self.__delSafeZoneMarker()
        super(_GasAttackSafeZonePlugin, self).stop()

    def __updateSafeZoneMarker(self, isVisible):
        if not self.__isMarkerVisible == isVisible:
            self.__isMarkerVisible = isVisible
            self._parentObj.invokeMarker(self.__safeZoneMarkerHandle, 'update', [self.__isMarkerVisible])

    def __initMarker(self, center):
        if self.__safeZoneMarkerHandle is None:
            _, self.__safeZoneMarkerHandle = self._parentObj.createStaticMarker(center + _MARKER_POSITION_ADJUSTMENT, _SAFE_ZONE_MARKER_TYPE)
        return

    def __delSafeZoneMarker(self):
        if self.__safeZoneMarkerHandle is not None:
            self._parentObj.destroyStaticMarker(self.__safeZoneMarkerHandle)
            self.__safeZoneMarkerHandle = None
        return

    def __onGasAttackUpdate(self, state):
        isVisible = not state.state == GAS_ATTACK_STATE.INSIDE_SAFE_ZONE
        self.__updateSafeZoneMarker(isVisible)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\battle\markers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:53:11 St�edn� Evropa (b�n� �as)

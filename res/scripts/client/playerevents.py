# 2015.11.18 11:51:05 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/PlayerEvents.py
import Event
from constants import ARENA_PERIOD
from debug_utils import *

class DeprecatedEvent(Event.Event):

    def __iadd__(self, delegate):
        LOG_WARNING('Event deprecated')
        self._Event__delegates.add(delegate)
        return self


class _PlayerEvents(object):

    def __init__(self):
        self.onPlayerEntityChanging = Event.Event()
        self.onPlayerEntityChangeCanceled = Event.Event()
        self.isPlayerEntityChanging = True
        self.onAccountBecomePlayer = Event.Event()
        self.onAccountBecomeNonPlayer = Event.Event()
        self.onAccountShowGUI = Event.Event()
        self.onClientUpdated = Event.Event()
        self.onEnqueuedRandom = Event.Event()
        self.onDequeuedRandom = Event.Event()
        self.onEnqueueRandomFailure = Event.Event()
        self.onTutorialEnqueued = Event.Event()
        self.onTutorialDequeued = Event.Event()
        self.onTutorialEnqueueFailure = Event.Event()
        self.onEnqueuedUnitAssembler = Event.Event()
        self.onDequeuedUnitAssembler = Event.Event()
        self.onEnqueueUnitAssemblerFailure = Event.Event()
        self.onEnqueuedEventBattles = Event.Event()
        self.onDequeuedEventBattles = Event.Event()
        self.onEnqueueEventBattlesFailure = Event.Event()
        self.onEnqueuedSandbox = Event.Event()
        self.onDequeuedSandbox = Event.Event()
        self.onEnqueuedSandboxFailure = Event.Event()
        self.onPrebattleJoined = Event.Event()
        self.onPrebattleLeft = Event.Event()
        self.onPrebattleJoinFailure = Event.Event()
        self.onArenaCreated = Event.Event()
        self.onArenaJoinFailure = Event.Event()
        self.onKickedFromRandomQueue = Event.Event()
        self.onKickedFromTutorialQueue = Event.Event()
        self.onKickedFromUnitAssembler = Event.Event()
        self.onKickedFromEventBattles = Event.Event()
        self.onKickedFromSandboxQueue = Event.Event()
        self.onKickedFromPrebattle = Event.Event()
        self.onKickedFromArena = Event.Event()
        self.onQueueInfoReceived = Event.Event()
        self.onPrebattlesListReceived = Event.Event()
        self.onPrebattleAutoInvitesChanged = Event.Event()
        self.onAccountGlobalRatingChanged = Event.Event()
        self.onPrebattleInvitesChanged = Event.Event()
        self.onPrebattleInvitationsChanged = Event.Event()
        self.onPrebattleInvitesStatus = Event.Event()
        self.onClanMembersListChanged = Event.Event()
        self.onEventsDataChanged = Event.Event()
        self.onPrebattleRosterReceived = Event.Event()
        self.onArenaListReceived = Event.Event()
        self.onServerStatsReceived = Event.Event()
        self.onInventoryResync = Event.Event()
        self.onStatsResync = Event.Event()
        self.onShopResyncStarted = Event.Event()
        self.onShopResync = Event.Event()
        self.onDossiersResync = Event.Event()
        self.onOffersResync = Event.Event()
        self.onEventNotificationsChanged = Event.Event()
        self.onVehicleLockChanged = Event.Event()
        self.onVehicleBecomeElite = Event.Event()
        self.onCenterIsLongDisconnected = Event.Event()
        self.onIGRTypeChanged = Event.Event()
        self.onAvatarBecomePlayer = Event.Event()
        self.onAvatarBecomeNonPlayer = Event.Event()
        self.onArenaPeriodChange = Event.Event()
        self.onAvatarReady = Event.Event()
        self.onBattleResultsReceived = Event.Event()
        self.onLoginQueueNumberReceived = Event.Event()
        self.onKickWhileLoginReceived = Event.Event()
        self.onGuiCacheSyncCompleted = Event.Event()
        self.onPQLocksChanged = Event.Event()


g_playerEvents = _PlayerEvents()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\playerevents.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:51:05 St�edn� Evropa (b�n� �as)

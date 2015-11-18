# 2015.11.18 11:56:14 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/server_events/__init__.py
import BigWorld
from debug_utils import LOG_DEBUG
from gui.server_events.EventsCache import g_eventsCache

def isPotapovQuestEnabled():
    try:
        return BigWorld.player().serverSettings['isPotapovQuestEnabled']
    except Exception:
        LOG_DEBUG('There is problem while getting potapov quests supporting flag.Availability value is default')
        return False
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\server_events\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:56:14 Støední Evropa (bìžný èas)

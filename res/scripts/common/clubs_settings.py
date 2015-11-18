# 2015.11.18 11:58:53 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/clubs_settings.py
import ResMgr
from debug_utils import LOG_ERROR, LOG_DEBUG
_CONFIG_FILE = 'scripts/item_defs/clubs_settings.xml'

class ClubsSettings:
    prearenaWaitTime = property(lambda self: self.__prearenaWaitTime)
    maxLegionariesCount = property(lambda self: self.__maxLegionariesCount)

    def __init__(self, prearenaWaitTime, maxLegionariesCount):
        self.__prearenaWaitTime = prearenaWaitTime
        self.__maxLegionariesCount = maxLegionariesCount

    @classmethod
    def default(cls):
        return cls(180, 6)


g_cache = None

def init():
    global g_cache
    LOG_DEBUG('clubs.init()')
    try:
        section = ResMgr.openSection(_CONFIG_FILE)
        prearenaWaitTime = section['prearena_wait_time'].asInt
        maxLegionariesCount = section['max_legionaries_count'].asInt
        g_cache = ClubsSettings(prearenaWaitTime, maxLegionariesCount)
    except Exception as e:
        LOG_ERROR('Wrong config :{}. Error: {}'.format(_CONFIG_FILE, repr(e)))
        g_cache = ClubsSettings.default()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\clubs_settings.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:58:53 St�edn� Evropa (b�n� �as)

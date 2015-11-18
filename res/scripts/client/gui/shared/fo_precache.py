# 2015.11.18 11:56:16 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/shared/fo_precache.py
import BigWorld
from debug_utils import LOG_ERROR, LOG_DEBUG
_IS_ENABLED = True
if _IS_ENABLED:

    def add(path, forced = False):
        result = True
        try:
            result = BigWorld.wg_precacheScaleformResource(path, forced)
            if result:
                LOG_DEBUG('Resource is added to precache', path)
        except AttributeError:
            LOG_ERROR('BigWorld package does not include function wg_precacheScaleformResource')

        return result


    def clear(path = ''):
        try:
            BigWorld.wg_eraseScaleformResFromCache(path)
            LOG_DEBUG('Resource(s) is(are) cleared from precache', path)
        except AttributeError:
            LOG_ERROR('BigWorld package does not include function wg_eraseScaleformResFromCache')


else:

    def add(path, forced = False):
        return True


    def clear(path = ''):
        pass
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\fo_precache.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:56:16 Støední Evropa (bìžný èas)

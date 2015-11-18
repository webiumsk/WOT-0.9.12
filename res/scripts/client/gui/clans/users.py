# 2015.11.18 11:52:09 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/clans/users.py
from adisp import async, process
import weakref
from gui.clans.contexts import AccountClanRatingsCtx

class UserCache(object):

    def __init__(self, clanCtrl):
        super(UserCache, self).__init__()
        self.__cache = dict()
        self.__clanCtrl = weakref.proxy(clanCtrl)

    @async
    @process
    def requestUsers(self, dbIDs, callback):
        status = True
        missingUser = [ usrID for usrID in dbIDs if usrID not in self.__cache ]
        if len(missingUser):
            usrCtx = AccountClanRatingsCtx(missingUser)
            result = yield self.__clanCtrl.sendRequest(usrCtx, allowDelay=True)
            if result.isSuccess():
                ratingsData = usrCtx.getDataObj(result.data)
                for key, item in ratingsData.iteritems():
                    self.__cache[key] = item

            else:
                status = False
        users = dict(((usrID, self.__cache[usrID]) for usrID in dbIDs if usrID in self.__cache))
        callback((status, users))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\clans\users.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:09 Støední Evropa (bìžný èas)

# 2015.11.18 11:59:47 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/bwobsolete_helpers/Region.py
import BigWorld
import FantasyDemo

class Region:

    def __init__(self):
        self.currentSpace = ''
        self.currentRegion = None
        self.currentDesc = ''
        self.listeners = []
        FantasyDemo.addChangeEnvironmentsListener(self.onChangeEnvironments)
        return

    def fini(self):
        FantasyDemo.delChangeEnvironmentsListener(self.onChangeEnvironments)

    def addListener(self, l):
        self.listeners.append(l)
        l.onEnterRegion(self.describeCurrent())

    def delListener(self, l):
        try:
            self.listeners.remove(l)
        except ValueError:
            pass

    def describeCurrent(self):
        if self.currentRegion != None:
            return self.currentRegion
        else:
            return self.currentSpace
            return

    def onChangeEnvironments(self, inside):
        player = BigWorld.player()
        if player != None:
            spaceID = player.spaceID
            try:
                self.currentSpace = self.fancify(FantasyDemo.rds.spaceNameMap[spaceID])
            except KeyError:
                self.currentSpace = ''

            self.checkForChanges()
        return

    def fancify(self, name):
        name = name.split('spaces/')[-1]
        name = name.replace('_', ' ')
        name = name.title()
        return name

    def onEnterRegion(self, description):
        if self.currentRegion != description:
            self.currentRegion = description
            self.checkForChanges()

    def onLeaveRegion(self, description):
        if self.currentRegion == description:
            self.currentRegion = None
            self.checkForChanges()
        return

    def checkForChanges(self):
        desc = self.describeCurrent()
        if self.currentDesc != desc:
            self.currentDesc = desc
            for l in self.listeners:
                l.onEnterRegion(desc)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\bwobsolete_helpers\region.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:47 St�edn� Evropa (b�n� �as)

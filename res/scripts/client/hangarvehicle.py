# 2015.11.18 11:51:02 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/HangarVehicle.py
import BigWorld
import Math
from ModelHitTester import segmentMayHitVehicle, SegmentCollisionResult

class HangarVehicle(BigWorld.Entity):

    def __init__(self):
        self.typeDescriptor = None
        return

    def prerequisites(self):
        return []

    def onEnterWorld(self, prereqs):
        pass

    def onLeaveWorld(self):
        pass

    def collideSegment(self, startPoint, endPoint, skipGun = False):
        worldToVehMatrix = Math.Matrix(self.model.matrix)
        worldToVehMatrix.invert()
        startPoint = worldToVehMatrix.applyPoint(startPoint)
        endPoint = worldToVehMatrix.applyPoint(endPoint)
        res = None
        for compDescr, compMatrix in self.getComponents():
            if skipGun and compDescr.get('itemTypeName') == 'vehicleGun':
                continue
            hitTester = compDescr['hitTester']
            if not hitTester.isBspModelLoaded():
                hitTester.loadBspModel()
            collisions = hitTester.localHitTest(compMatrix.applyPoint(startPoint), compMatrix.applyPoint(endPoint))
            if collisions is None:
                continue
            for dist, _, hitAngleCos, matKind in collisions:
                if res is None or res[0] >= dist:
                    matInfo = compDescr['materials'].get(matKind)
                    res = SegmentCollisionResult(dist, hitAngleCos, matInfo.armor if matInfo is not None else 0)

        return res

    def segmentMayHitVehicle(self, startPoint, endPoint):
        return segmentMayHitVehicle(self.typeDescriptor, startPoint, endPoint, self.position)

    def getComponents(self):
        res = []
        vehicleDescr = self.typeDescriptor
        m = Math.Matrix()
        m.setIdentity()
        res.append((vehicleDescr.chassis, m))
        hullOffset = vehicleDescr.chassis['hullPosition']
        m = Math.Matrix()
        offset = -hullOffset
        m.setTranslate(offset)
        res.append((vehicleDescr.hull, m))
        m = Math.Matrix()
        offset -= vehicleDescr.hull['turretPositions'][0]
        m.setTranslate(offset)
        res.append((vehicleDescr.turret, m))
        m = Math.Matrix()
        offset -= vehicleDescr.turret['gunPosition']
        m.setTranslate(offset)
        res.append((vehicleDescr.gun, m))
        return res
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\hangarvehicle.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:51:03 Støední Evropa (bìžný èas)

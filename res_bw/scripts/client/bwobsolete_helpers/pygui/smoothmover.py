# 2015.11.18 11:59:54 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/SmoothMover.py
import BigWorld, GUI, Math, Keys
from PyGUIBase import PyGUIBase

class SmoothMover(PyGUIBase):
    factoryString = 'PyGUI.SmoothMover'

    def __init__(self, component):
        PyGUIBase.__init__(self, component)
        self.minScroll = [0, 0]
        self.maxScroll = [0, 0]
        self.scroll = [0, 0]
        self.scrollSpeed = 0.5
        self.scrollTransform = Math.Matrix()
        self.scrollTransform.setIdentity()

    def scrollTo(self, x, y, animate = True):
        self.scroll[0] = max(x, self.minScroll[0])
        self.scroll[0] = min(self.scroll[0], self.maxScroll[0])
        self.scroll[1] = max(y, self.minScroll[1])
        self.scroll[1] = min(self.scroll[1], self.maxScroll[1])
        self.scrollTransform.setTranslate((self.scroll[0], self.scroll[1], 0))
        self.component.transform.target = self.scrollTransform
        self.component.transform.eta = self.scrollSpeed if animate else 0.0

    def scrollBy(self, x, y):
        self.scrollTo(self.scroll[0] + x, self.scroll[1] + y)

    def canScrollUp(self):
        return self.scroll[1] > self.minScroll[1] + 0.0001

    def canScrollDown(self):
        return self.scroll[1] < self.maxScroll[1] - 0.0001

    def canScrollLeft(self):
        return self.scroll[0] > self.minScroll[0] + 0.0001

    def canScrollRight(self):
        return self.scroll[0] < self.maxScroll[0] - 0.0001
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\bwobsolete_helpers\pygui\smoothmover.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:54 Støední Evropa (bìžný èas)

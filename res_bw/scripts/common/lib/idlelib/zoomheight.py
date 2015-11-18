# 2015.11.18 12:04:17 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/idlelib/ZoomHeight.py
import re
import sys
from idlelib import macosxSupport

class ZoomHeight:
    menudefs = [('windows', [('_Zoom Height', '<<zoom-height>>')])]

    def __init__(self, editwin):
        self.editwin = editwin

    def zoom_height_event(self, event):
        top = self.editwin.top
        zoom_height(top)


def zoom_height(top):
    geom = top.wm_geometry()
    m = re.match('(\\d+)x(\\d+)\\+(-?\\d+)\\+(-?\\d+)', geom)
    if not m:
        top.bell()
        return
    width, height, x, y = map(int, m.groups())
    newheight = top.winfo_screenheight()
    if sys.platform == 'win32':
        newy = 0
        newheight = newheight - 72
    elif macosxSupport.isAquaTk():
        newy = 22
        newheight = newheight - newy - 88
    else:
        newy = 0
        newheight = newheight - 88
    if height >= newheight:
        newgeom = ''
    else:
        newgeom = '%dx%d+%d+%d' % (width,
         newheight,
         x,
         newy)
    top.wm_geometry(newgeom)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\idlelib\zoomheight.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:04:17 Støední Evropa (bìžný èas)

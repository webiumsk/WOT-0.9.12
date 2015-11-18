# 2015.11.18 11:52:18 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/doc_loaders/GuiDirReader.py
import ResMgr

class GuiDirReader(object):
    SCALEFORM_STARTUP_VIDEO_PATH = 'gui/flash/video'
    SCALEFORM_STARTUP_VIDEO_MASK = 'video/%s'
    VIDEO_EXTENSION = 'usm'

    def __init__(self):
        super(GuiDirReader, self).__init__()

    @staticmethod
    def getAvailableIntroVideoFiles():
        ds = ResMgr.openSection(GuiDirReader.SCALEFORM_STARTUP_VIDEO_PATH)
        movieFiles = []
        for filename in ds.keys():
            basename, extension = filename.split('.')
            if extension == GuiDirReader.VIDEO_EXTENSION and basename[0:1] != '_':
                movieFiles.append(GuiDirReader.SCALEFORM_STARTUP_VIDEO_MASK % filename)

        ResMgr.purge(GuiDirReader.SCALEFORM_STARTUP_VIDEO_PATH, True)
        return movieFiles
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\doc_loaders\guidirreader.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:18 Støední Evropa (bìžný èas)

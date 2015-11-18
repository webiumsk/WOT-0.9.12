# 2015.11.18 11:51:03 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/LcdKeyboard.py
import BigWorld
_g_instance = None

class LCD_KEY:
    LEFT = 256
    RIGHT = 512
    OK = 1024
    CANCEL = 2048
    UP = 4096
    DOWN = 8192
    MENU = 16384


def enableLcdKeyboardSpecificKeys(bValue):
    global _g_instance
    if bValue:
        if _g_instance is not None:
            return True
        _g_instance = BigWorld.WGLcdKeyboard()
        if not _g_instance.isValid():
            _g_instance.destroy()
            _g_instance = None
            return False
    else:
        if _g_instance is None:
            return True
        _g_instance.destroy()
        _g_instance = None
    return True


def getKeys(mask = 4294967295L):
    if _g_instance is None:
        return 0
    else:
        return _g_instance.getKeys() & mask


def finalize():
    enableLcdKeyboardSpecificKeys(False)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\lcdkeyboard.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:51:03 Støední Evropa (bìžný èas)

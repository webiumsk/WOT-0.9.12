# 2015.11.18 11:59:54 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/TextStyles.py
import BigWorld, GUI, Math, ResMgr
from bwdebug import ERROR_MSG
styles = {'Heading': ('Heading.font', (255, 255, 255, 255)),
 'Label': ('Label.font', (255, 255, 255, 255)),
 'ButtonNormal': ('Heading.font', (255, 255, 255, 200)),
 'ButtonHover': ('Heading.font', (255, 255, 255, 255)),
 'ButtonPressed': ('Heading.font', (255, 255, 255, 255)),
 'ButtonActive': ('Heading.font', (0, 0, 0, 255)),
 'ButtonDisabled': ('Heading.font', (128, 128, 128, 255))}
fontAliases = {}

def setStyle(component, styleName):
    if styles.has_key(styleName):
        style = styles[styleName]
        component.font = fontAliases.get(style[0], style[0])
        component.colour = style[1]
    else:
        ERROR_MSG("No style named '%s'." % (styleName,))
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\bwobsolete_helpers\pygui\textstyles.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:54 St�edn� Evropa (b�n� �as)

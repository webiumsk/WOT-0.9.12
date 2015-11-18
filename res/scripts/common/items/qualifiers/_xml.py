# 2015.11.18 11:59:42 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/items/qualifiers/_xml.py
import expressions

def parseCondition(section):
    if not section.has_key('condition'):
        return (None, None)
    else:
        return expressions.parseExpression(section['condition'].asString)


def parseValue(section):
    if not section.has_key('value'):
        return (None, None)
    else:
        x = section['value'].asString.strip(' ')
        if x.endswith('%'):
            res = (True, int(x[:-1]))
        else:
            res = (False, int(x))
        return res
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\items\qualifiers\_xml.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:42 Støední Evropa (bìžný èas)

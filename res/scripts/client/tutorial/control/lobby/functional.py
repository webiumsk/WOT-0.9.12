# 2015.11.18 11:58:22 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/tutorial/control/lobby/functional.py
from tutorial.control.functional import FunctionalEffect, FunctionalConditions, FunctionalChapterInfo
from tutorial.logger import LOG_ERROR

class FunctionalShowHintEffect(FunctionalEffect):

    def triggerEffect(self):
        hint = self.getTarget()
        if hint is not None:
            self._gui.playEffect('ShowHint', hint.getData(), itemRef=hint.getTargetID(), containerRef=hint.getContainerID())
        else:
            LOG_ERROR('Hint not found', self._effect.getTargetID())
        return


class FunctionalCloseHintEffect(FunctionalEffect):

    def triggerEffect(self):
        self._gui.stopEffect('ShowHint', self._effect.getTargetID())


class FunctionalLobbyChapterInfo(FunctionalChapterInfo):

    def __init__(self):
        super(FunctionalChapterInfo, self).__init__()
        chapter = self._data
        chapterID = chapter.getID()
        self._conditions = None
        conditions = chapter.getHasIDEntity(chapterID)
        if conditions is not None and len(conditions):
            self._conditions = FunctionalConditions(conditions)
        self._isShow = False
        return

    def invalidate(self):
        if self._conditions is None:
            return
        else:
            ok = self._conditions.allConditionsOk()
            if ok and not self._isShow:
                chapter = self._data
                self._gui.setChapterInfo(chapter.getTitle(), chapter.getDescription(afterBattle=self._cache.isAfterBattle()))
                self._isShow = True
            elif not ok and self._isShow:
                self._gui.clearChapterInfo()
                self._isShow = False
            return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\tutorial\control\lobby\functional.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:58:22 Støední Evropa (bìžný èas)

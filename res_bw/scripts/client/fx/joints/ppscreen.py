# 2015.11.18 12:00:05 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/FX/Joints/PPScreen.py
from FX import s_sectionProcessors
from FX import typeCheck
from FX.Joint import Joint
from bwdebug import *
import BigWorld
import PostProcessing

class PPScreen(Joint):
    """
    This class implements a Joint that attaches a PostProcessing chain to the 
    screen.
    
    The actor must be a PPChain.
    """

    def load(self, pSection, prereqs = None):
        return self

    def attach(self, actor, source, target = None):
        ch = PostProcessing.chain()
        ch += actor
        PostProcessing.chain(ch)

    def detach(self, actor, source, target = None):
        ch = PostProcessing.chain()
        for effect in actor:
            try:
                ch.remove(effect)
            except ValueError:
                pass

        PostProcessing.chain(ch)


s_sectionProcessors['PPScreen'] = PPScreen
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\fx\joints\ppscreen.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:00:05 Støední Evropa (bìžný èas)

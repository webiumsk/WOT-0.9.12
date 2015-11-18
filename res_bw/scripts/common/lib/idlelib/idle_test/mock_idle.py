# 2015.11.18 12:04:17 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/idlelib/idle_test/mock_idle.py
"""Mock classes that imitate idlelib modules or classes.

Attributes and methods will be added as needed for tests.
"""
from idlelib.idle_test.mock_tk import Text

class Editor(object):
    """Minimally imitate EditorWindow.EditorWindow class.
    """

    def __init__(self, flist = None, filename = None, key = None, root = None):
        self.text = Text()
        self.undo = UndoDelegator()

    def get_selection_indices(self):
        first = self.text.index('1.0')
        last = self.text.index('end')
        return (first, last)


class UndoDelegator(object):
    """Minimally imitate UndoDelegator,UndoDelegator class.
    """

    def undo_block_start(*args):
        pass

    def undo_block_stop(*args):
        pass
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\idlelib\idle_test\mock_idle.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:04:17 St�edn� Evropa (b�n� �as)

# 2015.11.18 11:58:06 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/messenger/proto/xmpp/extensions/shared_handlers.py
from messenger.proto.xmpp.extensions import PyHandler

class IQHandler(PyHandler):

    def getFilterString(self):
        return '/iq/{0}'.format(self._ext.getXPath())


class IQChildHandler(PyHandler):
    __slots__ = ('_index',)

    def __init__(self, ext, index = 0):
        super(IQChildHandler, self).__init__(ext)
        self._index = index

    def getFilterString(self):
        return '/iq/{0}'.format(self._ext.getXPath(self._index))

    def handleTag(self, pyGlooxTag):
        child = self._ext.getChild(self._index)
        if not child:
            return
        result = pyGlooxTag.filterXPath(self.getFilterString())
        for tag in result:
            data = child.parseTag(tag)
            if data:
                yield data
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\proto\xmpp\extensions\shared_handlers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:58:06 Støední Evropa (bìžný èas)

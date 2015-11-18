# 2015.11.18 11:58:06 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/messenger/proto/xmpp/extensions/shared_queries.py
from messenger.proto.xmpp.extensions import PyQuery
from messenger.proto.xmpp.extensions.wg_items import WgClientExtension

class MessageQuery(PyQuery):
    __slots__ = ('_body',)

    def __init__(self, msgType, to, msgBody = '', ext = None):
        super(MessageQuery, self).__init__(msgType, ext, to)
        self._body = msgBody

    def getBody(self):
        return self._body


class PresenceQuery(PyQuery):

    def __init__(self, queryType, to = ''):
        super(PresenceQuery, self).__init__(queryType, WgClientExtension(), to)

    def setIgrID(self, igrID):
        if self._ext:
            self._ext.setIgrID(igrID)

    def setIgrRoomID(self, igrRoomID):
        if self._ext:
            self._ext.setIgrRoomID(igrRoomID)

    def setGameServerHost(self, host):
        if self._ext:
            self._ext.setGameServerHost(host)

    def setArenaGuiLabel(self, label):
        if self._ext:
            self._ext.setArenaGuiLabel(label)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\proto\xmpp\extensions\shared_queries.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:58:06 St�edn� Evropa (b�n� �as)

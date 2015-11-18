# 2015.11.18 11:57:35 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/messenger/gui/Scaleform/channels/xmpp/factories.py
from messenger.gui.Scaleform.channels.xmpp import lobby_controllers
from messenger.gui.interfaces import IControllerFactory
from messenger.proto.xmpp import find_criteria
from messenger.proto.xmpp.gloox_constants import MESSAGE_TYPE
from messenger.storage import storage_getter

class LobbyControllersFactory(IControllerFactory):

    @storage_getter('channels')
    def channelsStorage(self):
        return None

    def init(self):
        controllers = []
        channels = self.channelsStorage.getChannelsByCriteria(find_criteria.XMPPChannelFindCriteria())
        for channel in channels:
            controller = self.factory(channel)
            if controller is not None:
                controllers.append(controller)

        return controllers

    def factory(self, channel):
        controller = None
        msgType = channel.getProtoData().msgType
        if msgType == MESSAGE_TYPE.CHAT:
            controller = lobby_controllers.ChatChannelController(channel)
        return controller
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\gui\scaleform\channels\xmpp\factories.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:57:35 Støední Evropa (bìžný èas)

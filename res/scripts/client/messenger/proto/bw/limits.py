# 2015.11.18 11:57:49 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/messenger/proto/bw/limits.py
from constants import CHAT_MESSAGE_MAX_LENGTH, CHAT_MESSAGE_MAX_LENGTH_IN_BATTLE
from messenger.m_constants import MESSAGES_HISTORY_MAX_LEN
from messenger.proto.interfaces import IProtoLimits

class BattleLimits(IProtoLimits):

    def getMessageMaxLength(self):
        return CHAT_MESSAGE_MAX_LENGTH_IN_BATTLE

    def getHistoryMaxLength(self):
        return MESSAGES_HISTORY_MAX_LEN


class LobbyLimits(IProtoLimits):

    def getMessageMaxLength(self):
        return CHAT_MESSAGE_MAX_LENGTH

    def getHistoryMaxLength(self):
        return MESSAGES_HISTORY_MAX_LEN
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\proto\bw\limits.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:57:49 Støední Evropa (bìžný èas)

# 2015.11.18 11:59:48 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/bwobsolete_helpers/XMPP.py
import FantasyDemo
import FDGUI
import XMPPRoster

class AvatarRosterVisitor(XMPPRoster.XMPPRosterVisitor):

    def __init__(self):
        XMPPRoster.XMPPRosterVisitor.__init__(self)

    def onFriendAdd(self, friend, transport):
        msg = 'Added %s to the friends list.' % friend
        FantasyDemo.addChatMsg(-1, msg, FDGUI.TEXT_COLOUR_SYSTEM)

    def onFriendDelete(self, friend, transport):
        msg = 'Removed %s from the friends list.' % friend
        FantasyDemo.addChatMsg(-1, msg, FDGUI.TEXT_COLOUR_SYSTEM)

    def onFriendPresenceChange(self, friend, transport, oldPresence, newPresence):
        state = None
        if oldPresence == 'available' and newPresence == 'unavailable':
            state = 'gone offline'
        elif oldPresence == 'unavailable' and newPresence == 'available':
            state = 'come online'
        if state:
            msg = '%s has %s' % (friend, state)
            FantasyDemo.addChatMsg(-1, msg, FDGUI.TEXT_COLOUR_SYSTEM)
        return

    def onError(self, message):
        FantasyDemo.addChatMsg(-1, message, FDGUI.TEXT_COLOUR_SYSTEM)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\bwobsolete_helpers\xmpp.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:48 Støední Evropa (bìžný èas)

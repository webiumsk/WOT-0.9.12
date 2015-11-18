# 2015.11.18 12:02:34 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/Crypto/Protocol/__init__.py
"""Cryptographic protocols

Implements various cryptographic protocols.  (Don't expect to find
network protocols here.)

Crypto.Protocol.AllOrNothing
 Transforms a message into a set of message blocks, such that the blocks
 can be recombined to get the message back.

Crypto.Protocol.Chaffing
 Takes a set of authenticated message blocks (the wheat) and adds a number
 of randomly generated blocks (the chaff).

Crypto.Protocol.KDF
 A collection of standard key derivation functions.

:undocumented: __revision__
"""
__all__ = ['KDF']
__revision__ = '$Id$'
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\crypto\protocol\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:02:34 Støední Evropa (bìžný èas)

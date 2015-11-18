# 2015.11.18 12:02:33 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/Crypto/Hash/SHA1.py
"""SHA-1 cryptographic hash algorithm.

SHA-1_ produces the 160 bit digest of a message.

    >>> from Crypto.Hash import SHA1
    >>>
    >>> h = SHA1.new()
    >>> h.update(b'Hello')
    >>> print h.hexdigest()

*SHA* stands for Secure Hash Algorithm.

This algorithm is not considered secure. Do not use it for new designs.

.. _SHA-1: http://csrc.nist.gov/publications/fips/fips180-2/fips180-2.pdf
"""
from __future__ import nested_scopes
_revision__ = '$Id$'
__all__ = ['new', 'block_size', 'digest_size']
from Crypto.Util.py3compat import *
if sys.version_info[0] == 2 and sys.version_info[1] == 1:
    from Crypto.Util.py21compat import *

def __make_constructor():
    try:
        from hashlib import sha1 as _hash_new
    except ImportError:
        from sha import new as _hash_new

    h = _hash_new()
    if hasattr(h, 'new') and hasattr(h, 'name') and hasattr(h, 'digest_size') and hasattr(h, 'block_size'):
        return _hash_new
    else:
        _copy_sentinel = object()

        class _SHA1(object):
            digest_size = 20
            block_size = 64
            name = 'sha1'

            def __init__(self, *args):
                if args and args[0] is _copy_sentinel:
                    self._h = args[1]
                else:
                    self._h = _hash_new(*args)

            def copy(self):
                return _SHA1(_copy_sentinel, self._h.copy())

            def update(self, *args):
                f = self.update = self._h.update
                f(*args)

            def digest(self):
                f = self.digest = self._h.digest
                return f()

            def hexdigest(self):
                f = self.hexdigest = self._h.hexdigest
                return f()

        _SHA1.new = _SHA1
        return _SHA1


new = __make_constructor()
del __make_constructor
digest_size = new().digest_size
block_size = new().block_size
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\crypto\hash\sha1.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:02:33 St�edn� Evropa (b�n� �as)

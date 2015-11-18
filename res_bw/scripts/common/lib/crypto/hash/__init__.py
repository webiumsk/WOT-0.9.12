# 2015.11.18 12:02:33 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/Crypto/Hash/__init__.py
"""Hashing algorithms

Hash functions take arbitrary binary strings as input, and produce a random-like output
of fixed size that is dependent on the input; it should be practically infeasible 
to derive the original input data given only the hash function's
output. In other words, the hash function is *one-way*.

It should also not be practically feasible to find a second piece of data
(a *second pre-image*) whose hash is the same as the original message
(*weak collision resistance*).

Finally, it should not be feasible to find two arbitrary messages with the
same hash (*strong collision resistance*).

The output of the hash function is called the *digest* of the input message.
In general, the security of a hash function is related to the length of the
digest. If the digest is *n* bits long, its security level is roughly comparable
to the the one offered by an *n/2* bit encryption algorithm.

Hash functions can be used simply as a integrity check, or, in
association with a public-key algorithm, can be used to implement
digital signatures.

The hashing modules here all support the interface described in `PEP
247`_ , "API for Cryptographic Hash Functions". 

.. _`PEP 247` : http://www.python.org/dev/peps/pep-0247/

:undocumented: _MD2, _MD4, _RIPEMD160, _SHA224, _SHA256, _SHA384, _SHA512
"""
__all__ = ['HMAC', 'SHA1', 'CMAC']
__revision__ = '$Id$'
import sys
if sys.version_info[0] == 2 and sys.version_info[1] == 1:
    from Crypto.Util.py21compat import *
from Crypto.Util.py3compat import *

def new(algo, *args):
    """Initialize a new hash object.
    
    The first argument to this function may be an algorithm name or another
    hash object.
    
    This function has significant overhead.  It's recommended that you instead
    import and use the individual hash modules directly.
    """
    try:
        new_func = algo.new
    except AttributeError:
        pass
    else:
        return new_func(*args)

    if isinstance(algo, str):
        name = algo
    else:
        try:
            name = algo.name
        except AttributeError:
            raise ValueError('unsupported hash type %r' % (algo,))

    try:
        new_func = _new_funcs[name]
    except KeyError:
        try:
            import hashlib
        except ImportError:
            raise ValueError('unsupported hash type %s' % (name,))

        return hashlib.new(name, *args)

    return new_func(*args)


_new_funcs = {}

def _md2_new(*args):
    from Crypto.Hash import MD2
    _new_funcs['MD2'] = _new_funcs['md2'] = MD2.new
    return MD2.new(*args)


_new_funcs['MD2'] = _new_funcs['md2'] = _md2_new
del _md2_new

def _md4_new(*args):
    from Crypto.Hash import MD4
    _new_funcs['MD4'] = _new_funcs['md4'] = MD4.new
    return MD4.new(*args)


_new_funcs['MD4'] = _new_funcs['md4'] = _md4_new
del _md4_new

def _md5_new(*args):
    from Crypto.Hash import MD5
    _new_funcs['MD5'] = _new_funcs['md5'] = MD5.new
    return MD5.new(*args)


_new_funcs['MD5'] = _new_funcs['md5'] = _md5_new
del _md5_new

def _ripemd160_new(*args):
    from Crypto.Hash import RIPEMD160
    _new_funcs['RIPEMD160'] = _new_funcs['ripemd160'] = _new_funcs['RIPEMD'] = _new_funcs['ripemd'] = RIPEMD160.new
    return RIPEMD160.new(*args)


_new_funcs['RIPEMD160'] = _new_funcs['ripemd160'] = _new_funcs['RIPEMD'] = _new_funcs['ripemd'] = _ripemd160_new
del _ripemd160_new

def _sha1_new(*args):
    from Crypto.Hash import SHA1
    _new_funcs['SHA1'] = _new_funcs['sha1'] = _new_funcs['SHA'] = _new_funcs['sha'] = SHA1.new
    return SHA1.new(*args)


_new_funcs['SHA1'] = _new_funcs['sha1'] = _new_funcs['SHA'] = _new_funcs['sha'] = _sha1_new
del _sha1_new

def _sha224_new(*args):
    from Crypto.Hash import SHA224
    _new_funcs['SHA224'] = _new_funcs['sha224'] = SHA224.new
    return SHA224.new(*args)


_new_funcs['SHA224'] = _new_funcs['sha224'] = _sha224_new
del _sha224_new

def _sha256_new(*args):
    from Crypto.Hash import SHA256
    _new_funcs['SHA256'] = _new_funcs['sha256'] = SHA256.new
    return SHA256.new(*args)


_new_funcs['SHA256'] = _new_funcs['sha256'] = _sha256_new
del _sha256_new

def _sha384_new(*args):
    from Crypto.Hash import SHA384
    _new_funcs['SHA384'] = _new_funcs['sha384'] = SHA384.new
    return SHA384.new(*args)


_new_funcs['SHA384'] = _new_funcs['sha384'] = _sha384_new
del _sha384_new

def _sha512_new(*args):
    from Crypto.Hash import SHA512
    _new_funcs['SHA512'] = _new_funcs['sha512'] = SHA512.new
    return SHA512.new(*args)


_new_funcs['SHA512'] = _new_funcs['sha512'] = _sha512_new
del _sha512_new
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\crypto\hash\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:02:33 St�edn� Evropa (b�n� �as)

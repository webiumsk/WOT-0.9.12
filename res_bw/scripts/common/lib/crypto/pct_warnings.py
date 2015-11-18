# 2015.11.18 12:02:31 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/Crypto/pct_warnings.py


class CryptoWarning(Warning):
    """Base class for PyCrypto warnings"""
    pass


class CryptoDeprecationWarning(DeprecationWarning, CryptoWarning):
    """Base PyCrypto DeprecationWarning class"""
    pass


class CryptoRuntimeWarning(RuntimeWarning, CryptoWarning):
    """Base PyCrypto RuntimeWarning class"""
    pass


class RandomPool_DeprecationWarning(CryptoDeprecationWarning):
    """Issued when Crypto.Util.randpool.RandomPool is instantiated."""
    pass


class ClockRewindWarning(CryptoRuntimeWarning):
    """Warning for when the system clock moves backwards."""
    pass


class GetRandomNumber_DeprecationWarning(CryptoDeprecationWarning):
    """Issued when Crypto.Util.number.getRandomNumber is invoked."""
    pass


class DisableShortcut_DeprecationWarning(CryptoDeprecationWarning):
    """Issued when Counter.new(disable_shortcut=...) is invoked."""
    pass


class PowmInsecureWarning(CryptoRuntimeWarning):
    """Warning for when _fastmath is built without mpz_powm_sec"""
    pass


import warnings as _warnings
_warnings.filterwarnings('always', category=ClockRewindWarning, append=1)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\crypto\pct_warnings.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:02:31 Støední Evropa (bìžný èas)

# 2015.11.18 11:51:21 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/account_helpers/pwd_token.py
from constants import DEFAULT_LANGUAGE
import hashlib
__all__ = ['generate']

def _generateMd5Hash(pwd):
    md = hashlib.md5()
    md.update(pwd)
    return md.hexdigest()


_BY_LANG = {'cn': _generateMd5Hash,
 'vn': _generateMd5Hash}

def generate(pwd):
    return pwd


if DEFAULT_LANGUAGE in _BY_LANG:
    generate = _BY_LANG[DEFAULT_LANGUAGE]
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\account_helpers\pwd_token.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:51:21 Støední Evropa (bìžný èas)

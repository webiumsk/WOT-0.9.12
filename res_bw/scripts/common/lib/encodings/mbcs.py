# 2015.11.18 12:03:47 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/encodings/mbcs.py
""" Python 'mbcs' Codec for Windows


Cloned by Mark Hammond (mhammond@skippinet.com.au) from ascii.py,
which was written by Marc-Andre Lemburg (mal@lemburg.com).

(c) Copyright CNRI, All Rights Reserved. NO WARRANTY.

"""
from codecs import mbcs_encode, mbcs_decode
import codecs
encode = mbcs_encode

def decode(input, errors = 'strict'):
    return mbcs_decode(input, errors, True)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final = False):
        return mbcs_encode(input, self.errors)[0]


class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    _buffer_decode = mbcs_decode


class StreamWriter(codecs.StreamWriter):
    encode = mbcs_encode


class StreamReader(codecs.StreamReader):
    decode = mbcs_decode


def getregentry():
    return codecs.CodecInfo(name='mbcs', encode=encode, decode=decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\encodings\mbcs.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:03:47 St�edn� Evropa (b�n� �as)

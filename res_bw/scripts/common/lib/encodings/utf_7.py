# 2015.11.18 12:03:51 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/encodings/utf_7.py
""" Python 'utf-7' Codec

Written by Brian Quinlan (brian@sweetapp.com).
"""
import codecs
encode = codecs.utf_7_encode

def decode(input, errors = 'strict'):
    return codecs.utf_7_decode(input, errors, True)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final = False):
        return codecs.utf_7_encode(input, self.errors)[0]


class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    _buffer_decode = codecs.utf_7_decode


class StreamWriter(codecs.StreamWriter):
    encode = codecs.utf_7_encode


class StreamReader(codecs.StreamReader):
    decode = codecs.utf_7_decode


def getregentry():
    return codecs.CodecInfo(name='utf-7', encode=encode, decode=decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\encodings\utf_7.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:03:51 St�edn� Evropa (b�n� �as)

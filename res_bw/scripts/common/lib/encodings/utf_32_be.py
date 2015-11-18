# 2015.11.18 12:03:50 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/encodings/utf_32_be.py
"""
Python 'utf-32-be' Codec
"""
import codecs
encode = codecs.utf_32_be_encode

def decode(input, errors = 'strict'):
    return codecs.utf_32_be_decode(input, errors, True)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final = False):
        return codecs.utf_32_be_encode(input, self.errors)[0]


class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    _buffer_decode = codecs.utf_32_be_decode


class StreamWriter(codecs.StreamWriter):
    encode = codecs.utf_32_be_encode


class StreamReader(codecs.StreamReader):
    decode = codecs.utf_32_be_decode


def getregentry():
    return codecs.CodecInfo(name='utf-32-be', encode=encode, decode=decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\encodings\utf_32_be.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:03:50 Støední Evropa (bìžný èas)

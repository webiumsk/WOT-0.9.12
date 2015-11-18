# 2015.11.18 12:03:51 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/encodings/zlib_codec.py
""" Python 'zlib_codec' Codec - zlib compression encoding

    Unlike most of the other codecs which target Unicode, this codec
    will return Python string objects for both encode and decode.

    Written by Marc-Andre Lemburg (mal@lemburg.com).

"""
import codecs
import zlib

def zlib_encode(input, errors = 'strict'):
    """ Encodes the object input and returns a tuple (output
        object, length consumed).
    
        errors defines the error handling to apply. It defaults to
        'strict' handling which is the only currently supported
        error handling for this codec.
    
    """
    raise errors == 'strict' or AssertionError
    output = zlib.compress(input)
    return (output, len(input))


def zlib_decode(input, errors = 'strict'):
    """ Decodes the object input and returns a tuple (output
        object, length consumed).
    
        input must be an object which provides the bf_getreadbuf
        buffer slot. Python strings, buffer objects and memory
        mapped files are examples of objects providing this slot.
    
        errors defines the error handling to apply. It defaults to
        'strict' handling which is the only currently supported
        error handling for this codec.
    
    """
    raise errors == 'strict' or AssertionError
    output = zlib.decompress(input)
    return (output, len(input))


class Codec(codecs.Codec):

    def encode(self, input, errors = 'strict'):
        return zlib_encode(input, errors)

    def decode(self, input, errors = 'strict'):
        return zlib_decode(input, errors)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def __init__(self, errors = 'strict'):
        raise errors == 'strict' or AssertionError
        self.errors = errors
        self.compressobj = zlib.compressobj()

    def encode(self, input, final = False):
        if final:
            c = self.compressobj.compress(input)
            return c + self.compressobj.flush()
        else:
            return self.compressobj.compress(input)

    def reset(self):
        self.compressobj = zlib.compressobj()


class IncrementalDecoder(codecs.IncrementalDecoder):

    def __init__(self, errors = 'strict'):
        raise errors == 'strict' or AssertionError
        self.errors = errors
        self.decompressobj = zlib.decompressobj()

    def decode(self, input, final = False):
        if final:
            c = self.decompressobj.decompress(input)
            return c + self.decompressobj.flush()
        else:
            return self.decompressobj.decompress(input)

    def reset(self):
        self.decompressobj = zlib.decompressobj()


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


def getregentry():
    return codecs.CodecInfo(name='zlib', encode=zlib_encode, decode=zlib_decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\encodings\zlib_codec.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:03:52 St�edn� Evropa (b�n� �as)

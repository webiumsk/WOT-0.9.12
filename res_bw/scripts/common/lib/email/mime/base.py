# 2015.11.18 12:03:25 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/email/mime/base.py
"""Base class for MIME specializations."""
__all__ = ['MIMEBase']
from email import message

class MIMEBase(message.Message):
    """Base class for MIME specializations."""

    def __init__(self, _maintype, _subtype, **_params):
        """This constructor adds a Content-Type: and a MIME-Version: header.
        
        The Content-Type: header is taken from the _maintype and _subtype
        arguments.  Additional parameters for this header are taken from the
        keyword arguments.
        """
        message.Message.__init__(self)
        ctype = '%s/%s' % (_maintype, _subtype)
        self.add_header('Content-Type', ctype, **_params)
        self['MIME-Version'] = '1.0'
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\email\mime\base.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:03:25 St�edn� Evropa (b�n� �as)

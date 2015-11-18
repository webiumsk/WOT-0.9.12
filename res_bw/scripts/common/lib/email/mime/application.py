# 2015.11.18 12:03:25 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/email/mime/application.py
"""Class representing application/* type MIME documents."""
__all__ = ['MIMEApplication']
from email import encoders
from email.mime.nonmultipart import MIMENonMultipart

class MIMEApplication(MIMENonMultipart):
    """Class for generating application/* MIME documents."""

    def __init__(self, _data, _subtype = 'octet-stream', _encoder = encoders.encode_base64, **_params):
        """Create an application/* type MIME document.
        
        _data is a string containing the raw application data.
        
        _subtype is the MIME content type subtype, defaulting to
        'octet-stream'.
        
        _encoder is a function which will perform the actual encoding for
        transport of the application data, defaulting to base64 encoding.
        
        Any additional keyword arguments are passed to the base class
        constructor, which turns them into parameters on the Content-Type
        header.
        """
        if _subtype is None:
            raise TypeError('Invalid application MIME subtype')
        MIMENonMultipart.__init__(self, 'application', _subtype, **_params)
        self.set_payload(_data)
        _encoder(self)
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\email\mime\application.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:03:25 Støední Evropa (bìžný èas)

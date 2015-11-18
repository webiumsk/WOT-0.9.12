# 2015.11.18 12:03:25 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/email/mime/nonmultipart.py
"""Base class for MIME type messages that are not multipart."""
__all__ = ['MIMENonMultipart']
from email import errors
from email.mime.base import MIMEBase

class MIMENonMultipart(MIMEBase):
    """Base class for MIME multipart/* type messages."""

    def attach(self, payload):
        raise errors.MultipartConversionError('Cannot attach additional subparts to non-multipart/*')
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\email\mime\nonmultipart.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:03:25 Støední Evropa (bìžný èas)

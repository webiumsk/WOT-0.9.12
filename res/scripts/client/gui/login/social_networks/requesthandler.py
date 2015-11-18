# 2015.11.18 11:52:28 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/login/social_networks/RequestHandler.py
import httplib
import base64
from urlparse import urlparse, parse_qsl
from BaseHTTPServer import BaseHTTPRequestHandler
from gui import GUI_SETTINGS
_TEMPLATE_EMPTY_GIF_BASE64 = 'R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=='

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        params = dict(parse_qsl(parsed.query))
        if ('token' in params or 'token_encrypted' in params) and path == '/login/' and 'account_id' in params:
            if 'next' in params and params['next'] == GUI_SETTINGS.socialNetworkLogin['redirectURL']:
                self.onLoginWithRedirect(**params)
            else:
                self.onLogin(**params)
        else:
            self.send_response(httplib.NOT_FOUND)
            self.end_headers()

    def onLogin(self, **kwargs):
        if 'token_encrypted' in kwargs:
            token = kwargs['token_encrypted']
        else:
            token = kwargs['token']
        self.send_response(httplib.OK)
        self.send_header('Content-Type', 'image/gif')
        self.end_headers()
        self.wfile.write(base64.decodestring(_TEMPLATE_EMPTY_GIF_BASE64))
        self.wfile.close()
        self.server.keepData(token, kwargs['account_id'])

    def onLoginWithRedirect(self, **kwargs):
        if 'token_encrypted' in kwargs:
            token = kwargs['token_encrypted']
        else:
            token = kwargs['token']
        self.send_response(httplib.FOUND)
        self.send_header('Location', kwargs['next'])
        self.end_headers()
        self.server.keepData(token, kwargs['account_id'])

    def log_request(self, code = '-', size = '-'):
        pass
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\login\social_networks\requesthandler.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:52:28 St�edn� Evropa (b�n� �as)

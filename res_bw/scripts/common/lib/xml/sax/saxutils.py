# 2015.11.18 12:06:46 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/xml/sax/saxutils.py
"""A library of useful helper classes to the SAX classes, for the
convenience of application and driver writers.
"""
import os, urlparse, urllib, types
import io
import sys
import handler
import xmlreader
try:
    _StringTypes = [types.StringType, types.UnicodeType]
except AttributeError:
    _StringTypes = [types.StringType]

def __dict_replace(s, d):
    """Replace substrings of a string using a dictionary."""
    for key, value in d.items():
        s = s.replace(key, value)

    return s


def escape(data, entities = {}):
    """Escape &, <, and > in a string of data.
    
    You can escape other strings of data by passing a dictionary as
    the optional entities parameter.  The keys and values must all be
    strings; each key will be replaced with its corresponding value.
    """
    data = data.replace('&', '&amp;')
    data = data.replace('>', '&gt;')
    data = data.replace('<', '&lt;')
    if entities:
        data = __dict_replace(data, entities)
    return data


def unescape(data, entities = {}):
    """Unescape &amp;, &lt;, and &gt; in a string of data.
    
    You can unescape other strings of data by passing a dictionary as
    the optional entities parameter.  The keys and values must all be
    strings; each key will be replaced with its corresponding value.
    """
    data = data.replace('&lt;', '<')
    data = data.replace('&gt;', '>')
    if entities:
        data = __dict_replace(data, entities)
    return data.replace('&amp;', '&')


def quoteattr(data, entities = {}):
    """Escape and quote an attribute value.
    
    Escape &, <, and > in a string of data, then quote it for use as
    an attribute value.  The " character will be escaped as well, if
    necessary.
    
    You can escape other strings of data by passing a dictionary as
    the optional entities parameter.  The keys and values must all be
    strings; each key will be replaced with its corresponding value.
    """
    entities = entities.copy()
    entities.update({'\n': '&#10;',
     '\r': '&#13;',
     '\t': '&#9;'})
    data = escape(data, entities)
    if '"' in data:
        if "'" in data:
            data = '"%s"' % data.replace('"', '&quot;')
        else:
            data = "'%s'" % data
    else:
        data = '"%s"' % data
    return data


def _gettextwriter(out, encoding):
    if out is None:
        import sys
        out = sys.stdout
    if isinstance(out, io.RawIOBase):
        buffer = io.BufferedIOBase(out)
        buffer.close = lambda : None
    else:
        buffer = io.BufferedIOBase()
        buffer.writable = lambda : True
        buffer.write = out.write
        try:
            buffer.seekable = out.seekable
            buffer.tell = out.tell
        except AttributeError:
            pass

    class UnbufferedTextIOWrapper(io.TextIOWrapper):

        def write(self, s):
            super(UnbufferedTextIOWrapper, self).write(s)
            self.flush()

    return UnbufferedTextIOWrapper(buffer, encoding=encoding, errors='xmlcharrefreplace', newline='\n')


class XMLGenerator(handler.ContentHandler):

    def __init__(self, out = None, encoding = 'iso-8859-1'):
        handler.ContentHandler.__init__(self)
        out = _gettextwriter(out, encoding)
        self._write = out.write
        self._flush = out.flush
        self._ns_contexts = [{}]
        self._current_context = self._ns_contexts[-1]
        self._undeclared_ns_maps = []
        self._encoding = encoding

    def _qname(self, name):
        """Builds a qualified name from a (ns_url, localname) pair"""
        if name[0]:
            if 'http://www.w3.org/XML/1998/namespace' == name[0]:
                return 'xml:' + name[1]
            prefix = self._current_context[name[0]]
            if prefix:
                return prefix + ':' + name[1]
        return name[1]

    def startDocument(self):
        self._write(u'<?xml version="1.0" encoding="%s"?>\n' % self._encoding)

    def endDocument(self):
        self._flush()

    def startPrefixMapping(self, prefix, uri):
        self._ns_contexts.append(self._current_context.copy())
        self._current_context[uri] = prefix
        self._undeclared_ns_maps.append((prefix, uri))

    def endPrefixMapping(self, prefix):
        self._current_context = self._ns_contexts[-1]
        del self._ns_contexts[-1]

    def startElement(self, name, attrs):
        self._write(u'<' + name)
        for name, value in attrs.items():
            self._write(u' %s=%s' % (name, quoteattr(value)))

        self._write(u'>')

    def endElement(self, name):
        self._write(u'</%s>' % name)

    def startElementNS(self, name, qname, attrs):
        self._write(u'<' + self._qname(name))
        for prefix, uri in self._undeclared_ns_maps:
            if prefix:
                self._write(u' xmlns:%s="%s"' % (prefix, uri))
            else:
                self._write(u' xmlns="%s"' % uri)

        self._undeclared_ns_maps = []
        for name, value in attrs.items():
            self._write(u' %s=%s' % (self._qname(name), quoteattr(value)))

        self._write(u'>')

    def endElementNS(self, name, qname):
        self._write(u'</%s>' % self._qname(name))

    def characters(self, content):
        if not isinstance(content, unicode):
            content = unicode(content, self._encoding)
        self._write(escape(content))

    def ignorableWhitespace(self, content):
        if not isinstance(content, unicode):
            content = unicode(content, self._encoding)
        self._write(content)

    def processingInstruction(self, target, data):
        self._write(u'<?%s %s?>' % (target, data))


class XMLFilterBase(xmlreader.XMLReader):
    """This class is designed to sit between an XMLReader and the
    client application's event handlers.  By default, it does nothing
    but pass requests up to the reader and events on to the handlers
    unmodified, but subclasses can override specific methods to modify
    the event stream or the configuration requests as they pass
    through."""

    def __init__(self, parent = None):
        xmlreader.XMLReader.__init__(self)
        self._parent = parent

    def error(self, exception):
        self._err_handler.error(exception)

    def fatalError(self, exception):
        self._err_handler.fatalError(exception)

    def warning(self, exception):
        self._err_handler.warning(exception)

    def setDocumentLocator(self, locator):
        self._cont_handler.setDocumentLocator(locator)

    def startDocument(self):
        self._cont_handler.startDocument()

    def endDocument(self):
        self._cont_handler.endDocument()

    def startPrefixMapping(self, prefix, uri):
        self._cont_handler.startPrefixMapping(prefix, uri)

    def endPrefixMapping(self, prefix):
        self._cont_handler.endPrefixMapping(prefix)

    def startElement(self, name, attrs):
        self._cont_handler.startElement(name, attrs)

    def endElement(self, name):
        self._cont_handler.endElement(name)

    def startElementNS(self, name, qname, attrs):
        self._cont_handler.startElementNS(name, qname, attrs)

    def endElementNS(self, name, qname):
        self._cont_handler.endElementNS(name, qname)

    def characters(self, content):
        self._cont_handler.characters(content)

    def ignorableWhitespace(self, chars):
        self._cont_handler.ignorableWhitespace(chars)

    def processingInstruction(self, target, data):
        self._cont_handler.processingInstruction(target, data)

    def skippedEntity(self, name):
        self._cont_handler.skippedEntity(name)

    def notationDecl(self, name, publicId, systemId):
        self._dtd_handler.notationDecl(name, publicId, systemId)

    def unparsedEntityDecl(self, name, publicId, systemId, ndata):
        self._dtd_handler.unparsedEntityDecl(name, publicId, systemId, ndata)

    def resolveEntity(self, publicId, systemId):
        return self._ent_handler.resolveEntity(publicId, systemId)

    def parse(self, source):
        self._parent.setContentHandler(self)
        self._parent.setErrorHandler(self)
        self._parent.setEntityResolver(self)
        self._parent.setDTDHandler(self)
        self._parent.parse(source)

    def setLocale(self, locale):
        self._parent.setLocale(locale)

    def getFeature(self, name):
        return self._parent.getFeature(name)

    def setFeature(self, name, state):
        self._parent.setFeature(name, state)

    def getProperty(self, name):
        return self._parent.getProperty(name)

    def setProperty(self, name, value):
        self._parent.setProperty(name, value)

    def getParent(self):
        return self._parent

    def setParent(self, parent):
        self._parent = parent


def prepare_input_source(source, base = ''):
    """This function takes an InputSource and an optional base URL and
    returns a fully resolved InputSource object ready for reading."""
    if type(source) in _StringTypes:
        source = xmlreader.InputSource(source)
    elif hasattr(source, 'read'):
        f = source
        source = xmlreader.InputSource()
        source.setByteStream(f)
        if hasattr(f, 'name'):
            source.setSystemId(f.name)
    if source.getByteStream() is None:
        try:
            sysid = source.getSystemId()
            basehead = os.path.dirname(os.path.normpath(base))
            encoding = sys.getfilesystemencoding()
            if isinstance(sysid, unicode):
                if not isinstance(basehead, unicode):
                    try:
                        basehead = basehead.decode(encoding)
                    except UnicodeDecodeError:
                        sysid = sysid.encode(encoding)

            elif isinstance(basehead, unicode):
                try:
                    sysid = sysid.decode(encoding)
                except UnicodeDecodeError:
                    basehead = basehead.encode(encoding)

            sysidfilename = os.path.join(basehead, sysid)
            isfile = os.path.isfile(sysidfilename)
        except UnicodeError:
            isfile = False

        if isfile:
            source.setSystemId(sysidfilename)
            f = open(sysidfilename, 'rb')
        else:
            source.setSystemId(urlparse.urljoin(base, source.getSystemId()))
            f = urllib.urlopen(source.getSystemId())
        source.setByteStream(f)
    return source
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\xml\sax\saxutils.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:06:47 St�edn� Evropa (b�n� �as)

# 2015.11.18 12:06:42 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/xml/dom/NodeFilter.py


class NodeFilter:
    """
    This is the DOM2 NodeFilter interface. It contains only constants.
    """
    FILTER_ACCEPT = 1
    FILTER_REJECT = 2
    FILTER_SKIP = 3
    SHOW_ALL = 4294967295L
    SHOW_ELEMENT = 1
    SHOW_ATTRIBUTE = 2
    SHOW_TEXT = 4
    SHOW_CDATA_SECTION = 8
    SHOW_ENTITY_REFERENCE = 16
    SHOW_ENTITY = 32
    SHOW_PROCESSING_INSTRUCTION = 64
    SHOW_COMMENT = 128
    SHOW_DOCUMENT = 256
    SHOW_DOCUMENT_TYPE = 512
    SHOW_DOCUMENT_FRAGMENT = 1024
    SHOW_NOTATION = 2048

    def acceptNode(self, node):
        raise NotImplementedError
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\xml\dom\nodefilter.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:06:42 St�edn� Evropa (b�n� �as)

# 2015.11.18 12:05:01 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/lib2to3/pgen2/literals.py
"""Safely evaluate Python string literals without using eval()."""
import re
simple_escapes = {'a': '\x07',
 'b': '\x08',
 'f': '\x0c',
 'n': '\n',
 'r': '\r',
 't': '\t',
 'v': '\x0b',
 "'": "'",
 '"': '"',
 '\\': '\\'}

def escape(m):
    all, tail = m.group(0, 1)
    if not all.startswith('\\'):
        raise AssertionError
        esc = simple_escapes.get(tail)
        return esc is not None and esc
    else:
        if tail.startswith('x'):
            hexes = tail[1:]
            if len(hexes) < 2:
                raise ValueError("invalid hex string escape ('\\%s')" % tail)
            try:
                i = int(hexes, 16)
            except ValueError:
                raise ValueError("invalid hex string escape ('\\%s')" % tail)

        else:
            try:
                i = int(tail, 8)
            except ValueError:
                raise ValueError("invalid octal string escape ('\\%s')" % tail)

        return chr(i)


def evalString(s):
    if not (s.startswith("'") or s.startswith('"')):
        raise AssertionError(repr(s[:1]))
        q = s[0]
        q = s[:3] == q * 3 and q * 3
    raise s.endswith(q) or AssertionError(repr(s[-len(q):]))
    raise len(s) >= 2 * len(q) or AssertionError
    s = s[len(q):-len(q)]
    return re.sub('\\\\(\\\'|\\"|\\\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})', escape, s)


def test():
    for i in range(256):
        c = chr(i)
        s = repr(c)
        e = evalString(s)
        if e != c:
            print i, c, s, e


if __name__ == '__main__':
    test()
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\lib2to3\pgen2\literals.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:05:01 St�edn� Evropa (b�n� �as)

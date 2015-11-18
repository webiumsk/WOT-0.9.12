# 2015.11.18 12:02:51 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/curses/__init__.py
"""curses

The main package for curses support for Python.  Normally used by importing
the package, and perhaps a particular module inside it.

   import curses
   from curses import textpad
   curses.initscr()
   ...

"""
__revision__ = '$Id$'
from _curses import *
from curses.wrapper import wrapper
import os as _os
import sys as _sys

def initscr():
    import _curses, curses
    setupterm(term=_os.environ.get('TERM', 'unknown'), fd=_sys.__stdout__.fileno())
    stdscr = _curses.initscr()
    for key, value in _curses.__dict__.items():
        if key[0:4] == 'ACS_' or key in ('LINES', 'COLS'):
            setattr(curses, key, value)

    return stdscr


def start_color():
    import _curses, curses
    retval = _curses.start_color()
    if hasattr(_curses, 'COLORS'):
        curses.COLORS = _curses.COLORS
    if hasattr(_curses, 'COLOR_PAIRS'):
        curses.COLOR_PAIRS = _curses.COLOR_PAIRS
    return retval


try:
    has_key
except NameError:
    from has_key import has_key
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\curses\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:02:51 St�edn� Evropa (b�n� �as)

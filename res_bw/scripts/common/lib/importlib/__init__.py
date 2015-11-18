# 2015.11.18 12:04:21 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/importlib/__init__.py
"""Backport of importlib.import_module from 3.x."""
import sys

def _resolve_name(name, package, level):
    """Return the absolute name of the module to be imported."""
    if not hasattr(package, 'rindex'):
        raise ValueError("'package' not set to a string")
    dot = len(package)
    for x in xrange(level, 1, -1):
        try:
            dot = package.rindex('.', 0, dot)
        except ValueError:
            raise ValueError('attempted relative import beyond top-level package')

    return '%s.%s' % (package[:dot], name)


def import_module(name, package = None):
    """Import a module.
    
    The 'package' argument is required when performing a relative import. It
    specifies the package to use as the anchor point from which to resolve the
    relative import to an absolute import.
    
    """
    if name.startswith('.'):
        if not package:
            raise TypeError("relative imports require the 'package' argument")
        level = 0
        for character in name:
            if character != '.':
                break
            level += 1

        name = _resolve_name(name[level:], package, level)
    __import__(name)
    return sys.modules[name]
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\importlib\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:04:21 St�edn� Evropa (b�n� �as)

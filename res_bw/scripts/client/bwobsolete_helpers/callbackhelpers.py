# 2015.11.18 11:59:45 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/bwobsolete_helpers/CallbackHelpers.py
"""This module contains a number of helper functions intended simplify
implementing callback functions in a safe way.
"""
import BigWorld

def IgnoreCallbackIfDestroyed(function):

    def checkIfDestroyed(self, *args, **kwargs):
        if not isinstance(self, BigWorld.Entity):
            raise AssertionError
            return self.isDestroyed or function(self, *args, **kwargs)

    return checkIfDestroyed
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\bwobsolete_helpers\callbackhelpers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 11:59:45 Støední Evropa (bìžný èas)

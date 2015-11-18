# 2015.11.18 12:06:21 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/plat-os2emx/pwd.py
"""Replacement for pwd standard extension module, intended for use on
OS/2 and similar systems which don't normally have an /etc/passwd file.

The standard Unix password database is an ASCII text file with 7 fields
per record (line), separated by a colon:
  - user name (string)
  - password (encrypted string, or "*" or "")
  - user id (integer)
  - group id (integer)
  - description (usually user's name)
  - home directory (path to user's home directory)
  - shell (path to the user's login shell)

(see the section 8.1 of the Python Library Reference)

This implementation differs from the standard Unix implementation by
allowing use of the platform's native path separator character - ';' on OS/2,
DOS and MS-Windows - as the field separator in addition to the Unix
standard ":".  Additionally, when ":" is the separator path conversions
are applied to deal with any munging of the drive letter reference.

The module looks for the password database at the following locations
(in order first to last):
  - ${ETC_PASSWD}             (or %ETC_PASSWD%)
  - ${ETC}/passwd             (or %ETC%/passwd)
  - ${PYTHONHOME}/Etc/passwd  (or %PYTHONHOME%/Etc/passwd)

Classes
-------

None

Functions
---------

getpwuid(uid) -  return the record for user-id uid as a 7-tuple

getpwnam(name) - return the record for user 'name' as a 7-tuple

getpwall() -     return a list of 7-tuples, each tuple being one record
                 (NOTE: the order is arbitrary)

Attributes
----------

passwd_file -    the path of the password database file

"""
import os
__passwd_path = []
if os.environ.has_key('ETC_PASSWD'):
    __passwd_path.append(os.environ['ETC_PASSWD'])
if os.environ.has_key('ETC'):
    __passwd_path.append('%s/passwd' % os.environ['ETC'])
if os.environ.has_key('PYTHONHOME'):
    __passwd_path.append('%s/Etc/passwd' % os.environ['PYTHONHOME'])
passwd_file = None
for __i in __passwd_path:
    try:
        __f = open(__i, 'r')
        __f.close()
        passwd_file = __i
        break
    except:
        pass

def __nullpathconv(path):
    return path.replace(os.altsep, os.sep)


def __unixpathconv(path):
    if path[0] == '$':
        conv = path[1] + ':' + path[2:]
    elif path[1] == ';':
        conv = path[0] + ':' + path[2:]
    else:
        conv = path
    return conv.replace(os.altsep, os.sep)


__field_sep = {':': __unixpathconv}
if os.pathsep:
    if os.pathsep != ':':
        __field_sep[os.pathsep] = __nullpathconv

def __get_field_sep(record):
    fs = None
    for c in __field_sep.keys():
        if record.count(c) == 6:
            fs = c
            break

    if fs:
        return fs
    else:
        raise KeyError, '>> passwd database fields not delimited <<'
        return


class Passwd:

    def __init__(self, name, passwd, uid, gid, gecos, dir, shell):
        self.__dict__['pw_name'] = name
        self.__dict__['pw_passwd'] = passwd
        self.__dict__['pw_uid'] = uid
        self.__dict__['pw_gid'] = gid
        self.__dict__['pw_gecos'] = gecos
        self.__dict__['pw_dir'] = dir
        self.__dict__['pw_shell'] = shell
        self.__dict__['_record'] = (self.pw_name,
         self.pw_passwd,
         self.pw_uid,
         self.pw_gid,
         self.pw_gecos,
         self.pw_dir,
         self.pw_shell)

    def __len__(self):
        return 7

    def __getitem__(self, key):
        return self._record[key]

    def __setattr__(self, name, value):
        raise AttributeError('attribute read-only: %s' % name)

    def __repr__(self):
        return str(self._record)

    def __cmp__(self, other):
        this = str(self._record)
        if this == other:
            return 0
        elif this < other:
            return -1
        else:
            return 1


def __read_passwd_file():
    if passwd_file:
        passwd = open(passwd_file, 'r')
    else:
        raise KeyError, '>> no password database <<'
    uidx = {}
    namx = {}
    sep = None
    while 1:
        entry = passwd.readline().strip()
        if len(entry) > 6:
            if sep is None:
                sep = __get_field_sep(entry)
            fields = entry.split(sep)
            for i in (2, 3):
                fields[i] = int(fields[i])

            for i in (5, 6):
                fields[i] = __field_sep[sep](fields[i])

            record = Passwd(*fields)
            if not uidx.has_key(fields[2]):
                uidx[fields[2]] = record
            if not namx.has_key(fields[0]):
                namx[fields[0]] = record
        elif len(entry) > 0:
            pass
        else:
            break

    passwd.close()
    if len(uidx) == 0:
        raise KeyError
    return (uidx, namx)


def getpwuid(uid):
    u, n = __read_passwd_file()
    return u[uid]


def getpwnam(name):
    u, n = __read_passwd_file()
    return n[name]


def getpwall():
    u, n = __read_passwd_file()
    return n.values()


if __name__ == '__main__':
    getpwall()
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\plat-os2emx\pwd.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:06:21 St�edn� Evropa (b�n� �as)

# 2015.11.18 12:05:33 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/plat-irix5/cdplayer.py
from warnings import warnpy3k
warnpy3k('the cdplayer module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
cdplayerrc = '.cdplayerrc'

class Cdplayer:

    def __init__(self, tracklist):
        import string
        self.artist = ''
        self.title = ''
        if type(tracklist) == type(''):
            t = []
            for i in range(2, len(tracklist), 4):
                t.append((None, (string.atoi(tracklist[i:i + 2]), string.atoi(tracklist[i + 2:i + 4]))))

            tracklist = t
        self.track = [None] + [''] * len(tracklist)
        self.id = 'd' + string.zfill(len(tracklist), 2)
        for track in tracklist:
            start, length = track
            self.id = self.id + string.zfill(length[0], 2) + string.zfill(length[1], 2)

        try:
            import posix
            f = open(posix.environ['HOME'] + '/' + cdplayerrc, 'r')
        except IOError:
            return

        import re
        reg = re.compile('^([^:]*):\\t(.*)')
        s = self.id + '.'
        l = len(s)
        while 1:
            line = f.readline()
            if line == '':
                break
            if line[:l] == s:
                line = line[l:]
                match = reg.match(line)
                if not match:
                    print 'syntax error in ~/' + cdplayerrc
                    continue
                name, value = match.group(1, 2)
                if name == 'title':
                    self.title = value
                elif name == 'artist':
                    self.artist = value
                elif name[:5] == 'track':
                    trackno = string.atoi(name[6:])
                    self.track[trackno] = value

        f.close()
        return

    def write(self):
        import posix
        filename = posix.environ['HOME'] + '/' + cdplayerrc
        try:
            old = open(filename, 'r')
        except IOError:
            old = open('/dev/null', 'r')

        new = open(filename + '.new', 'w')
        s = self.id + '.'
        l = len(s)
        while 1:
            line = old.readline()
            if line == '':
                break
            if line[:l] != s:
                new.write(line)

        new.write(self.id + '.title:\t' + self.title + '\n')
        new.write(self.id + '.artist:\t' + self.artist + '\n')
        for i in range(1, len(self.track)):
            new.write('%s.track.%r:\t%s\n' % (self.id, i, self.track[i]))

        old.close()
        new.close()
        posix.rename(filename + '.new', filename)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\plat-irix5\cdplayer.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:05:33 St�edn� Evropa (b�n� �as)

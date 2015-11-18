# 2015.11.18 12:06:22 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/plat-sunos5/CDIO.py
CDROM_LBA = 1
CDROM_MSF = 2
CDROM_DATA_TRACK = 4
CDROM_LEADOUT = 170
CDROM_AUDIO_INVALID = 0
CDROM_AUDIO_PLAY = 17
CDROM_AUDIO_PAUSED = 18
CDROM_AUDIO_COMPLETED = 19
CDROM_AUDIO_ERROR = 20
CDROM_AUDIO_NO_STATUS = 21
CDROM_DA_NO_SUBCODE = 0
CDROM_DA_SUBQ = 1
CDROM_DA_ALL_SUBCODE = 2
CDROM_DA_SUBCODE_ONLY = 3
CDROM_XA_DATA = 0
CDROM_XA_SECTOR_DATA = 1
CDROM_XA_DATA_W_ERROR = 2
CDROM_BLK_512 = 512
CDROM_BLK_1024 = 1024
CDROM_BLK_2048 = 2048
CDROM_BLK_2056 = 2056
CDROM_BLK_2336 = 2336
CDROM_BLK_2340 = 2340
CDROM_BLK_2352 = 2352
CDROM_BLK_2368 = 2368
CDROM_BLK_2448 = 2448
CDROM_BLK_2646 = 2646
CDROM_BLK_2647 = 2647
CDROM_BLK_SUBCODE = 96
CDROM_NORMAL_SPEED = 0
CDROM_DOUBLE_SPEED = 1
CDROM_QUAD_SPEED = 3
CDROM_TWELVE_SPEED = 12
CDROM_MAXIMUM_SPEED = 255
CDIOC = 1024
CDROMPAUSE = CDIOC | 151
CDROMRESUME = CDIOC | 152
CDROMPLAYMSF = CDIOC | 153
CDROMPLAYTRKIND = CDIOC | 154
CDROMREADTOCHDR = CDIOC | 155
CDROMREADTOCENTRY = CDIOC | 156
CDROMSTOP = CDIOC | 157
CDROMSTART = CDIOC | 158
CDROMEJECT = CDIOC | 159
CDROMVOLCTRL = CDIOC | 160
CDROMSUBCHNL = CDIOC | 161
CDROMREADMODE2 = CDIOC | 162
CDROMREADMODE1 = CDIOC | 163
CDROMREADOFFSET = CDIOC | 164
CDROMGBLKMODE = CDIOC | 165
CDROMSBLKMODE = CDIOC | 166
CDROMCDDA = CDIOC | 167
CDROMCDXA = CDIOC | 168
CDROMSUBCODE = CDIOC | 169
CDROMGDRVSPEED = CDIOC | 170
CDROMSDRVSPEED = CDIOC | 171
SCMD_READ_TOC = 67
SCMD_PLAYAUDIO_MSF = 71
SCMD_PLAYAUDIO_TI = 72
SCMD_PAUSE_RESUME = 75
SCMD_READ_SUBCHANNEL = 66
SCMD_PLAYAUDIO10 = 69
SCMD_PLAYTRACK_REL10 = 73
SCMD_READ_HEADER = 68
SCMD_PLAYAUDIO12 = 165
SCMD_PLAYTRACK_REL12 = 169
SCMD_CD_PLAYBACK_CONTROL = 201
SCMD_CD_PLAYBACK_STATUS = 196
SCMD_READ_CDDA = 216
SCMD_READ_CDXA = 219
SCMD_READ_ALL_SUBCODES = 223
CDROM_MODE2_SIZE = 2336
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\plat-sunos5\cdio.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.11.18 12:06:22 St�edn� Evropa (b�n� �as)

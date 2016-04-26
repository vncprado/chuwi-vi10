b = bytearray(open('SileadTouch.fw', 'rb').read())
for i in range(len(b)):
    b[i] ^= 0x88
open('GSL_TS_CFG.h', 'w').write(b)

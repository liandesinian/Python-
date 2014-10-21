#!/usr/bin/env python

import sys, email, codecs
from email import Header

msg=email.message_from_file(sys.stdin)
for header, value in msg.items():
    headerparts=Header.decode_header(value)
    headerval=[]
    for part in headerparts:
        data, charset=part
        if charset is None:
            charset='ascii'
        dec=codecs.getdecoder(charset)
        enc=codecs.getencoder('utf-8')
        data=enc(dec(data)[0])[0]
        headerval.append(data)
        print '%s: %s' % (header, ' '.join(headerval))

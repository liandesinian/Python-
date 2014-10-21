#!/usr/bin/env python

import sys, smtplib, socket

if len(sys.argv)<4:
    print 'Syntax: %s server fromaddr toaddr [to addr...]' % sys.argv[0]
    sys.exit(1)
    
server=sys.argv[1]
fromaddr=sys.argv[2]
toaddrs=sys.argv[3:]

message='''To: %s
From: %s
Subject: Test

Hello, this is a test'''%(', '.join(toaddrs), fromaddr)

try:
    s=smtplib.SMTP(server)
    s.set_debuglevel(1)
    s.sendmail(fromaddr, toaddrs, message)
except (socket.gaierror, socket.errnor, socket.herror, smtplib.SMTPException), e:
    print '*** Your message may not have been sent'
    print e
    sys.exit(1)
else:
    print 'Message successfully sent to %d recipient(s)'%len(toaddrs)

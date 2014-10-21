#!/usr/bin/env python

import sys, smtplib, socket
from getpass import getpass

if len(sys.argv)<4:
    print 'Syntax: %s server fromaddr toaddr' % sys.argv[0]
    sys.exit(255)
    
server=sys.argv[1]
fromaddr=sys.argv[2]
toaddrs=sys.argv[3:]

message='''To: %s
From: %s
Subject: Test

Hello, this is a test'''%(', '.join(toaddrs), fromaddr)

sys.stdout.write('Enter username: ')
username=sys.stdin.readline().strip()
password=getpass('Enter password: ')

try:
    s=smtplib.SMTP(server)
    try:
        s.login(username, password)
    except smtplib.SMTPException, e:
        print "authentication failed:", e
        sys.exit(1)
    s.sendmail(fromaddr, toaddrs, message)
except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), e:
    print '*** Your message may not have been sent'
    print e
    sys.exit(2)
else:
    print 'Message successfully sent to %d recipient(s)'%len(toaddrs)

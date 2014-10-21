#!/usr/bin/env python

import sys, smtplib, socket

if len(sys.argv)<4:
    print 'Syntax: %s server fromaddr toaddr'%sys.argv[0]
    sys.exit(1)

server=sys.argv[1]
fromaddr=sys.argv[2]
toaddrs=sys.argv[3:]

message='''To: %s
From: %s
Subject: test

Hello, this is a test'''%(', '.join(toaddrs), fromaddr)

try:
    s=smtplib.SMTP(server)
    code=s.ehlo()[0]
    usesesmtp=1
    if not (200<=code<=299):
        usesestmp=0
        code=s.helo()[0]
        if not (200<=code<=299):
            raise SMTPHeloError(code, resp)
    
    if usesesmtp and s.has_extn('starttls'):
        print 'Negotiating TLS...'
        s.starttls()
        code=s.ehlo()[0]
        if not (200<=code<=299):
            print 'Could not EHLO after STRTTLS'
            sys.exit(5)
        print 'Using TLS connection'
    else:
        print 'Server does not support TLS'
    s.sendmail(fromaddr, toaddrs, message)
    
except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), e:
    print '*** Your message may not have been sent'
    print e
    sys.exit(1)
else:
    print 'Message successfully sent to %d recipient(s)'%len(toaddrs)

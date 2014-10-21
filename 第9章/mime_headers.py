#!/usr/bin/env python
#-*-coding:utf-8-*-

from email.MIMEText import MIMEText
from email.Header import Header
from email import Utils
message='''Hello, this is a test'''

msg=MIMEText(message)
msg['To']='recipient@example.com'
fromhdr=Header('Michael M"你"ller', 'utf-8')
fromhdr.append('<mmueller@example.com>', 'ascii')
msg['From']=fromhdr
msg['Subject']=Header('Test')
msg['Date']=Utils.formatdate(localtime=1)
msg['Message-ID']=Utils.make_msgid()

print msg.as_string()

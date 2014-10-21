#!/usr/bin/env python

from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Utils, Encoders
import mimetypes, sys

def genpart(data, contenttype):
    maintype, subtype=contenttype.split('/')
    if maintype=='text':
        retval=MIMEText(data, _subtype=subtype)
    else:
        retval=MIMEBase(maintype, subtype)
        retval.set_payload(data)
        Encoders.encode_base64(retval)
    
    return retval

def attachment(filename):
    fd=open(filename, 'rb')
    mimetype, mimeencoding=mimetypes.guess_type(filename)
    if mimeencoding or (mimetype is None):
        mimetype='application/octet-stream'
    retval=genpart(fd.read(), mimetype)
    retval.add_header('Content-Disposition', 'attachment', filename=filename)
    fd.close()
    return retval

messagetext='''Hello, This is a test'''

messagehtml='Hello, <p> this is a <B>great</B> test message</p>'''

msg=MIMEMultipart()
msg['To']='recipient@example.com'
msg['From']='Test sender <sender@example.com>'
msg['Subject']='Test'
msg['Date']=Utils.formatdate(localtime=1)
msg['Message-ID']=Utils.make_msgid()

body=MIMEMultipart('alternative')
body.attach(genpart(messagetext, 'text/plain'))
body.attach(genpart(messagetext, 'text/html'))
msg.attach(body)

for filename in sys.argv[1:]:
    msg.attach(attachment(filename))

print msg.as_string()

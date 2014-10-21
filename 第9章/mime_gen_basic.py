#!/usr/bin/env python

from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Utils, Encoders
import mimetypes, sys

def attachment(filename):
    fd=open(filename, 'rb')
    mimetype, mimeencoding=mimetypes.guess_type(filename)
    if mimeencoding or (mimetype is None):
        mimetype='application/octet-stream'
    maintype, subtype=mimetype.split('/')
    if maintype=='text':
        retval=MIMEText(fd.read(), _subtype=subtype)
    else:
        retval=MIMEBase(maintype, subtype)
        retval.set_payload(fd.read())
        Encoders.encode_base64(retval)
    retval.add_header('Content-Disposition', 'attachment', filename=filename)
    
    fd.close()
    return retval

message='''Hello, this is a test'''

msg=MIMEMultipart()
msg['To']='recipient@example.com'
msg['From']='Test Sender <sender@example.com>'
msg['Subject']='Test'
msg['Date']=Utils.formatdate(localtime=1)
msg['Message-ID']=Utils.make_msgid()

body=MIMEText(message, _subtype='plain')
msg.attach(body)
for filename in sys.argv[1:]:
    msg.attach(attachment(filename))
print msg.as_string()

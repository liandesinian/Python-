#!/usr/bin/env python

import sys, email, time
from email import Utils

def getdate(msg):
    
    if not 'date' in msg:
        return None
    
    datehdr=msg['date'].strip()
    try:
        return Utils.mktime_tz(Utils.parsedate_tz(datehdr))
    except:
        return None
        
msg=email.message_from_file(sys.stdin)

dateval=getdate(msg)
if dateval is None:
    print 'No valid date was found.'
else:
    print 'Message was sent on', time.strftime('%A, %B %d %Y at %I:%M %p', time.localtime(dateval))

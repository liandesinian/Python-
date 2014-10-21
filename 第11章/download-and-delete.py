#!/usr/bin/env python

import getpass, poplib, sys, email

def log(text):
    '''Simple function to write status information'''
    sys.stdout.write(text)
    sys.stdout.flush()
    
(host, user, dest)=sys.argv[1:]
passwd=getpass.getpass()

destfd=open(dest, 'at')

log('Connecting to %s...\n'%host)
p=poplib.POP3(host)
try:
    log('Logging on...')
    p.user(user)
    p.pass_(passwd)
    log('success.\n')
except poplib.error_proto, e:
    print 'Login failed:', e
    sys.exit(1)
    
log('Scanning INBOX...')
mblist=p.list()[1]
log('%d messages.\n'%len(mblist))

dellist=[]

for item in mblist:
    number, octets=item.split(' ')
    log('Downloading message %s (%s bytes)...'%(number, octets))
    
    lines=p.retr(number)[1]
    msg=email.message_from_string('\n'.join(lines))
    destfd.write(msg.as_string(unixfrom=1))
    destfd.write('\n')
    dellist.append(number)
    
    log('done\n')
    
destfd.close()

counter=0

for number in dellist:
    counter+=1
    log('Deleting message %d of %d\r'%(counter, len(dellist)))
    
    p.dele(number)
    
if counter>0:
    log('successfully deleted %d messages from server.\n'% counter)
else:
    log('No messages present to download.\n')
    
log('Closing connection,....')
p.quit()
log('done\n')

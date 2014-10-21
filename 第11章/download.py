#!/usr/bin/env python

import getpass, poplib, sys, email
(host, user, dest)=sys.argv[1:]
passwd=getpass.getpass()

#open a mailbox for appending
destfd=open(dest, 'at')

#Log in like usual
p=poplib.POP3(host)
try:
    p.user(user)
    p.pass_(passwd)
except poplib.error_proto, e:
    print 'Login failed:', e
    sys.exit(1)
    
#Iterate over the list of messages in the mailbox
for item in p.list()[1]:
    number, octets=item.split(' ')
    print 'Downloading message %s (%s bytes)' %(number, octets)
    
    #Retrieve the message
    lines=p.retr(number)[1]
    
    #Create an e-mail object representing the message
    msg=email.message_from_string('\n'.join(lines))
    
    #Write it out to the mailbox
    destfd.write(msg.as_string(unixfrom=1))
    
    #Make sure there's an extra newline separating messages
    destfd.write('\n')
    
p.quit()
destfd.close()

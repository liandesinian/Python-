#!/usr/bin/env python

from socket import *
import sys

def getipaddrs(hostname):
    result=getaddrinfo(hostname, None, 0, SOCK_STREAM)
    return [x[4][0] for x in result]
    
hostname=gethostname()
print 'Host name:', hostname

print 'Fully-qualitiedname:', getfqdn(hostname)
try:
    print 'IP addresses:', ', '.join(getipaddrs(hostname))
except gaierror, e:
    print "Couldn't get ip addresses:", e

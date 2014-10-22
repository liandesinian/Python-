#!/usr/bin/env python

from socket import *
import sys

try:
    result=gethostbyaddr(sys.argv[1])
    print 'Primary hostname:'
    print " "+result[0]
    
    print '\nAddress:'
    for item in result[2]:
        print ' '+item
        
except herror, e:
    print 'Could not look up name:', e

#!/usr/bin/env python

import sys,urllib2

req=urllib2.Request(sys.argv[1])
fd=urllib2.urlopen(req)
while True:
	data=fd.read(1024)
	if not len(data):
		break
	sys.stdout.write(data)


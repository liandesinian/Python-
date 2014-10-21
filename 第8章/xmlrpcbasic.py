#!/usr/bin/env python

import xmlrpclib
url='http://www.oreillynet.com/meerkat/xml-rpc/server.php'
s=xmlrpclib.ServerProxy(url)
catdata=s.meerkat.getCategories()
cattitiles=[item['title'] for item in catdata]
cattitles.sort()
for item in cattitles:
    print item

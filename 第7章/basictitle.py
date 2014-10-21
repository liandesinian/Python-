#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys
from HTMLParser import HTMLParser

class TitleParser(HTMLParser):
	def __init__(self):
		self.title=''
		self.readingtitle=0
		HTMLParser.__init__(self)#初始化和重置实例
	
	def handle_starttag(self,tag,attrs):
		if tag=='title':
			print 'start:',tag
			self.readingtitle=1

	def handle_data(self,data):
		if self.readingtitle:
			self.title+=data

	def handle_endtag(self,tag):
		if tag=='title':
			print 'end:',tag
			self.readingtitle=0
	
	def gettitle(self):
		return self.title

fd=open(sys.argv[1])
tp=TitleParser()
tp.feed(fd.read())
print 'Title is:',tp.gettitle()
tp.close()

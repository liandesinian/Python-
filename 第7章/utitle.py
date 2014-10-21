#!/usr/bin/env python

from htmlentitydefs import entitydefs
from HTMLParser import HTMLParser
import sys,re

class TitleParser(HTMLParser):
	def __init__(self):
		self.taglevels=[]
		self.handledtags=['title','ul','li']
		self.processing=None
		HTMLParser.__init__(self)
	
	def handle_starttag(self,tag,attrs):
		if len(self.taglevels) and self.taglevels[-1]==tag:
			#Processing a previous version of this tag.Close it out 
			#and then start a new on this one
			self.handle_endtag(tag)
	
		#Note that we're now processing this tag
		self.taglevels.append(tag)
		
		if tag in self.handledtags:
			self.data=''
			self.processing=tag
			if tag=='ul':
				print 'List started.'
	def handle_data(self,data):
		if self.processing:
			self.data+=data
	
	def handle_endtag(self,tag):
		if not tag in self.taglevels:
			return
		while len(self.taglevels):
			starttag=self.taglevels.pop()

			if starttag in self.handledtags:
				self.finishprocessing(starttag)
			if starttag==tag:
				break
	def cleanse(self):
		self.data=re.sub('\s+',' ',self.data)

	def finishprocessing(self,tag):
		self.cleanse()
		if tag=='title' and tag==self.processing:
			print 'Document Title:',self.data
		elif tag=='ul':
			print 'List ended.'
		elif tag=='li' and tag==self.processing:
			print 'List item:',self.data

		self.processing=None

	def handle_entityref(self,name):
		if entitydefs.has_key(name):
			self.handle_data(entitydefs[name])
		else:
			self.handle_data('&'+name+';')
	
	def handle_charref(self,name):
		try:
			charnum=int(name)
		except ValueError:
			return

		if charnum<1 or charnum>255:
			return

		self.handle_data(chr(charnum))
	
	def gettitle(self):
		return self.title

fd=open(sys.argv[1])
tp=TitleParser()
tp.feed(fd.read())

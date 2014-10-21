#!/usr/bin/env python

from socket import *
import sys,select

HOST='localhost'
PORT=51234
ADDR=(HOST,PORT)

spinsize=10
spinpos=0
spindir=1

def spin():
	global spinsize,spinpos,spindir
	spinstr='.'*spinpos+'|'+'.'*(spinsize-spinpos-1)
	sys.stdout.write('\r'+spinstr+' ')
	sys.stdout.flush()

	spinpos+=spindir
	if spinpos<0:
		spindir=1
		spinpos=1
	elif spinpos>=spinsize:
		spinpos-=2
		spindir=-1

s=socket(AF_INET,SOCK_STREAM)
s.connect(ADDR)
p=select.poll()
p.register(s.fileno(),select.POLLIN|select.POLLERR|select.POLLHUP)#对这些事情使用poll，对到来的数据感兴趣
while True:
	results=p.poll(50)#表示等待50毫秒后可能会发生某件事情，若什么都没有发生，则p.poll()返回一个空的列表
	if len(results):
		if results[0][1]==select.POLLIN:
			data=s.recv(4096)
			if not len(data):
				print ('\rRemote end closed connection;exiting.')
				break
			sys.stdout.write('\rReceived: '+data)
			sys.stdout.flush()
		else:
			print '\rProblem occurred;exiting'
			sys.exit(0)

	spin()

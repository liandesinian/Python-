#!/usr/bin/env python

from socket import *
import sys

HOST='localhost'
PORT=51234
ADDR=(HOST, PORT)
BUF=1024

data='x'*10485760  #10M of data

client=socket(AF_INET, SOCK_STREAM)
client.connect(ADDR)

byteswritten=0
while byteswritten<len(data):
    startpos=byteswritten
    endpos=min(byteswritten+1024, len(data))
    byteswritten+=client.send(data[startpos:endpos])
    sys.stdout.write('Wrote %d bytes\n'%byteswritten)
    sys.stdout.flush()
    
client.shutdown(1)

print 'All data sent..'
while True:
    buf=client.recv(BUF)
    if not buf:
        break
    sys.stdout.write(buf)

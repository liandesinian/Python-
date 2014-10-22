#!/usr/bin/env python

from socket import *
import sys, time, traceback

HOST=''
PORT=51234
ADDR=(HOST, PORT)
BUF=1024

server=socket(AF_INET, SOCK_DGRAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(ADDR)

try:
    while True:
        print 'waiting for message...'
        data, addr=server.recvfrom(BUF)
        server.sendto('[%s] %s' %(time.ctime(), data), addr)
        print '..received from and returned to:', addr
except (KeyboardInterrupt, SystemExit):
    raise
except:
    traceback.print_exc()
finally:
    server.close()

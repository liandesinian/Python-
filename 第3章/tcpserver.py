#!/usr/bin/env python

from socket import *
import sys, time, traceback

HOST=''
PORT=51234
ADDR=(HOST, PORT)
BUF=1024

server=socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(ADDR)
server.listen(1)

while True:
    print 'waiting for connection...'
    try:
        client, addr=server.accept()
        print 'connected from', addr
    
        while True:
            data=client.recv(BUF)
            if not data:
                break
            print data
            client.sendall('[%s] %s' %(time.ctime(), data))
            
    except (KeyboardInterrupt, SystemExit):
        raise
    except :
        traceback.print_exc()
    
    finally:
        client.close()
        
server.close()

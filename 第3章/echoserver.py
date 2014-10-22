#!/usr/bin/env python


from socket import *
import traceback

HOST=''
PORT=51234
ADDR=(HOST, PORT)
BUF=1024

server=socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(ADDR)
server.listen(1)

while True:
    try:
        client, addr=server.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
    
    try:
        print 'Got connection from', client.getpeername()
        
        while True:
            data=client.recv(BUF)
            if not data:
                break
            client.sendall(data)
        
        client.close()
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()

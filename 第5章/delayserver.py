#!/usr/bin/env python

from socket import *
import traceback,time

HOST=''
PORT=51234
ADDR=(HOST,PORT)

s=socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(1)

while True:
    try:
        client,addr=s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue

    try:
        print "Got connection from",client.getpeername()
        while True:
            try:
                client.sendall(time.asctime()+'\n')
            except:
                break
            time.sleep(5)
    except (KeyboardInterrupt,SystemExit):
        raise
    except:
        traceback.print_exc()

try:
    client.close()
except KeyboardInterrupt:
    raise
except:
    traceback.print_exc()


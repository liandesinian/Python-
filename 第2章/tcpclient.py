#!/usr/bin/env python

from socket import *
import traceback

HOST='localhost'
PORT=51234
ADDR=(HOST, PORT)
BUF=1024

client=socket(AF_INET, SOCK_STREAM)
client.connect(ADDR)
try:
    while True:
        data=raw_input("Please input data: ")
        if not data:
            break
        client.sendall(data)
        data=client.recv(BUF)
        if not data:
            break
        print data
except (KeyboardInterrupt, SystemExit):
    raise
except:
    traceback.print_exc()
finally:
    client.close()

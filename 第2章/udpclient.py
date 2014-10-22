#!/usr/bin/env python

from socket import *
import sys

HOST='localhost'
PORT=51234
ADDR=(HOST, PORT)
BUF=1024

client=socket(AF_INET, SOCK_DGRAM)

try:
    while True:
        data=raw_input('Please input your data: ')
        if not data:
            break
        client.sendto(data, ADDR)
        data, addr=client.recvfrom(BUF)
        if not data:
            break
        print data
except (KeyboardInterrupt, SystemExit):
    raise
except:
    traceback.print_exc()
finally:
    client.close()

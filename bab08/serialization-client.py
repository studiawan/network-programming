#!/usr/bin/env python

import socket
import time
import sys
import pickle

def now():
    return time.asctime(time.localtime(time.time()))

# building socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 5001))

while 1: 
    # infinite send pickled message
    try:
        # arranging message
        msg = []
        msg.append("Hi Server")
        msg.append(now())

        # pickling message
        msg = pickle.dumps(msg)

        s.send(msg)
        time.sleep(1)
    # exception        
    except(KeyboardInterrupt, SystemExit):
        sys.exit(0)

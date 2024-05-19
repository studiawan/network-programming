#!/usr/bin/env python

import socket
import time
import sys
import pickle
import json

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
        msg_dict = {
            'message': 'Hi Server',
            'timestamp': now()
        }

        # pickling message
        msg = pickle.dumps(msg)
        msg_dict = bytes(json.dumps(msg_dict), 'utf-8')

        # s.send(msg)
        s.send(msg_dict)
        time.sleep(1)
    # exception        
    except(KeyboardInterrupt, SystemExit):
        s.close()
        sys.exit(0)

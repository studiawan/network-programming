#!/usr/bin/env python

import socket
import pickle
import sys
import json

# some definitions
SIZE = 1024

# building socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 5001))
s.listen(5)

while 1:
    try:
        # receive connected client
        client, client_address = s.accept()

        # receive client message
        while 1:
            try:
                message = client.recv(SIZE)

                if not message:
                    break

                # unpickle message and print it
                # message = pickle.loads(message)
                message = message.decode('utf-8')
                message = json.loads(message)
                print(client_address, message)        
            except(KeyboardInterrupt, SystemExit):
                sys.exit(0)
    except(KeyboardInterrupt, SystemExit):
        sys.exit(0)


#!/usr/bin/env python
# client.py

import sys
import socket
import time


def main(elements):
    try:
        for e in elements:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            client.connect(('127.0.0.1', 5000))
            client.send(bytes(e, encoding='utf-8'))
            client.shutdown(socket.SHUT_RDWR)
            client.close()
            time.sleep(1)
    except Exception as msg:
        print(msg)


if __name__ == "__main__":
    main(sys.argv[1:])

#!/usr/bin/env python
# client.py

import sys
import socket


def main(elements):
    try:
        for e in elements:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = socket.gethostname()
            client.connect((host, 5000))
            client.send(bytes(e, encoding='utf-8'))
            client.shutdown(socket.SHUT_RDWR)
            client.close()
    except Exception as msg:
        print(msg)


if __name__ == "__main__":
    main(sys.argv[1:])

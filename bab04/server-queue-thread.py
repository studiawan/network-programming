#!/usr/bin/env python
# server.py

import socket
import select
import queue
from threading import Thread
from time import sleep
from random import randint
import sys


class ProcessThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True
        self.q = queue.Queue()

    def add(self, data):
        self.q.put(data)

    def stop(self):
        self.running = False

    def run(self):
        q = self.q
        while self.running:
            try:
                # block for 1 second only:
                value = q.get(block=True, timeout=1)
                process(value)
            except queue.Empty:
                sys.stdout.write('.')
                sys.stdout.flush()

        if not q.empty():
            print("Elements left in the queue:")
            while not q.empty():
                print(q.get())


t = ProcessThread()
t.start()


def process(value):
    """
    Implement this. Do something useful with the received data.
    """
    print(value)
    sleep(randint(1, 5))  # emulating processing time


def main():
    s = socket.socket()             # Create a socket object
    host = socket.gethostname()     # Get local machine name
    port = 5000                     # Reserve a port for your service.
    s.bind((host, port))            # Bind to the port
    print("Listening on port {p}...".format(p=port))

    s.listen(5)  # Now wait for client connection.
    while True:
        try:
            client, address = s.accept()
            ready = select.select([client, ], [], [], 2)
            if ready[0]:
                data = client.recv(4096)
                # print data
                t.add(data)
        except KeyboardInterrupt:
            print("Stop.")
            break
        except socket.error:
            print("Socket error!")
            break
    cleanup()


def cleanup():
    t.stop()
    t.join()


if __name__ == "__main__":
    main()

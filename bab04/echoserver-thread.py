#!/usr/bin/env python
# http://ilab.cs.byu.edu/python/threadingmodule.html

import select
import socket
import sys
import threading


class Server:
    def __init__(self):
        # self.host = '10.211.55.2'
        self.host = '127.0.0.1'
        self.port = 5000
        self.backlog = 5
        self.size = 1024
        self.server = None
        self.threads = []

    def open_socket(self):        
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        
    def run(self):
        self.open_socket()
        input_list = [self.server, sys.stdin]
        running = 1
        while running:
            input_ready, _, _ = select.select(input_list, [], [])

            for s in input_ready:

                if s == self.server:
                    # handle the server socket
                    client_socket, client_address = self.server.accept()
                    c = Client(client_socket, client_address)
                    c.start()
                    self.threads.append(c)

                elif s == sys.stdin:
                    # handle standard input
                    _ = sys.stdin.readline()
                    running = 0

        # close all threads

        self.server.close()
        for c in self.threads:
            c.join()


class Client(threading.Thread):
    def __init__(self, client, address):
        threading.Thread.__init__(self)
        self.client = client
        self.address = address
        self.size = 1024

    def run(self):
        running = 1
        while running:
            try: 
                data = self.client.recv(self.size)
                print('received: ', self.address, data)
                if data:
                    self.client.send(data)
                else:
                    self.client.close()
                    running = 0
            except ConnectionResetError:
                print('Connection reset')


if __name__ == "__main__":
    server = Server()
    server.run()

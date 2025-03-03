import socket

class Client(object):
    def __init__(self) -> None:
        self.server_address = ('127.0.0.1', 5001)
        self.client_socket = None

    def connect(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.server_address)
        
        return self.client_socket
    
    def send(self) -> int:
        bytes_sent = self.client_socket.send(b'Hello network programming.')
        self.client_socket.close()

        return bytes_sent

if __name__ == '__main__':
    sender = Client()
    sender.connect()
    sender.send()

import socket

server_address = ('127.0.0.1', 5001)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect(server_address)

message = b'Hi ...'
client_socket.send(message)
recv_message = client_socket.recv(1024)
print(recv_message)

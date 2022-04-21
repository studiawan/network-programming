import socket

server_address = ('127.0.0.1', 5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = b'Hi ...'
client_socket.sendto(message, server_address)

recv_message, server_address = client_socket.recvfrom(1024) 
print(recv_message, server_address) 

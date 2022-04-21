import socket

server_address = ('127.0.0.1', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(server_address)

data, client_address = server_socket.recvfrom(1024)
server_socket.sendto(data, client_address)
print('data:', data, 'client address', client_address)
print('sock name', server_socket.getsockname())

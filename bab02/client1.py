import socket

# create socket and connect to server
server_address = ('localhost', 5001)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

# send string to server and close socket
client_socket.send(b'Hi ... ')
client_socket.close()

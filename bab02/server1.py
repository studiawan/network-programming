import socket

# define server address, create socket, bind, and listen
server_address = ('localhost', 5001)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1)

# accept client, receive its message and print
client_socket, client_address = server_socket.accept()
data = client_socket.recv(1024)
print(data)

# close socket client and socket client
client_socket.close()
server_socket.close()

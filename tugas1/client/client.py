import socket

def write_file(file_data, file_name):
    with open(file_name, 'w+') as f:
        f.write(file_data)


# create socket and connect to server
server_address = ('localhost', 5001)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

# send string to server and close socket
command = input()
client_socket.send(command.encode())

file_content = client_socket.recv(1024).decode()
print(file_content)

content = file_content.split("\n")

file_name = content[0].split()[1]
file_data = content[4]

#print("hasil: " + file_name + " dan " + file_data)
write_file(file_data, file_name)

client_socket.close()

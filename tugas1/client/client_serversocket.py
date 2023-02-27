import socket

def write_file(file_data, file_name):
    with open(file_name, 'wb+') as f:
        f.write(file_data)


# create socket and connect to server
server_address = ('localhost', 5001)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

# send string to server and close socket
command = input()
client_socket.send(command.encode())

# menerima files dari server (di loops biar nrima file lbh dr buffernya(1024))
file_content = ""
while True:
    data = client_socket.recv(1024).decode('iso-8859-1')
    if not data:
        break
    file_content += data

# melakukan parsing pada informasi yang diterima dari server
content = file_content.split("\n \n\n")

file_name = content[0].split()[1]
file_data = content[1]

# tampilkan header dan write files dari server
print("Header : \n{}".format(content[0]))
write_file(file_content.encode('iso-8859-1'), file_name)

client_socket.close()

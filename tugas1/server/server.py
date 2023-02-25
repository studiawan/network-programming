import socket
import sys
import os

def read_file(path_file):
    text = ""
    with open(path_file, 'r') as f:
        text = f.read()
    
    return text


# define server address, create socket, bind, and listen
server_address = ('localhost', 5001)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)

# infinite loop accepting client
try:
    while True:
        client_socket, client_address = server_socket.accept()
        print(client_socket, client_address)

        # receive data from client and print
        data = client_socket.recv(1024).decode()
        print(data)
        commands = data.split()
        file_name = ""
        
        if(commands[0] == "download"):
            file_name = commands[1]
            print(file_name)

            if (os.path.exists(file_name)):
                file_text = read_file(file_name)
                print(file_text)
                client_socket.send(file_text.encode())
        
        # close socket client
        client_socket.close()        

# if user press ctrl + c, close socket client and exit    
except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)

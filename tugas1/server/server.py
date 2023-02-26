import socket
import sys
import os

def read_file(path_file):
    text = b""
    with open(path_file, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            text += data
    
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
        
        # parsing command dari client
        commands = data.split()
        file_path = "files/"
        file_name = ""
        
        if(commands[0] == "download"):
            file_name = commands[1]
            file_path += commands[1]

            # cek apakah file yang diminta ada
            if (os.path.exists(file_path)):
                file_text = read_file(file_path)

                # membuat header lalu menambahkan isi file di bawahnya
                content = "file-name: {} ,\nfile-size: {} ,\n \n\n".format(file_name, os.path.getsize(file_path)).encode() 
                content += file_text

                # kirim ke client
                client_socket.sendall(content)
                print("file terkirim")

            else:
                print("file tidak ada")
        
        # close socket client
        client_socket.close()

# if user press ctrl + c, close socket client and exit    
except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)

import socket
import select
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
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(5)

input_socket = [server_socket]

# infinite loop accepting client
try:
    while True:
        # client_socket, client_address = server_socket.accept()
        read_ready, write_ready, exception = select.select(input_socket, [], [])
        # print(client_socket, client_address)


        for sock in read_ready:
            if sock == server_socket:
                client_socket, client_address = server_socket.accept()
                input_socket.append(client_socket)
            else:            	
                data = sock.recv(1024).decode()
                print(sock.getpeername(), data)
                if data:
                    commands = data.split()
                    file_path = "files/"
                    file_name = ""
                    
                    if(commands[0] == "download"):
                        file_name = commands[1]
                        file_path += commands[1]

                        if (os.path.exists(file_path)):
                            file_text = read_file(file_path)
                            #print(file_text)

                            content = "file-name: {} ,\nfile-size: {} ,\n \n\n".format(file_name, os.path.getsize(file_path)).encode() 
                            content += file_text

                            sock.sendall(content)
                # else:                    
                sock.close()
                input_socket.remove(sock)

# if user press ctrl + c, close socket client and exit    
except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)
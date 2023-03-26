import socket
import select
import sys
import configparser
import os

# Mengambil nilai HOST dan PORT dari file .conf
config = configparser.ConfigParser()
config.read('httpserver.conf')

server_address = (config.get('progjar_6', 'HOST'), config.getint('progjar_6', 'PORT'))
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(5)

input_socket = [server_socket]

try:
    while True:
        read_ready, write_ready, exception = select.select(input_socket, [], [])
        
        for sock in read_ready:
            if sock == server_socket:
                client_socket, client_address = server_socket.accept()
                input_socket.append(client_socket)                       
            
            else:                
                # receive data from client, break when null received          
                data = sock.recv(4096)
                print(client_address)
                print(client_socket)
                
                data = data.decode('utf-8')
                request_header = data.split('\r\n')
                request_file = request_header[0].split()[1]
                response_header = b''
                response_data = b''
                
                # Jika request file client '/', server akan membaca index.html lalu mengirimnya ke client dgn header kode 200 OK
                if request_file == 'index.html' or request_file == '/' or request_file == '/index.html':
                    f = open('index.html', 'r')
                    response_data = f.read()
                    f.close()
                    
                    content_length = len(response_data)
                    response_header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Length:' \
                                      + str(content_length) + '\r\n\r\n'

                    sock.sendall(response_header.encode('utf-8') + response_data.encode('utf-8'))


                else:
                    # Jika request file '/dataset', server melist isi dari folder dataset lalu menampilkannya dalam bentuk ul di html dgn href menuju masing2 req file
                    if request_file == '/dataset':
                        dir_contents = os.listdir('dataset')
                        response_data = '<html><body><ul>'
                        for content in dir_contents:
                            response_data += f'<li><a href="dataset/{content}">{content}</a></li>'
                        response_data += '</ul></body></html>'

                        content_length = len(response_data)
                        response_header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Length:' \
                                        + str(content_length) + '\r\n\r\n'

                        sock.sendall(response_header.encode('utf-8') + response_data.encode('utf-8'))

                    
                    # karakter awal request file('/') dihapus agar dapat mengakses filepath di dataset server, lalu meread file tsb pd dataset
                    elif os.path.exists(request_file[1:]):
                        f = open(request_file[1:], 'rb')
                        response_data = f.read()
                        f.close()
                        
                        content_length = len(response_data)
                        response_header = 'HTTP/1.1 200 OK\r\nContent-Type: multipart/form-data; charset=UTF-8\r\nContent-Length:' \
                                        + str(content_length) + '\r\n\r\n'

                        sock.sendall(response_header.encode('utf-8') + response_data)

                    # Jika req file lain, kirimkan 404.html dgn kode 404 Not Found
                    else:
                        f = open('404.html', 'r')
                        response_data = f.read()
                        f.close()

                        content_length = len(response_data)
                        response_header = 'HTTP/1.1 404 Not found\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Length:' \
                                        + str(content_length) + '\r\n\r\n'
                        sock.sendall(response_header.encode('utf-8') + response_data.encode('utf-8'))
                    
                    

except KeyboardInterrupt:        
    server_socket.close()
    sys.exit(0)

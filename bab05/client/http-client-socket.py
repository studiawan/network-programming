import socket

def write_file(file_data, file_name):
    with open(file_name, 'wb+') as f:
        f.write(file_data)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8000)
client_socket.connect(server_address)

command = input()
#client_socket.send(command.encode())

request_header = 'GET ' + command + ' HTTP/1.0\r\nHost: www.python.org\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/110.0\r\n\r\n'
client_socket.send(request_header.encode())

response = ''
while True:
    received = client_socket.recv(1024)
    if not received:
        break
    response += received.decode('iso-8859-1')

if '/dataset/' in command:
    content = response.split("\r\n\r\n", maxsplit=1)

    file_name = command[9:]
    file_data = content[1]
    write_file(file_data.encode('iso-8859-1'), file_name)
else:
    print(response)
    
client_socket.close()
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8000)
client_socket.connect(server_address)

request_header = b'GET / HTTP/1.0\r\nHost: www.python.org\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/110.0\r\n\r\n'
client_socket.send(request_header)

response = b''
while True:
    received = client_socket.recv(1024)
    if not received:
        break
    response += received.decode('utf-8')

print(response)
client_socket.close()
import socket

def get_first_length(data):
    header = data.split('\r\n\r\n')[0]
    header_length = len(header)
    for line in header.split('\r\n'):
        if line.lower().startswith('content-length:'):
            parts = line.split(':')
            if len(parts) == 2:
                try:
                    content_length = int(parts[1].strip())
                except ValueError:
                    return 0
    
    return header_length + int(content_length)  

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_address = ('www.python.org', 80)
server_address = ('localhost', 8080)
client_socket.connect(server_address)

# request_header = b'GET / HTTP/1.1\r\nHost: www.python.org\r\n\r\n'
request_header = b'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n'
client_socket.send(request_header)

response = ''
while True:
    received = client_socket.recv(1024)
    decoded_received = received.decode('utf-8')
    first_length = get_first_length(decoded_received)
    response += decoded_received

    if not received or first_length < 1024:
        break
    

print(response)
client_socket.close()

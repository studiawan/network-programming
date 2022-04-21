import socket

server_address = ('127.0.0.1', 5001)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect(server_address)

message = 'Hi ...'
delay = 1

while True:
    client_socket.send(message)
    client_socket.settimeout(delay)
    try:
        recv_message = client_socket.recv(1024)
        print recv_message, 'delay:', delay
    except socket.timeout:
        delay *= 2
        if delay > 2:
            print 'Server is down'        

    else:
        break

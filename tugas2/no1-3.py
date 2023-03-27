import socket
import ssl

target_host = "www.its.ac.id"
target_port = 443

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect the client_socket
client_socket.connect((target_host, target_port))

# ssl wrap the socket
context = ssl.create_default_context()
client_socket = context.wrap_socket(client_socket, server_hostname = target_host)

client_socket.send(b'GET / HTTP/1.1\r\nHost: www.its.ac.id\r\n\r\n')

response = ''
while True:
    received = client_socket.recv(4096)
    if not received:
        break
    response += received.decode('utf-8')

print("1. Status Code and Description:", response.splitlines()[0].partition(" ")[2])
print("2. Transfer-Encoding:", response.splitlines()[4].partition(" ")[2], "Vary:", response.splitlines()[10].partition(" ")[2])
print("3. HTTP Version:", response.splitlines()[0].partition(" ")[0])
# print(response)
print(response.splitlines()[0:15])
client_socket.close()

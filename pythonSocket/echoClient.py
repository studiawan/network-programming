# import socket module
import socket 
 
# creating socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# connect to server in defined address and port
client_socket.connect(('localhost', 5000))
 
# send message to server
client_socket.send("Hi server ... ")
 
# receive message from server, 1024 is buffer size in bytes
message = client_socket.recv(1024)
 
# print message
print "From server: " + message
 
# close socket client 
client_socket.close()
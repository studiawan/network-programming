# import socket module
import socket 
import pickle
 
# creating socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# connect to server in defined address and port
client_socket.connect(('localhost', 5000))
 
# send message to server
message = "Hi server ... "
message = pickle.dumps(message)
client_socket.send(message)
 
# receive message from server, 1024 is buffer size in bytes
message = client_socket.recv(1024)
message = pickle.loads(message)
 
# print message
print "From server: " + message
 
# close socket client 
client_socket.close()
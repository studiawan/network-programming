# import socket module
import socket
import sys 
 
# creating socket server object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# bind socket server to defined server address and port in tuple
server_socket.bind(('localhost', 5000))
 
# listening connection from client, only 1 backlog
server_socket.listen(1)
 
# infinite loop for receiving message from client
try: 
    while 1:
        # receiving client socket
        client_socket, client_address = server_socket.accept()
     
        # receive message from client, 1024 is buffer size in bytes
        message = client_socket.recv(1024)
        print "From client: " + message            
     
        # send message back to client
        client_socket.send(message)
        
        # close client socket
        client_socket.close()

# when user press CTRL + C (in Linux), close socket server and exit   
except KeyboardInterrupt:    
    server_socket.close()
    sys.exit(0)
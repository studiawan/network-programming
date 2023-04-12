import socket
import ssl
from bs4 import BeautifulSoup


# define hostname and ssl context
hostname = 'www.python.org'
context = ssl.create_default_context()

# create socket with ssl connection
with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())

        # prepare request header
        request_header = 'GET / HTTP/1.0\r\nHost: ' + hostname + '\r\n' +  '\r\n\r\n'
        request_header = request_header.encode()

        # make a request
        ssock.send(request_header)

        # receive response from server
        response = b'' 
        while True:
            received = ssock.recv(1024)
            if not received:
                break
            response += received
        
        # parse header and content    
        header, content = response.split(bytes('\r\n\r\n', 'utf-8'), 1)
        header = header.decode()
        soup = BeautifulSoup(content, features="lxml")

        # print header and content text
        print(header)
        print(soup.get_text())
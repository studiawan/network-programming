import socket
import ssl
import gzip
from io import BytesIO
from bs4 import BeautifulSoup

# Define hostname and SSL context
hostname = 'www.python.org'
context = ssl.create_default_context()

# Create an SSL socket connection
with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        # Prepare request header with HTTP/1.1 and necessary headers
        request_header = f"GET / HTTP/1.1\r\nHost: {hostname}\r\nAccept-Encoding: gzip\r\nConnection: close\r\n\r\n"
        ssock.send(request_header.encode())

        # Initialize buffer for response
        response = bytearray()
        try:
            while True:
                chunk = ssock.recv(1024)
                if not chunk:
                    break
                response += chunk
        except socket.timeout:
            print("Connection timed out")

        # Parse response into header and content
        header, _, content = response.partition(b'\r\n\r\n')

        # Decode and print headers
        header = header.decode()
        print(header)

        # Check if the content is gzip compressed
        if 'gzip' in header:
            buf = BytesIO(content)
            f = gzip.GzipFile(fileobj=buf)
            content = f.read()

        # Parse HTML content with BeautifulSoup
        soup = BeautifulSoup(content, 'lxml')
        print(soup.get_text())

import socket
import ssl
import gzip
import io


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
                return header_length + content_length
    return 0


# Define the client socket and wrap it with SSL for HTTPS
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context = ssl.create_default_context()
secure_socket = context.wrap_socket(client_socket, server_hostname='www.python.org')

server_address = ('www.python.org', 443)  # Use port 443 for HTTPS
secure_socket.connect(server_address)

request_header = (
    b'GET / HTTP/1.1\r\n'
    b'Host: www.python.org\r\n'
    b'Accept-Encoding: identity\r\n'
    b'Connection: close\r\n'
    b'\r\n'
)
secure_socket.send(request_header)

# Set a timeout to prevent hanging
secure_socket.settimeout(5)

response = b''
while True:
    try:
        received = secure_socket.recv(4096)
        if not received:
            break
        response += received
    except socket.timeout:
        print("Socket timed out.")
        break

# Split headers and body
header, body = response.split(b'\r\n\r\n', 1)
header = header.decode('utf-8')
header_lower = header.lower()

# Check for Transfer-Encoding: chunked (case-insensitive)
if 'transfer-encoding: chunked' in header_lower:
    chunks = []
    while True:
        try:
            size_line, rest = body.split(b'\r\n', 1)
            chunk_size = int(size_line, 16)
            if chunk_size == 0:
                break
            chunks.append(rest[:chunk_size])
            body = rest[chunk_size:].lstrip(b'\r\n')
        except ValueError:
            break
    body = b''.join(chunks)

# Handle gzip: check header (case-insensitive) OR magic bytes as fallback
is_gzip = 'content-encoding: gzip' in header_lower or body[:2] == b'\x1f\x8b'
if is_gzip:
    try:
        with gzip.GzipFile(fileobj=io.BytesIO(body)) as decompressed:
            body = decompressed.read()
    except Exception as e:
        print(f"Error decompressing gzip content: {e}")
        body = b''

try:
    print(body.decode('utf-8'))
except UnicodeDecodeError as e:
    print(f"Error decoding response body: {e}")

secure_socket.close()
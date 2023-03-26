import socket
import ssl
from bs4 import BeautifulSoup

target_host = "its.ac.id"
target_port = 443

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect the client_socket
client_socket.connect((target_host, target_port))

# ssl wrap the socket
context = ssl.create_default_context()
client_socket = context.wrap_socket(client_socket, server_hostname = target_host)

client_socket.send(b'GET / HTTP/1.0\r\nHost: its.ac.id\r\n\r\n')

# client_socket.send(f"GET /xyz/../service/ HTTP/1.1\r\nHost:{target_host}\r\n\r\n".encode())

response = ''
while True:
    received = client_socket.recv(4096)
    if not received:
        break
    response += received.decode('utf-8')

# print("1. Status Code and Description:", response.splitlines()[0].partition(" ")[2])
# print("2. Content-Encoding:", response.splitlines()[16].partition(" ")[2])
# print("3. HTTP Version:", response.splitlines()[0].partition(" ")[0])
# print("4. Content-Type (charset):", response.splitlines()[3].partition("=")[2])
# print(response)
print(response.splitlines()[0:15])

# menu_ul = soup.find('ul', {'class':'navbar-nav h-100 wdm-custom-menus links'})
menu_ul = response.partition('<ul class="navbar-nav h-100 wdm-custom-menus links">')[2].partition('</ul>')[0]
soup = BeautifulSoup(menu_ul, 'html.parser')

result = []
menu_li = soup.find_all('li')
for li in menu_li:
    a = li.find('a')
    if a:
        result.append(a.text.strip())
    div = li.find('div')
    a_content = div.find_all('a')
    for content in a_content:
        result.append('' + content.text.strip())

# print("5. Daftar Menu:")
# for index, element in enumerate(result):
#     if index == 1 or index == 2 or index == 4:
#         print(f"     {result[index]}")
#     else:
#         print(result[index])

# client_socket.close()

# receive some data
# response = b''
# while True:
#     data = client.recv(4096)
#     print(f'receiving {len(data)} bytes data...')
#     response += data
#     if not data:
#         client.close()
#         break

# http_response = repr(response.splitlines()[0])
# http_response = repr(response.splitlines())
# http_response_len = len(http_response)

# display the response
# print(f"http_response_len={http_response_len}\nhttp_response={http_response}")
import socket
import ssl
from bs4 import BeautifulSoup

target_host = "classroom.its.ac.id"
target_port = 443

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect the client_socket
client_socket.connect((target_host, target_port))

# ssl wrap the socket
context = ssl.create_default_context()
client_socket = context.wrap_socket(client_socket, server_hostname = target_host)

client_socket.send(b'GET / HTTP/1.0\r\nHost: classroom.its.ac.id\r\n\r\n')

response = ''
while True:
    received = client_socket.recv(4096)
    if not received:
        break
    response += received.decode('utf-8')

# print(response)
print("4. Content-Type (charset):", response.splitlines()[3].partition("=")[2])

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

print("5. Daftar Menu:")
for index, element in enumerate(result):
    if index == 1 or index == 2 or index == 4:
        print(f"     {result[index]}")
    else:
        print(result[index])

client_socket.close()

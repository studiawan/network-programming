import socket
from bs4 import BeautifulSoup

def write_file(file_data, file_name):
    with open(file_name, 'wb+') as f:
        f.write(file_data)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8000)
client_socket.connect(server_address)

command = input()
#client_socket.send(command.encode())

request_header = 'GET ' + command + ' HTTP/1.0\r\nHost: www.python.org\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/110.0\r\n\r\n'
client_socket.send(request_header.encode())

response = ''
while True:
    received = client_socket.recv(1024)
    if not received:
        break
    response += received.decode('iso-8859-1')

if '/dataset/' in command:
    content = response.split("\r\n\r\n", maxsplit=1)

    file_name = command[9:]
    file_data = content[1]
    write_file(file_data.encode('iso-8859-1'), file_name)
else:
    if '/dataset' in command:
        partisi = response.partition("<ul>")[2].partition("</ul>")[0]
        soup = BeautifulSoup(partisi, 'html.parser')

        menu_li = soup.get_text(" ").split(" ")
        for li in menu_li:
            print(li)
    else:
        print(response)

    # result = []
    # for li in menu_li:
    #     a = li.find('a')
    #     if a:
    #         result.append(a.text.strip())
    #     # div = li.find('div')
    #     # a_content = div.find_all('a')
    #     # a_content = div.find_all('a')
    #     for content in a:
    #         result.append('' + content.text.strip())
    
    
client_socket.close()
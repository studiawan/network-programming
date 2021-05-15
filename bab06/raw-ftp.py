import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 21))

commands = ['USER hudan\r\n', 'PASS 123\r\n', 'HELP\r\n', 'QUIT\r\n']
i = 1
while True:
    try:
        if i > len(commands):            
            msg = str(s.recv(1024))        
            print(msg.strip())
            break

        s.send(commands[i-1].encode('utf-8'))
        msg = str(s.recv(1024))        
        print(msg.strip())
        i += 1
                
    except socket.error:
        s.close()
        break

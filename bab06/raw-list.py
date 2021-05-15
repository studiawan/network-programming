import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 21))

commands = ['USER hudan\r\n', 'PASS 123\r\n', 'TYPE I\r\n', 'EPSV\r\n', 'MLSD\r\n', 'QUIT\r\n']
i = 1
while True:
    try:
        if i > len(commands):            
            msg = str(s.recv(4096))        
            print(msg.strip())
            s.close()
            break
        s.send(commands[i-1].encode('utf-8'))
        msg = str(s.recv(4096))
        print(msg.strip())

        if "Entering Extended Passive Mode" in msg:
            data_port = int(msg.strip().split('|||')[1].split('|')[0])
            data_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            data_sock.connect(('localhost', data_port))
            data = data_sock.recv(4096)
            print(data)
                    
        i += 1
                
    except socket.error:
        s.close()
        break

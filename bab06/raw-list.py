import socket

def create_socket(host, port=21):
    """ Create a socket and connect to the given host and port. """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

def recv_lines(sock):
    """ Receive lines from the server and decode them. """
    data = []
    while True:
        line = sock.recv(1024).decode('utf-8')
        if not line:
            break
        data.append(line)
        if line.endswith('\r\n'):
            break
    return ''.join(data)

def send_cmd(sock, cmd):
    """ Send a command to the FTP server. """
    sock.sendall(f"{cmd}\r\n".encode('utf-8'))
    return recv_lines(sock)

def main():
    host = 'localhost'  # Replace with your FTP server's IP address or hostname
    port = 21

    # Connect to FTP server
    ftp_socket = create_socket(host, port)
    print(recv_lines(ftp_socket))  # Print welcome message

    # Send username and password (use 'anonymous' and your email as password for anonymous access)
    print(send_cmd(ftp_socket, 'USER hudan'))  # Send USER command
    print(send_cmd(ftp_socket, 'PASS 123'))  # Send PASS command

    # Switch to Passive Mode
    pasv_mode = send_cmd(ftp_socket, 'PASV')
    print(pasv_mode)

    # Parse the passive mode response to get the IP and port
    ip_port = pasv_mode.split('(')[1].split(')')[0].split(',')
    ip_address = '.'.join(ip_port[:4])
    port = (int(ip_port[4]) * 256) + int(ip_port[5])

    # Connect to the data socket
    data_socket = create_socket(ip_address, port)
    
    # List files and directories in the current directory
    print(send_cmd(ftp_socket, 'LIST'))

    # Receive directory listing from data socket
    print(recv_lines(data_socket))
    data_socket.close()

    # Quit the session
    print(send_cmd(ftp_socket, 'QUIT'))
    ftp_socket.close()

if __name__ == "__main__":
    main()

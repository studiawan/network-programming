import socket

class FTP:
    def __init__(self, host='', user='', passwd='', timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.timeout = timeout
        self.sock = None
        self.file = None

    def connect(self):
        self.sock = socket.create_connection((self.host, 21), self.timeout)
        self.file = self.sock.makefile('r')
        self.getresp()

    def getresp(self):
        resp = self.file.readline()
        return resp

    def sendcmd(self, cmd):
        self.sock.sendall(cmd.encode('ascii') + b'\r\n')
        return self.getresp()

    def login(self):
        self.sendcmd(f'USER {self.user}')
        self.sendcmd(f'PASS {self.passwd}')

    def retrlines(self, cmd='LIST'):
        self.sendcmd('PASV')
        resp = self.getresp()
        start = resp.find('(') + 1
        end = resp.find(')', start)
        numbers = list(map(int, resp[start:end].split(',')))
        ip = '.'.join(map(str, numbers[:4]))
        port = (numbers[4] << 8) + numbers[5]

        data_sock = socket.create_connection((ip, port), self.timeout)
        self.sendcmd(cmd)
        data_file = data_sock.makefile('r')
        for line in data_file:
            print(line.strip())
        data_sock.close()
        self.getresp()

    def quit(self):
        self.sendcmd('QUIT')
        self.sock.close()
        self.file.close()

# Usage example
ftp = FTP('127.0.0.1', 'hudan', '123')
ftp.connect()
ftp.login()
ftp.retrlines()
ftp.quit()

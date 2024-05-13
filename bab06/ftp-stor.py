from ftplib import FTP

f = FTP('localhost') 
f.login('anonymous', '')

fd = open('icons.svg', 'rb')
f.storbinary('STOR icons.svg', fd)
fd.close() 

f.quit()



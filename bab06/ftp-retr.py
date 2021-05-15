from ftplib import FTP

f = FTP('localhost') 
f.login('hudan', '123')

fd = open('2019.pdf', 'wb')
f.retrbinary('RETR 2019.pdf', fd.write)
fd.close() 
f.quit()

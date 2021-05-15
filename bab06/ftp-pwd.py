from ftplib import FTP

f = FTP('localhost') 
print("Welcome:", f.getwelcome())

f.login('hudan', '123')
print("Current working directory:", f.pwd())
names = f.nlst()
print('List of directory: ', names)
f.quit() 

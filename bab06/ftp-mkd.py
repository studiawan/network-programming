from ftplib import FTP

# Specify the FTP server host
host = 'localhost'

# Create an FTP object and connect to the FTP server
ftp = FTP(host)

# Log in to the server with the default user (anonymous)
ftp.login('hudan', '123')

# Specify the name of the new directory to create
new_directory = '/new_folder'

# Create the new directory
try:
    result = ftp.mkd(new_directory)
    print(f"Directory created: {result}")
except Exception as e:
    print(f"Error: {e}")

# Properly close the connection
ftp.quit()

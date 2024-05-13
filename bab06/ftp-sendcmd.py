from ftplib import FTP

# Specify the FTP server host
host = 'localhost'

# Create an FTP object and connect to the FTP server
ftp = FTP(host)

# Log in to the server with the default user (anonymous)
ftp.login('hudan', '123')

# Send a custom command (e.g., 'FEAT' to list all features the server supports)
response = ftp.sendcmd('FEAT')

# Print the server's response to the 'FEAT' command
print("Server features:\n", response)

# Properly close the connection
ftp.quit()

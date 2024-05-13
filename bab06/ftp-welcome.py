from ftplib import FTP

# Specify the FTP server host
host = 'localhost'

# Create an FTP object and connect to the FTP server
ftp = FTP(host)

# Log in to the server with the default user (anonymous)
ftp.login('hudan', '123')

# Retrieve and print the welcome message from the FTP server
welcome_message = ftp.getwelcome()
print("Welcome message from the server:", welcome_message)

# Close the connection
ftp.quit()

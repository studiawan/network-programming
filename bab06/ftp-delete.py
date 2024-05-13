from ftplib import FTP

# Specify the FTP server host
host = 'localhost'

# Create an FTP object and connect to the FTP server
ftp = FTP(host)

# Log in to the server with the default user (anonymous)
ftp.login('hudan', '123')

# Specify the file name to be deleted
file_to_delete = 'unwantedfile.txt'

# Use delete to remove the file from the server
ftp.delete(file_to_delete)

# Print confirmation message
print(f"The file {file_to_delete} has been successfully deleted.")

# Properly close the connection
ftp.quit()

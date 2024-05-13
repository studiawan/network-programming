from ftplib import FTP

# Specify the FTP server host
host = 'localhost'

# Create an FTP object and connect to the FTP server
ftp = FTP(host)

# Log in to the server with the default user (anonymous)
ftp.login('hudan', '123')

# Specify the current file name and the new file name
old_file_name = 'upload.txt'
new_file_name = 'new-upload.txt'

# Use rename to change the file name on the server
ftp.rename(old_file_name, new_file_name)

# Print confirmation message
print(f"The file {old_file_name} has been renamed to {new_file_name}.")

# Properly close the connection
ftp.quit()

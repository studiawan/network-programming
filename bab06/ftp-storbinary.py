from ftplib import FTP

# Specify the FTP server host
host = 'localhost'

# Create an FTP object and connect to the FTP server
ftp = FTP(host)

# Log in to the server with the default user (anonymous)
ftp.login('hudan', '123')

# Specify the local file name to upload
local_file = 'example.zip'

# Specify the remote file name under which to store the file
remote_file = 'uploaded_example.zip'

# Open the local file in binary read mode
with open(local_file, 'rb') as file:
    # Use storbinary to upload the file, including the command to start the transfer
    ftp.storbinary(f'STOR {remote_file}', file)

# Print completion message
print(f"File {local_file} has been uploaded successfully as {remote_file}.")

# Properly close the connection
ftp.quit()

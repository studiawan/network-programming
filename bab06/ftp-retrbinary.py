from ftplib import FTP

def handle_binary_data(data):
    """Callback function to write binary data to a local file."""
    with open('downloaded_file.zip', 'ab') as f:
        f.write(data)

# Specify the FTP server host
host = 'localhost'

# Create an FTP object and connect to the FTP server
ftp = FTP(host)

# Log in to the server with the default user (anonymous)
ftp.login('hudan', '123')

# Specify the name of the file you want to download
remote_file = 'example.zip'

# Open the local file for appending binary data
with open('downloaded_file.zip', 'wb') as f:
    # Use retrbinary to download the file
    ftp.retrbinary(f'RETR {remote_file}', handle_binary_data)

# Print completion message
print("File has been downloaded successfully.")

# Properly close the connection
ftp.quit()

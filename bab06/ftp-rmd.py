from ftplib import FTP

# Specify the FTP server host
host = 'localhost'

# Create an FTP object and connect to the FTP server
ftp = FTP(host)

# Log in to the server with the default user (anonymous)
ftp.login('hudan', '123')

# Specify the name of the directory to be removed
directory_to_remove = '/new_folder'

# Remove the directory
try:
    ftp.rmd(directory_to_remove)
    print(f"Directory '{directory_to_remove}' has been removed successfully.")
except Exception as e:
    print(f"Failed to remove directory: {e}")

# Properly close the connection
ftp.quit()

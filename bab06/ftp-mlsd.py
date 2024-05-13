from ftplib import FTP

# Specify the FTP server host
host = 'localhost'

# Create an FTP object and connect to the FTP server
ftp = FTP(host)

# Log in to the server with the default user (anonymous)
ftp.login('hudan', '123')

# Specify the directory to list, use '.' for current directory
directory = '.'

# Use mlsd to get detailed list of files in the specified directory
print(f"Contents of directory {directory}:")
for filename, facts in ftp.mlsd(directory):
    print(f"{filename}:")
    for fact_name, fact_value in facts.items():
        print(f"  {fact_name}: {fact_value}")

# Properly close the connection
ftp.quit()

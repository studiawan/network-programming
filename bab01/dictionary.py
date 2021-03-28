# declare dictionary
banner = {}

# fill dictionary
banner['os'] = 'Ubuntu Server 13.04'
banner['server'] = 'ProFTPd 1.3.4'
banner['up'] = 315.5
banner[200] = 'OK'

print(banner)

# iterate through dictionary
for key, value in banner.items():
    print(key, value)
    
# delete item based on key
del banner['up']
print(banner)
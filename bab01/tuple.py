# declaration without brackets
# elements are separated with comma
address = 'localhost', 80, 21

# declaration with brackets
server_address = ('localhost', 5000)

# access by index
print(server_address[0])

# access by iteration
for value in server_address:
  print(value)
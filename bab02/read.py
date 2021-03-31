# very simple way: open-read-close
f = open('client1.py', 'r')
data = f.read() 
print(data)
f.close()

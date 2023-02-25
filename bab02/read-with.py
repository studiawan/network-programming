# read file without close, 'with' statement will close it for us :)
with open('client1.py', 'r') as f:
    text = f.read()
    print(text)

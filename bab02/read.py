# very simple way: open-read-close
f = open('textfile.txt', 'r')
data = f.read() 
f.close()
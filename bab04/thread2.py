# http://pymotw.com/2/threading/index.html
import threading


def worker():
    print('Worker')


threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

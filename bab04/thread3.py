# http://pymotw.com/2/threading/index.html
import threading


def worker(num):
    print('Worker: %s' % num)


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# http://pymotw.com/2/threading/index.html
import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s', )


class MyThread(threading.Thread):
    def run(self):
        logging.debug('running')        


for i in range(5):
    t = MyThread()
    t.start()

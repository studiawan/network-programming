import threading
from queue import Queue
import time

myQueue = Queue()


class CountStuff(threading.Thread):
    """
        A thread class that will count a number, sleep and output that number
    """
   
    def __init__(self, start_num, end, q):
        self.num = start_num
        self.end = end
        self.q = q        
        threading.Thread.__init__(self)
   
    def run(self):
        while True:
            if self.num != self.end:
                self.num += 1
                self.q.put(self.num)
                time.sleep(1)
            else:
                break
       
       
myThread = CountStuff(1, 5, myQueue)
myThread.start()

while True:
    if not myQueue.empty():
        val = myQueue.get()
        print("Outputting: ", val)
    else:
        break
    time.sleep(1)

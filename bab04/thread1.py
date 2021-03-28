# http://www.ibm.com/developerworks/aix/library/au-threadingpython/

import threading
import datetime


class ThreadClass(threading.Thread):
    def run(self):
        now = datetime.datetime.now()
        print("%s says Hello World at time: %s\n" % (self.getName(), now))


for i in range(5):
    t = ThreadClass()
    t.start()

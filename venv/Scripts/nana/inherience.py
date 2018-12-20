import threading
import time

#1.类需要继承自threading.Thread
class MyThread(threading.Thread):
    def __init__(self,arg):
        super(MyThread,self).__init__()
        self.arg = arg

        #2.必须重写run函数，run函数代表是真正的执行的功能
        def run(self):
            time.sleep(2)
            print("the args for this class is {0}".format(self))

for i in range(5):
    t = MyThread(i)
    t.start()
    t.join()

print("Main thread is done")
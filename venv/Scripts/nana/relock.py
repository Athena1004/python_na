import threading
import time

num = 0
mutex = threading.RLock()

class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if mutex.acquire(1):
            num += 1
            msg = self.name + "set num to" + str(num)
            print(msg)
            mutex.acquire()
            mutex.release()
            mutex.release()

def testTh():
    for i in range(5):
        print(i)
        t = MyThread()
        t.start()


if __name__ == "__main__":
    testTh()
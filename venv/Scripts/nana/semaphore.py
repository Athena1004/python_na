import threading
import time
semaphore = threading.Semaphore(3)

def func():
    if semaphore.acquire():
        for i in range(1,5):
            print(threading.current_thread().getName() + 'get semaphore')
        time.sleep(15)
        semaphore.release()
        print(threading.current_thread().getName() + 'release semaphore')

for i in range(1,8):
    t1 = threading.Thread(target=func,args = ())
    t1.start()
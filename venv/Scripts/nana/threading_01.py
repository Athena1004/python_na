#采用多线程 _thread
import time
import _thread as thread
def loop1():
    print("start loop 1 at:",time.ctime())
    time.sleep(4)
    print("end loop 1 at:", time.ctime())

def loop2():
    print("start loop 2 at:",time.ctime())
    time.sleep(2)
    print("end loop 2 at:", time.ctime())

def main():
    print("start at:", time.ctime())
    thread.start_new_thread(loop1,())
    thread.start_new_thread(loop2,())
    print("done at:", time.ctime())
if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)
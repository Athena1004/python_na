#线程常用属性
import time
import threading
def loop1():
    print("start loop 1 at:",time.ctime())
    time.sleep(4)
    print("end loop 1 at:", time.ctime())

def loop2():
    print("start loop 2 at:",time.ctime())
    time.sleep(2)
    print("end loop 2 at:", time.ctime())


def loop3():
    print("start loop 3 at:",time.ctime())
    time.sleep(2)
    print("end loop 3 at:", time.ctime())

def main():
    print("start at:", time.ctime())
    t1 =  threading.Thread(target = loop1,args = ())
    t1.setName("Th1")
    t1.start()

    t2 = threading.Thread(target=loop2, args=( ))
    t2.setName("Th2")
    t2.start()

    t3 = threading.Thread(target=loop3, args=( ))
    t3.setName("Th3")
    t3.start()
    time.sleep(3)


    for th in threading.enumerate():
        print("running thread is {0}".format(th.getName()))

    print("running thread num is {0}".format(threading.active_count()))
    print(" all done at:", time.ctime())
if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)
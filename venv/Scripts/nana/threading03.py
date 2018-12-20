import time
import threading

def loop1(in1):
    print("start loop 1 at:",time.ctime())
    print("我是参数",in1)
    time.sleep(4)
    print("end loop 1 at:", time.ctime())

def loop2(in1,in2):
    print("start loop 2 at:",time.ctime())
    print("我是参数", in1,"和参数 ", in2)
    time.sleep(2)
    print("end loop 2 at:", time.ctime())

def main():
    print("start at:", time.ctime())
    t1 = threading.Thread(target = loop1, args = ("aaa",))
    t1.start()

    t2 = threading.Thread(target=loop2, args=("bbb", "ccc"))
    t2.start()

    t1.join()
    t2.join()
    print(" all done at:", time.ctime())

if __name__ == '__main__':
    main()
    while True:#一定要有while语句。因为启动多线程后本程序就作为主线程存在,如果主线程执行完毕，则子线程可能也需要终止
        time.sleep(10)
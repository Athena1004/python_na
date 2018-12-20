#利用time，生成两个函数
#采用多线程  传参数
#练习带参数的多线程启动方法
import time
import _thread as thread
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
    thread.start_new_thread(loop1,("aaa",))
    thread.start_new_thread(loop2,("bbb","ccc"))
    print("done at:", time.ctime())
if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)
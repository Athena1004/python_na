#顺序执行，耗时长
import time
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
    loop1()
    loop2()
    print("done at:", time.ctime())
if __name__ == '__main__':
    main()
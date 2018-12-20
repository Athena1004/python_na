import threading
from time import sleep, ctime
loop = [4,2]

class Threadfunc:

    def __init__(self,name):
        self.name = name

    def loop(self, nloop, nsec): #nloop: loop的函数名称， nsec: 系统休眠时间
        print('start loop', nloop, "at", ctime())
        sleep(nsec)
        print('Done loop', nloop, "at", ctime())

def main():
    print("starting at :", ctime())
    t = Threadfunc("loop")
    t1 = threading.Thread( target = t.loop, args = ("loop1",4))
    t2 = threading.Thread(target=Threadfunc('loop').loop, args=("loop2", 2))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()

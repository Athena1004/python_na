import threading

sum = 0
loopsum = 0

lock = threading.Lock()

def myAdd():
    global sum, loopsum
    for i in range(1,loopsum):
        lock.acquire()         #给共享变量sum上锁
        sum += 1
        lock.release()           # 给共享变量sum解锁


def myMinus():
    global sum, loopsum
    for i in range(1, loopsum):
        lock.acquire()
        sum -= 1
        lock.release()


if __name__ == '__main__':
    print("starting----------{0}".format(sum))

    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinus, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done-----{0}".format(sum))

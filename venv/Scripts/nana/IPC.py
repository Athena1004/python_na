import multiprocessing
from time import sleep,ctime

def Clock(interval):
    while True:
        print("the time is %s"% ctime())
        sleep(interval)

if __name__ == "__main__":
    p = multiprocessing.Process(target=Clock,args=(3,))
    p.start()

    while True:
        print("sleeping.......")
        sleep(1)
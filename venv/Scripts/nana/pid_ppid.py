from multiprocessing import Process
import os
def info(title):
    print(title)
    print("module name:",__name__)
    print("parent process:",os.getpid())#父进程id
    print("process id:", os.getppid())#子进程id

def f(name):
    info("function f")
    print("hello",name)

if __name__ == "__main__":
    info("main line")
    p = Process(target=f,args=("Athena",))
    p.start()
    p.join()

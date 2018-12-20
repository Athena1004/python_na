import time
def printTime(f):
    def wrapper(*args, **kwargs):
        print("Time: ", time.ctime())
        return f(*args, **kwargs)
    return wrapper
@printTime
def hello():
    print("hello world")
hello()

def hello3():
    print("我是手动执行装饰器的")
hello3 = printTime(hello3)
hello3()

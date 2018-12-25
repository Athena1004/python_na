# __call__例子
class A():
    def __init__(self,name = 0):
        print("哈哈我被调用啦")

    def __call__(self):
        print("我被调用了again")
a = A()
a()

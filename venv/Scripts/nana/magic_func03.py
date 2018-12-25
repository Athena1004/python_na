#__str__举例

class A():
    def __init__(self,name = 0):
        print("哈哈我被调用啦")

    def __call__(self):
        print("我被调用了again")

    def __str__(self):
        return "随便举得例子啦啊啊啊"
a = A()
print(a)
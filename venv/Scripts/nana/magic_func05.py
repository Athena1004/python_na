#__setattr__例子
class Person():
    def __init__(self):
        pass

    def __setattr__(self, name,value):
        print("设置属性 ：{0}".format(name))

        #self.value = value 该语句会导致死循环
        super().__setattr__(name,value) #此种情况，为了避免死循环，规定统一调用父类魔法函数
p = Person()
print(p.__dict__)
p.addr = "suzhou"
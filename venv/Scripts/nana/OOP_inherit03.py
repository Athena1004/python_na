#多继承的例子
class Fish():
    def __init__(self,name):
        name = self.name
    def swim(self):
        print("swimming")

class Bird():
    def __init__(self,name):
        name = self.name
    def fly(self):
        print("flying")

class Person():
    def __init__(self,name):
        name = self.name
    def work(self):
        print("working")

class SuperMan(Person,Bird,Fish):
    def __init__(self,name):
        self.name = name


s = SuperMan("nana")
s.fly()
s.swim()
s.work()



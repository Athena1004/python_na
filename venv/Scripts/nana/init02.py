class Animal():
    def __init__(self):
        print("Animal~~~~~~~")


class Paxing(Animal):
    def __init__(self, name):
        print("paxing animal {0}".format(name))


class Dog(Paxing):
    def __init__(self):
        print("i am an init dog")


class Cat(Paxing):
    pass


kaka = Dog()
c = Cat("xiaobai")

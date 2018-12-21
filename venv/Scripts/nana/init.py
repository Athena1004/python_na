class Animal():
    def __init__(self):
        print("Animal~~~~~~~")

class Paxing(Animal):
    def __init__(self):
        print("paxing animal")

class Dog(Paxing):
    def __init__(self):
        print("i am an init dog")

class Cat(Paxing):
    pass

kaka = Dog()
c = Cat()


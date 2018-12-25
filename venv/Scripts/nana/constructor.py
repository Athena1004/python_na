class Person():
    def __init__(self,name):
        self.name = "Noname"
        self.age = 18
        self.addr = "suzhou"
        print(" in init func")
        print("name:{0}".format(name))

p = Person(name = "nana")
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("hi~~,my name is {0}".format(self.name))

#单继承例子
class Person():
    def __init__(self,name):
        name = self.name
    def work(self):
        print("working")

class Student(Person):
    def __init__(self,name):
        self.name = name
        print("i am a student {0}".format(name))

stu = Student("nana")
stu.work()
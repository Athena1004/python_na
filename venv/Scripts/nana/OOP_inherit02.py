#继承的语法
#在python中任何类都有一个共同的父类object

class Person():
    name = "Noname"
    age = 18
    _single = "yes"
    __score = None
    def sleep(self):
        print("i am sleeping")
    def work(self):
        print("make money")
#父类写在括号里
class Teacher(Person):
    teacher_id = "1234"
    name = "nana"
    def have_test(self):
        print("testing")
    def work(self):
       # Person.work(self)#为扩充父类的功能只需要调用父类相应的函数
        super().work()#super 代表得到父类
        self.have_test()

t = Teacher()
t.work()




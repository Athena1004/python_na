#继承的语法
#在python中任何类都有一个共同的父类object

class Person():
    name = "Noname"
    age = 18
    _single = "yes"
    __score = None
    def sleep(self):
        print("i am sleeping")
#父类写在括号里
class Teacher(Person):
    name = "nana"
    def have_test(self):
        print("testing")

t = Teacher()
print(t.name)
# print(t.single) # 私有成员
# print(t.score)




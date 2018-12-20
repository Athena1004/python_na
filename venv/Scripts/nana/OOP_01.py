
#定义一个学生类，用来形容学生
class Student():
    pass#pass 代表直接跳过，必须要有，一个空的类

#定义一个对象
nana = Student()

#定义一个类，用来描述学习python的学生
class PythonStudent():
    name = None    #用None给不确定的值赋值
    age = 22
    course = "python"


    #需要注意的是
    #1.def doHomework的缩进层级
    #2.系统会默认一个参数self
    def doHomework(self):
        print("I am doing homework")

        return None  #推荐在函数末尾使用return语句

#实例化对象
nanali = PythonStudent()
print(nanali.name)
print(nanali.age)
nanali.doHomework()

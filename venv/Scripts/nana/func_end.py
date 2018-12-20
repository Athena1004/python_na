def func_1():
    print("有返回值呀")
    return 1
def func_2():
    print("木有返回值")

f1 = func_1()
print(f1)
f2 = func_2()
print(f2)



def stu(name, age, *args):
    '''
    第一行
    第二行
    第三行
    :param name:
    :param age:
    :param args:
    :return:
    '''
    print("this is hanshu stu")
#help(stu)
stu.__doc__

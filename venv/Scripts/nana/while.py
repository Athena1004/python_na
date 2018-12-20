benqian = 1000000
year = 0
while benqian < 2000000:
    benqian = benqian * (1+0.067)
    year += 1
    print("第{0}年，有{1}本钱".format(year,benqian))



#九九乘法表
#version 1.0
for row in range(1,10):
    for col in range(1,row + 1):
        print(row * col, end = ' ')
    print('----------------')

#九九乘法表
#version 2.0
def print_line(row):
    for col in range(1,row + 1):
        print(row * col, end = ' ')
    print(" ")
for row in range (1,10):
    print_line(row)



#默认参数实例
def reg(name, age, gender = "male"):
    if gender == "male":
        print("{0} is {1}, and he is a good student".format(name,age))
    else:
        print("{0} is {1}, and she is a good student".format(name,age))
reg("lina",18,"female")

#关键字参数实例
def stu(name, age, addr):
    print("i am a student")
    print("my name is {0},i am {1} years old, i live in {2}".format(name,age,addr))

stu("lina",22,"changsha")

def stu1(name = "nomane", age = 0, addr = "no addr"):
    print("i am a student")
    print("my name is {0},i am {1} years old, i live in {2}".format(name,age,addr))

name1 = "nali"
age1 = 18
addr1 = "suzhou"
stu1(age = age1,name = name1, addr = addr1)

#收集参数实例
#函数模拟一个学生进行自我介绍，但具体内容不清楚
def stu(*args):
    print("hi ~~~~")
    print(type(args))
    for item in args:
        print(item)

stu("1111",18,"csu","single")
stu("22222222")
stu()

#收集参数关键字实例
def stu(**kwargs):
    print("hi dajaihaoya")
stu(name = "lina", age  = 19, addr = "csu", work = "student")

print("*" * 10)
stu(name = "Athena")

##
# def stu(name, age, *args, hobby = "no", **kwargs):
#     print("hihihhh")
#     print("my name is {0},我今年{1}岁".format(name,age))
#     if hobby == "no":
#         print("i don't have any hobbies")
#     else:
#         print("my hobby is {0}".format(hobby))
#
#     print("~" * 20)
#     for i in args:
#         print(i)
#
#     for k,v in kwargs:
#         print(k,'---',v)
#
# name = "lina"
# age = 22
#
# stu(name, age)
# stu(name, age, hobby = "dancing")
# stu(name, age, "666", "777", hobby = "singing", hobby1 = "love", hobby2 = "me")


def stu(*args):
    print("hahaha")
    print("00" * 20)
    n = 0
    for i in args:
        print(type(i))
        print(n)
        n += 1
        print(i)

l = ["lina",12,23,45]
stu(l)
stu(*l)

def stu(*args):
    print("hahaha")
    print("00" * 20)
    n = 0
    for i in args:
        print(type(i))
        print(n)
        n += 1
        print(i)

l = ["lina",12,23,45]
stu(l)
stu(*l)


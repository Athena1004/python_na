#菱形继承实例
class A():
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass

#构造函数的调用顺序
class A():
    pass
class B(A):
    def __init__(self):
        print("B")
class C(B):#此时查找C的构造函数，如果没有，则向上按照MRO顺序查找父类，直到找到为止
    pass

c = C()
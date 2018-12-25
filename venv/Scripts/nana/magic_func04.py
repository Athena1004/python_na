#__getattr__例子
class A():
    name = "Noname"
    age = 18

    def __getattr__(self, item):
        print("木有啦")
        print(item)

a = A()
print(a.name)
print(a.addr)
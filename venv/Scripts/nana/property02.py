#peroperty案例
# x = property(fget,fset,fdel,doc)
class Person():
    '''
    this is an doc for introducing peroperty
    '''
    def fget(self):
        return self._name * 2

    def fset(self,name):
        self._name = name.upper()#输入的姓名以大写保存

    def fdel(self):
        self._name = "Noname"

    name = property(fget, fset, fdel, "对name进行操作")

p1 = Person()
p1.name = "tuling"
print(p1.name)
#类的内置属性距离
print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__bases__)
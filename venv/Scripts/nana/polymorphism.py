#issubclass
class A():
    pass

class B(A):
    pass

class C():
    pass

print(issubclass(B,A))
print(issubclass(C,A))
print(issubclass(C,object))
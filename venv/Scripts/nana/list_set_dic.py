a1 = 100
def fun():
    print(a1)
    print("~" * 10)
    a2 = 1
    print(a2)
print(a1)


def fun():
    global b1
    b1 = 100
    print(b1)
    print("#" * 10)
    global b2
    b2 = 99
    print(b2)
# print(b1)
# print(b2)
fun()

x = 100
y = 200
z1 = x + y
z2 = exec("print('x + y:', x+y)")

print(z1)
print(z2 )


print("6"*20)
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(1))
print(fib(10))

print("="*40)

l = [1,2,3,4,5]
print(l[1])
print(l[1:3])
print(l[:])

print("="*100)
a = 100
b = 200
print(id(a))
print(id(b))
c = a
print(id(c))

a = 101
print(id(a))
print(id(c))

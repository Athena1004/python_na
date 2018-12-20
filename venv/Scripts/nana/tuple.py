t = ()
print(type(t))

t = (1,)
print(type(t))
print(t)

t = 1,
print(type(t))
print(t)

t = (1,2,3,4,5)
print(type(t))
print(t)

t = [1,2,3,4,5]
t1 = tuple(t)
print(type(t1))
print(t1)

t1 = (1,2,3)
t2 = (4,5,6)
t = t1 + t2
print(t)

print("="*20)
t0 = (1,2,3)
ta = t0 * 3
print(ta)

a = (1,2,"nana","i","love","money")
for i in a:
    print(i, end = " ")

print("="*20)
t = ((1,2,3),(4,5,6),(7,8,9))
for i in t:
    print(i)
for k,m,n in t:
    print(k,'---',m,'--',n,'-')

l = [1,2,3,4]
t = tuple(l)
print(t)


a = 1
b = 3
a,b = b,a
print(a)
print(b)
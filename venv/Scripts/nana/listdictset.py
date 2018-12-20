#汉诺塔
def hannuota(n,a,b,c):
    if n == 1:
        print(a,"-->",c)
        return None
    if n == 2:
        print(a,"-->",b)
        print(a, "-->", c)
        print(b, "-->", c)
        return
    else:
     #把n-1个盘子，从A塔借助于C塔，移到B塔
        hannuota(n-1,a,c,b)
        #把n-1个盘子，从B塔借助于A塔，移到C塔
        hannuota(n - 1, b, a, c)
a = "A"
b = "B"
c ="C"
n = 4
hannuota(n,a,b,c)

#list
a = [1,2,3,4,5]
del a[2]
print(a)


a = [1,2,3,4,5]
b = [6,7,8,9,0]
c = ['a','b','c','d','e']
d = a + b + c
print(d)

a = [1,2,3,4,5]
b = a * 3
print(b)

a = [1,2,3,4,5]
b = 7
c = b in a
print(c)

a = [1,2,3,4,5]
for i in a:
    print(i)

b = ["i have a lot of money"]
for i in b:
    print(b)

for i in range(1,10):
    print(i)


print("while" * 6)
#用while循环访问list   一般不用while遍历List
a = [1,2,3,4,5,6]
length = len(a)
index = 0
while index < length:
    print(a[index])
    index += 1

a = [["one",1], ["two",2], ["three",3]]
for k,v in a:
    print(k,"-----",v)


a = ['a','b','c']
b = [ i for i in a]
print(b)

a = ['a','b','c']
b = [ i * 10 for i in a]
print(b)


a = [x for x in range(1,35)]
b = [m for m in a if m % 2 == 0]
print(b)

a = [x for x in range(1,35)]
b = [x for x in range(1,35) if x %2 == 0]
print(b)

a = [x for x in range(1,10)]
print(len(a))
print(max(a))

l = "i love money"
print(list(l))

a = [1,2,3,4,5,6]
print(a.pop())
print(a)


a = [1,2,3,4,5,6]
print(a)
print(id(a))
a.clear()
print(a)
print(id(a))

a = [1,2,3,4,5,6]
print(a)
print(id(a))
a.reverse()
print(a)
print(id(a))


a = [1,2,3,4,5,6]
b = ['a','b']
print(a)
print(id(a))
a.extend(b)
print(a)
print(id(a))

print("#"*20)
a = [1,2,3,4,5,6]
a.append(8)
a.insert(1,8)
print(a)
a_len = a.count(8)
print(a_len)
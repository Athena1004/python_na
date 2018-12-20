s = set()
print(type(s))
print(s)

s = {1,2,3,4}
print(type(s))
print(s)
print("=" * 20 )
s1 = { }
print(type(s1))
print(s1)

s = {"lala","456",1,2,3}
print(s)
if 1 in s:
    print("cool")
else:
    print("bad")


s = {4,5,6,"i","love","money"}
for i in s:
    print(i , end = " ")

print("=" * 20 )
s = {(4,5,6),("i","love","money")}
for k,m,n in s:
    print(k,"---",m,"---",n,"---")
for i in s:
    print(i)


s1 = {1,1,2,3,4,1}
print(s1)
ss = {i for i in s1}
print(ss)

sss = {i for i in s1 if i %2 == 0}
print(sss)

s1 = {1,2,3,4}
s2 = {"i","love","money"}
s = {m * n for m in s2 for n in s1}
print(s)


s = {23, 3, 4, 5}
s.remove(4)
print(s)
s.discard(3)
print(s)

# s.remove(10)
# print(s)
#
# s.discard(10)
# print(s)
s.pop()
print(s)

print(" 0 " * 20)
s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9}
s3 = s1.intersection(s2)
print(s3)
s4 = s1.difference(s2)
print(s4)

s5 = s1.issubset(s2)
print(s5)

s = frozenset()
print(type(s))

d = {}
print(type(d))
print(d)

d1 = dict()
print(type(d1))
print(d1)

d = {"one":1, "two":2, "three":3}
print(d)

d = dict({"one":1, "two":2, "three":3})
print(d)

d = dict(one=1, two=2, three=3)
print(d)
print(d["one"])
del d["one"]
print(d)


d = {"one":1, "two":2, "three":3}
if 2 in d:
    print("value")
if "two" in d:
    print("key")
if ("two",2) in d:
    print("kv")


d = {"one":1, "two":2, "three":3}
for k in d:
    print(k,d[k])
for v in d.keys():
    print(v,d[k])
for m in d.values():
    print(m,d[k])
for k,v in d.items():
    print(k,"---",v)


d = {"one":1, "two":2, "three":3}
dd = {k:v for k,v in d.items()}
print(dd)
ddd = {k:v for k,v in d.items() if v %2 == 0}
print(ddd)

d = {"one":1, "two":2, "three":3}
print(str(d))

d = {"one":1, "two":2, "three":3}
i = d.items()
print(type(i))
print(i)

k = d.keys()
print(type(k))
v = d.values()
print(type(v))

print(d.get("thre",300))

l = ["eins","awei","drei"]
d = dict.fromkeys(l,"aaaa")
print(d)

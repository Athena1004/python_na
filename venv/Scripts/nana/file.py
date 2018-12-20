#打开文件
# f = open(r"1128.py","w")
# f.close()

# with语句
# with open(r"1128.py",'w') as f:
#     pass
# with open(r"./1128.py",'r') as f:
#     strline = f.readline()
#     while strline:
#         print(strline)
#         strline = f.readline()

# with open(r"./1128.py",'r') as f:
#     # l = list(f)
#     # for line in l:
#     #     print(line)
#     # strchar = f.read(1)
#     # print(len(strchar))
#     # print(strchar)
#     f.seek(4,0)
#     strChar = f.read()
#     print(strChar)

# with open(r"./1128.py",'r') as f:
#     strChar = f.read(3)
#     pos = f.tell()
#     while strChar:
#         print(pos)
#         print(strChar)
#         strChar = f.read(3)
#         pos = f.tell()

####写操作
# with open(r"1128.py", 'a') as f:
#     f.write(" ")
# l = ["i","love","wangxiaojing"]
# with open(r"1128.py", 'a') as f:
#     f.writelines(l)

# import pickle
# a = [19, 'my age is ', '666']
# with open(r"test01.txt",'wb') as f:
#     pickle.dump(a,f)
#
# with open(r"test01.txt",'rb') as f:
#     a = pickle.load(f)
#     print(a)
import shelve
shv = shelve.open(r'shelve.txt')
shv['one'] = 1
shv['two'] = 2
shv['three'] = 3
shv.close()

shv = shelve.open(r'shelve.txt')
print(shv['two'])
shv.close()
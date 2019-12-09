import sys
t = ('lmx',27,True,'中国广西')
print(t)
print(t[1])
print(t[3])
for i in t:
    print(i)
m = ('102',33,True,'哈萨克斯坦')
print(m)
print(sys.getsizeof(m))
print(list(m))
print(sys.getsizeof(list(m)))


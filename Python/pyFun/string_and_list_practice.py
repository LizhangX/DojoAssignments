
words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

y = ["hello",2,54,-2,7,12,98,"world"]

print y[0]
print y[-1]
z = [y[0],y[-1]]
print z


# ver1.0

a = [19,2,54,-2,7,12,98,32,10,-3,6]
a.sort()
print a
print len(a)/2
b = []
c = []
for i in range(0,len(a)/2):
    b.append(a[i])
# print b
# print c
c.append(b)
# print c
for i in range(0,len(a)/2 + 1):
    c.append(a[i + len(a)/2])

print c

#ver2.0
i = [19,2,54,-2,7,12,98,32,10,-3,6]
i.sort()
j = i[0:len(a)/2]
i = i[len(a)/2:len(a)]
i.insert(0, j)
print i


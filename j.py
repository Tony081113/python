#加入數字
a=[]
a.append([-1])
a[0].append(50)
a[0].append(-100)
a.append([-8])
a.append([70])
a[2].append(66)
#a[1].append(66)
print(a)
#最大最小
b=a[0][0]
c=a[0][0]
d=0
e=0
f=-1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
for i in range(len(a)):
    for n in range(len(a[i])):
        if b<a[i][n]:
            b=a[i][n]
        if c>a[i][n]:
            c=a[i][n]
        d+=a[i][n]
        e+=a[i][n]
        if f<a[i][n]:
            f=a[i][n]
    print('本樓的加總為',e)
    print('本樓的最大為',f)
    e=0
    f=-1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
print('最大為',b,'最小為',c)
print('總合為',d)

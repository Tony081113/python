import random
a=[]
b=[4,5,6,7,8,9,0,1,2,3]
bb=[]
c=[]
d=[]
for i in range(10):
    a.append(random.randint(1,30))
print(a)
for i in range(10):
    bb=[]
    for u in range(10):
        bb.append((a[u]+b[u])+1)
    c.append(min(bb))
    for y in range(10):
        d.append(b[y])
    b=[]
    for x in range(9):
        b.append(d[x+1])
    b.append(d[0])
    print(i+1,'b:',b)
    print(i+1,'bb:',bb)
    d=[]
print(min(c))
banner=c[0]
banner1=1
print(c)
for i in range(10):
    if banner>c[i]:
        banner=c[i]
        banner1=i+1
print('是在第',banner1,'行')
'''
for g in range(10):
one=None
two=None
three=None
Four=None
five=None
six=None
seven=None
eight=None
Nine=None
ten=None
'''

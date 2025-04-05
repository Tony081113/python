a='abcdefgh'
b='12345678'
c=int(input('輸入數字:'))
o=0
p=0
d=''
t=1
aa=0
bb=0
aaa=0
bbb=0
while o<len(a) or p<len(b):
    if c<=len(a):
        d=d+a[o:c]
    elif c>len(a):
        aa=1
        aaa+=(c/2)
        bb=1
        bbb+=(c/2)
        print(bbb)
        print(aaa)
        break
'''
if c<=len(b):
d=d+b[p:t]
elif c>len(b):
bb=1
bbb+=c
print(bbb)
break
'''
    o+=c
    p+=1
    t+=1
    c=c*2
    print(d)
if aa==1:
    d=d+a[aaa:(len(a)+1)]
    print('1')
if bb==1:
    d=d+b[bbb:]
    print('1')
print(d)

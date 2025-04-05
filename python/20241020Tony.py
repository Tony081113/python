a=[]
o=[]
oo=[]
b=str(input('輸入字串:'))
o.append(b[0])
oo.append(1)
c=str(input('輸入想找的字元:'))
d=''
for i in range(len(b)):
    for p in range(len(o)):
        if b[i]==o[p]:
            if p>len(oo):
                oo.append(1)
                print('12')
            else:
                print('123')
                l=oo.pop(p-1)
            p-=1
            l+=1
            oo.insert(p,l)
        else:
            o.append(b[i])
for i in range(len(b)):
    a.append(b[i])
'''
for i in range(len(a)):
    if len(c)>2:
        break
    if a[i]==c:
        d+=a[i]
'''
for i in range(len(oo)):
    oo[i]=oo[i]-1
print(o)
print(oo)

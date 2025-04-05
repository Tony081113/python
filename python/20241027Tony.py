a=[]#文字
aa=[]#有哪些類型的文字
aaa=[]#各種類型文字的數量
t=0
b=str(input('輸入字串:'))
bb=str(input('輸入想找的字元:'))
for i in range(len(b)):
    a.append(b[i])
while t!=10:
    for i in range(len(a)):
        if (a[i] in aa)==False:
            #print('ooo')
            aa.append(a[i])
            aaa.append(1)
            t=0
            #print(aaa)
        if a[i] in aa:
            for p in range(len(aa)):
                if a[i]==aa[p]:
                    o=aaa.pop(p)
                    o+=1
                    #print(o)
                    #print(aaa)
                    #print(p)
                    aaa.append(o)
                    p+=1
                    t+=1

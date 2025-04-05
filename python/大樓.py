a=[]
a.append([20,30])
for i in range(3):
    a.append([])
a.append([70])
a[4].append([])
a[4][1].append([8])
a[4][1].append([9])
a[4].insert(1,'ghst')
a.append(['麻辣火鍋'])
a[5].append([])
a[5][1].append([])
a[5][1].append([])
a[4][2].pop()
a[5][1].append([])
a[5][1].append([])
print(a)
aa=[]
for i in range(len(a)):
    aa.append(a[i])
for i in range(len(a)):
    aaa=aa[0][0]
    #if aa[i]==int:
    if aaa>aa[i]:
        aaa=aa
print(aaa)

s=input('請輸入英文句子:')
ss=s.split('.')
b=[]
a=['I','She','He','she','he','We','we','Ther','ther']
for i in range(len(ss)):
    for o in range(len(ss[i])):
        sss=ss[i].split(' ')
        for p in range(len(sss)):
            for u in range(len(a)):
                if sss[p] in a[u]:
                    b.append(sss[p])
print('主詞:',end='')
for i in range(len(b)):
    print(b)

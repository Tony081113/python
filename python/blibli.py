li2=[[200, 30, 30,200,200,200,200],
     [200, 30, 35,200,200, 40, 40],
     [210, 30, 40,210,200,200,200],
     [200,200,200,200, 40,200,200],
     [200,200,200,200, 50, 40,200]]
li1=[[1,-1],[1,-1]]
li3=[]
li4=[]
p=1
yao=0
y=0
for pp in range(1):
    for i in range(7):
        yao=0
        for r in range(2):
            for o in range(2):
                #li1沒問題
                a=li1[o+pp][r]*li2[r+pp][o+y]
                yao=int(yao+a)
                print(r,o,i)
        print(yao)
        li3.append(yao)
        p+=1
        y+=1
        yao=0
print(li3)
for i in range(5):
    if li3[i]<=45:
        print('直',end='  ')
    else:
        print('不直',end='  ')

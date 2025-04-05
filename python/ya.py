import copy
li1=[[0,-1,0],[-1,5,-1],[0,-1,0]]
li2=[[1,1,1,1,1,1,1,1],[1,8,9,1,1,10,11,1],[1,1,1,1,1,1,1,1],[1,-2,-6,1,1,20,10,1],[1,1,1,1,1,1,1,1]]
li3=copy.deepcopy(li2)
p=1
yao=0
y=0
for i in range(6):
    yao=0
    for r in range(3):
        for o in range(3):
            #li1沒問題
            a=li1[o][r]*li2[r][o+y]
            yao=int(yao+a)
            print(r,o,i)
    print(yao)
    li3[1][p]=yao
    p+=1
    y+=1
    yao=0
print(li3)

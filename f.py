import time
lm=[]
lmm=[]
hh=[]
t=int(time.time())
tt=int(time.time())
a=0
b=0
bc=0
ac=0
cc=0
while True:
    ac=str(input('fygjkildgnljnkelksjcutsndjifsvjrutgbhk:'))
    if ac=='@':
        bc=1
        cc=1
    if ac=='!':
        break
    if bc==0 and cc==0:
        lm.append(ac)
    elif bc==1 and cc==0:
        lmm.append(ac)
    else:
        cc=0
    print(lm,lmm)
for i in range(len(lmm)):
    if t!=tt:
        if a==0:
            hh.append(lm[i])
        else:
            hh.append(lmm[i])
print(hh)
print(lm,lmm)

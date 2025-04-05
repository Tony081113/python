print('Power down')
p=0
aa=0
bb=0
while True:
    a=str(input('輸入:'))
    if p==1 and a=='p'and aa==0:
        p=0
        print('Power down')
        bb=1
    if p==0 and a=='p'and bb==0:
        p=1
        print('Power up')
        aa=1
    if p==1:
        if len(a)==2:
            if a[1]=='o':
                print('已轉到00'+a[0]+'台')
        if len(a)==3:
            if a[2]=='o':
                print('已轉到0'+a[0]+a[1]+'台')
        if len(a)==4:
            if a[3]=='o':
                print('已轉到'+a[0]+a[1]+a[2]+'台')
        if len(a)>4:
            if a[-1]=='o':
                print('已轉到'+a[-4]+a[-3]+a[-2]+'台')
    aa=0
    bb=0

a=[]
ll=0
f=open('歡迎來到沒什麼屁用的資料系統.txt','r')
print('歡迎來到沒什麼屁用的資料系統')
print('---------------------------------------------------')
print('1.新增資料')
print('2.查詢')
print('3.列印')
print('---------------------------------------------------')
l=str(input('輸入你想使用的功能編號(數字,數字,還是數字):'))
while ll==0
    if (l.isdigit())==False:
        l=str(input('輸數字:'))
    else:
        ll=1
def new():
    b=str(input('輸入你要輸入的資料:'))
    print('輸入中......')
    c=str(len(a)+1)
    c=c+'.'
    c=c+b
    a.append(c)
    for i in range(100000000):
        pass
    print('輸入完畢')
def see():
    b=str(input('1.關鍵字\n2.編號查詢'))
    if b=='1':
        bb=str(input('輸入關鍵字:'))
        for i in range(len(a)):
            if bb in a[i]:
                print(a[i])
    if b=='2':
        bb=str(input('輸入編號:'))
        bb=int(bb)
        for i in range(len(a)):
            aa=a[i].split('.')
        for i in range(len(aa)):
            if isdigit(aa[i])

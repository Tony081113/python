import time as tt 
f=open('y點數紀錄','a')
ff=open('r點數紀錄','a')
while True:
    print('1.加點','\n','2.扣點','\n','3.退出系統')
    a=int(input('請輸入欲使用的編號(不要亂輸入不然會出錯):'))
    if a==1:
        print('1.孟儒','\n','2.孟昀')
        b=int(input('請輸入欲使用的人物編號(不要亂輸入不然會出錯):'))
        if b==1:
            c=str(input('請輸入欲加幾點:'))
            r=c
        if b==1:
            c=str(input('請輸入欲加幾點:'))
            y=c
    if a==2:
        print('1.孟儒','\n','2.孟昀')
        b=int(input('請輸入欲使用的人物編號(不要亂輸入不然會出錯):'))
        if b==1:
            c=str(input('請輸入欲扣幾點:'))
            rr=c
        if b==1:
            c=str(input('請輸入欲扣幾點:'))
            yy=c
    if a==3:
        break
    u = f.read()
print('退出成功')
tt.sleep(3)
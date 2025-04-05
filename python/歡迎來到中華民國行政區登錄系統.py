print('歡迎來到中華民國行政區登錄系統')
a=[]
def newadministrativedistrict():
    new=str(input('輸入你要新增的行政區名字:'))
    a.append([new])
def Addadministrativeregioninformation():
    log=None
    banner=0
    new1=str(input('輸入你要新增資料的行政區:'))
    for i in range(len(a)):
        if new1!=a[i]:
            banner=1
        log=i
    if banner==0:
        new=str(input('輸入你要新增的行政區資料:'))
        a[log].append(new)
    else:
        print('沒有這個行政區')
def Deleteborough():
    log=None
    banner=0
    new=str(input('輸入你要刪除的行政區:'))
    for i in range(len(a)):
        if new==a[i]:
            banner=0
        if new!=a[i]:
            banner=1
        log=i
    if banner==0:
        a.pop(log)
    else:
        print('沒有這個行政區')
def Readadministrativearea():
    print(a)
while True:
    print('-----------------------------------------------')
    print('1.新增行政區')
    print('2.新增行政區資料')
    print('3.刪除行政區')
    print('4.讀取行政區')
    print('5.退出系統')
    enter=str(input('輸入你要執行的程式(編號):'))
    print('-----------------------------------------------')
    if enter=='1':
        newadministrativedistrict()
    elif enter=='2':
        Addadministrativeregioninformation()
    elif enter=='3':
        Deleteborough()
    elif enter=='4':
        Readadministrativearea()
    elif enter=='5':
        break
    else:
        print('錯誤，請重新輸入')

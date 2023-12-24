while True:
    a=str(input('1.新增書籍','\n','2.刪除書籍','\n','3.搜書籍','\n','4.退出','\n','請輸入想執行的操作編號:'))
    dic1={'A':'科學','B':'數學','C':'電腦','D':'小說','E':'人文','F':'歷史'}
    dic2={}
    if a=='1':
        b=str(input('請輸入書名:'))
        c=str(input('請輸入區域編號:'))
        dic2[b]=c
    elif a=='2':
        b=str(input('請輸入書籍名稱:'))
        del dic2[b]
    elif a=='3':
        b=str(input('請輸入關鍵字:'))
        c=dic2.keys(b)
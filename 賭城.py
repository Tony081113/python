import random
a=int(input('請問閣下帶了多少代幣?\n'))
b=0
while True:
    if a<=0:
        print('你沒錢了')
        break
    print('本局開始!')
    print('你的錢剩',a,'塊')
    print('莊家正在骰數字......')
    b=random.randint(0,999)
    print('莊家的數字是',b)
    c=str(input('你要賭注嗎?\n'))
    if('不要' in c)==True:
        print('請等待下一局......')

    elif('要'in c)==True:
        e=0
        d=int(input('那麼你要賭注幾塊?\n'))
        if d>a:
            print('餘額不足!')
        print('正在決定你的數字......')
        f=random.randint(0,999)
        print('你的數字是',f)
        if f<b:
            print('你的數字小於莊家，你的代幣已被莊家收走')
            a-=d
            print('正在準備下一局......')
        else:
            print('你的數字大於莊家，你的代幣以成以兩倍')
            a+=d
            print('正在準備下一局......')
    else:
        print('請輸入文字')
        print('正在準備下一局......')

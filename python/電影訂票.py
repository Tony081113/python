'''
a=['x','x','x','x','x','x','x','x','x','x','x','x','x','x']
b=['x','x','x','x','x','x','x','x','x','x','x','x','x','x']
c=['x','x','x','x','x','x','x','x','x','x','x','x','x','x']
d=['x','x','x','x','x','x','x','x','x','x','x','x','x','x']
e=['x','x','x','x','x','x','x','x','x','x','x','x','x','x']
f=['x','x','x','x','x','x','x','x','x','x','x','x','x','x']
g=['x','x','x','x','x','x','x','x','x','x','x','x','x','x']
h=['x','x','x','x','x','x','x','x','x','x','x','x','x','x']
'''
a=[]
for i in range(8):
    a.append([])
    for p in range(14):
        a[i].append(0)
while True:
    iu=0
    print('  1 2 3  4 5 6 7 8 9 10 11  12 13 14')
    ac=64
    pp=0
    ppp=0
    for i in range(8):
        ppp=0
        if pp==1:
            print()
        ac+=1
        print(chr(ac),end='')
        pp=1
        for p in range(16):
            print(' ',end='')
            if ppp==3 or ppp==11 or ppp==10 or ppp==12 or ppp==13:
                print(' ',end='')
            if ppp==11:
                print(' ',end='')
            if ppp<=13:
                if a[i][ppp]==1:
                    print('x',end='')
                elif a[i][ppp]==0:
                    print('o',end='')
            ppp+=1
    print()
    use=str(input('傻子快輸入座位:'))
    use1=int(use[1:])-1
    use2=use[0]
    if ord(use2)>=97 and ord(use2)<=104:
            l=ord(use2)-97
    if ord(use2)>=65 and ord(use2)<=72:
            l=ord(use2)-65
    #l=chr(l)
    if (a[l][use1]==1 or (a[l][use1])==False)==False:
        a[l][use1]=1
    else:
        print('滾')
        iu=1
    if iu==0:
        print('搞定')
'''
print('A',ali[0],ali[1],ali[2],'',ali[3],ali[4],ali[5],ali[6],ali[7],ali[8],ali[9],'',ali[10],'','',ali[11],'',ali[12],'',ali[13])
print('B',bli[0],bli[1],bli[2],'',bli[3],bli[4],bli[5],bli[6],bli[7],bli[8],bli[9],'',bli[10],'','',bli[11],'',bli[12],'',bli[13])
print('C',cli[0],cli[1],cli[2],cli[3],cli[4],cli[5],cli[6],cli[7],cli[8],cli[9],cli[10],cli[11],cli[12],cli[13])
print('D',dli[0],bli[1],bli[2],'',bli[3],bli[4],bli[5],bli[6],bli[7],bli[8],bli[9],'',bli[10],'','',bli[11],'',bli[12],'',bli[13])
print('E',eli[0],ali[1],ali[2],'',ali[3],ali[4],ali[5],ali[6],ali[7],ali[8],ali[9],'',ali[10],'','',ali[11],'',ali[12],'',ali[13])
print('F',fli[0],bli[1],bli[2],'',bli[3],bli[4],bli[5],bli[6],bli[7],bli[8],bli[9],'',bli[10],'','',bli[11],'',bli[12],'',bli[13])
print('G',gli[0],ali[1],ali[2],'',ali[3],ali[4],ali[5],ali[6],ali[7],ali[8],ali[9],'',ali[10],'','',ali[11],'',ali[12],'',ali[13])
print('H',hli[0],bli[1],bli[2],'',bli[3],bli[4],bli[5],bli[6],bli[7],bli[8],bli[9],'',bli[10],'','',bli[11],'',bli[12],'',bli[13])
'''
'''
    if pp==0:
        pp+=1
    else:
'''

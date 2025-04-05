'''
s='123+4+6-89+5'
a=s.split('+')
print(a)
aa=a[0]
print(aa)
aaa=s
for i in range(1,9):
    aaa=aaa.split(str(i))
    print(str(aaa))
'''
'''
s='123+45-60+5'
#期望值:123,+,45,-
li=[]
i=0
while i<len(s):
    if s[i]=='+'or s[i]=='-':
        li.append(s[:i])
        li.append(s[i])
        s=s[i+1:]
        i+0
    print(li)
    if i==(len(s)-1):
        li.append(s)
    i+=1
    print(li)
print(li)
'''
'''
p=[]
def push(a):
    if len(p)<10:
        p.append(a)
        print('堆疊成功，還可裝',10-len(p),'個')
    else:
        print('箱子已滿')
def pop(a):
    if len(p)>0:
        print('已拿出',p[0])
        p.pop(p[0])
    else:
        print('箱子是空的')
while True:
    a=str(input('請輸入push或pop:'))
    if a=='push':
        a=int(input('請輸入數字:'))
        push(a)
    elif a=='pop':
        pop(a)
'''
s='123+45-60+5'
li=[]
#期望值:123,+,45,-
for i in range(len(s)):
    if s[i]!='+'and s[i]!='-'and s[i]!='6'and s[i]!='0':
        li.append(s[:i])
print(li)

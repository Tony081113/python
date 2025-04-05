import tkinter as tk
import random
from PIL import Image,ImageTk

win=tk.Tk()
win.geometry('700x600')
win.title('ya')
y=0
x=0
r=0
p=0
xx1=700
xx2=700
e=random.randint(120,170)

def key(event):
    global y,x,r,p
    if event.keycode==38 and r!=1 and r!=2:
        p=30
        r=1
    print(event.keycode)
#    elif event.keycode==40:
#        y-=1

lb=tk.Label(win,width=12,height=1,text='sbsbsbsbsbsb',bg='#FF0004',fg='#000000')
lb.place(x=610,y=600,anchor='sw')
cv=tk.Canvas(win,width=700,height=580)
cv.place(x=0,y=0)
win.bind('<Key>',key)
bgid=ImageTk.PhotoImage(image=Image.open('y5.png'))
cv.create_image(0,0,image=bgid)
peid=ImageTk.PhotoImage(image=Image.open('y1.png'))
peimg=cv.create_image(80,537,image=peid)
boid=ImageTk.PhotoImage(image=Image.open('boon.png'))
boimg=cv.create_image(700,493,image=boid)

while True:
    if e!=0:
        boimg1=cv.create_image(900,493,image=boid)
    if boimg:
        cv.delete(boimg)
    if boimg1:
        cv.delete(boimg1)
    if peimg:
        cv.delete(peimg)
    xx1-=2.5
    if e==0:
        xx2-=2.5
        boimg1=cv.create_image(xx2,493,image=boid)
    elif e!=0:
        e-=1
    if r==0:
        y=0
    elif r==1 and p!=0:
        p-=1
    elif p==0 and r==1:
        r=2
        p=29
    elif p==0 and r==2:
        r=0
    elif p!=0 and r==2:
        p-=1
    if r==1:
        y-=2.5
    elif r==2:
        y+=2.5
    if xx1==-10:
        xx1=700
    if xx2==-10:
        xx2=700
    print(y,xx1)
    boimg=cv.create_image(xx1,493,image=boid)
    peimg=cv.create_image(80,475+y,image=peid)
    if 80<=xx1<=(80+72) and (475+y)<=493<=(475+y+5):
        print('game over')
        break
    elif 80<=(xx1+183)<=(80+72) and (475+y)<=493<=(475+y+5):
        print('game over')
        break
    if 80<=xx2<=(80+72) and (475+y)<=493<=(475+y+5):
        print('game over')
        break
    elif 80<=(xx2+183)<=(80+72) and (475+y)<=493<=(475+y+5):
        print('game over')
        break
    win.after(1)
    win.update()
win.mainloop()
'''
    if xx1<80 and xx1>40:
        if 537+y<497 and 537+y>490:
            break
'''

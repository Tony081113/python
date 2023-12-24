import tkinter as tk
import time as t
sb=tk.Tk()
sb.title('我是大鍋，大鍋大鍋')
sb.geometry('400x400')
cleanboard1k=False
cleanboard2k=False
cleanboard3k=False
cleanboard4k=False
def cleanboard1():
    global cleanboard1k
    cleanboard1k=True
def cleanboard2():
    global cleanboard2k
    cleanboard2k=True
def cleanboard3():
    global cleanboard3k
    cleanboard3k=True
def cleanboard4():
    global cleanboard4k
    cleanboard4k=True
btl=tk.Button(sb,width=4,height=1,text='/',command=cleanboard1)
btl.place(x=200,y=30,anchor='nw')
bt=tk.Button(sb,width=4,height=1,text='*',command=cleanboard2)
bt.place(x=140,y=30,anchor='nw')
b=tk.Button(sb,width=4,height=1,text='-',command=cleanboard3)
b.place(x=80,y=30,anchor='nw')
bt11=tk.Button(sb,width=4,height=1,text='+',command=cleanboard4)
bt11.place(x=10,y=30,anchor='nw')
#sb.delete('all')
'''
btla=tk.Button(win,width=8,height=1,text='刪除',command=cleanboard)
btla.place(x=520,y=30,anchor='nw')
'''
while True:
    #t.sleep(0.5)
    #print(cleanboard1,'/n',cleanboard2,'/n',cleanboard3,'/n',cleanboard4)
    if cleanboard1==True or cleanboard2==True or cleanboard3==True or cleanboard4== True:
        sb.delete('btl')
        sb.delete('bt')
        sb.delete('b')
        sb.delete('bt11')
        cleanboard1=False
        cleanboard2=False
        cleanboard3=False
        cleanboard4=False
    sb.after(-9999999999999999999)
    sb.update()
sb.destroy()
sb.mainloop()

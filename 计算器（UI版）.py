from tkinter import*

#基本设置、变量命名
tk=Tk()
tk.title('计算器')
tk.resizable(width=False,height=False)
strprint=''
a,i=0,0
l=Label(tk,width=10,height=3,font=('Times',15),anchor='center')
l.grid(column=0)

#函数定义
def printnum(butnum):
    global strprint
    strprint+=butnum
    if strprint!='0':
        l.config(font=('Times',15),text=strprint)
    else:
        strprint=''

def space():
    global strprint
    strprint=''
    l.config(font=('Times',15),text=strprint)
	
def Is():
    global strprint
    try:
        strprint=eval(strprint)
        l.config(font=('Times',15),text=strprint)
        strprint=''
    except:
        pass

def button(i1,i2,i):
    Button(text=str(i),
		    command=lambda:printnum(str(i)),
			fg='green',font=('Times',25),width=5,
			activebackground='green').grid(row=i1,column=i2)

def back():
    global strprint
    strprint=list(strprint)
    del strprint[len(strprint)-1]
    strprint=''.join(strprint)
    l.config(font=('Times',15),text=strprint)

#计算器页面布局
for i1 in range(1,4):
    for i2 in range(0,3):
        i+=1
        button(i1,i2,i)
button(4,1,'0')
button(4,3,'.')
Button(text='back',command=back,font=('Times',25),width=5,activebackground='green',fg='green').grid(row=0,column=2)
Button(text='Space',
	command=space,
	font=('Times',25),width=5,activebackground='green',
	fg='green').grid(row=4,column=2)
Button(text='=',command=Is,font=('Times',25),width=5,activebackground='green',fg='green').grid(row=4,column=0)
for b in range(1,5):
    jc=['+','-','*','/']
    button(b-1,3,jc[b-1])

mainloop()

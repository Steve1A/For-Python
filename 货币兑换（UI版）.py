from tkinter import *
from tkinter import ttk
from threading import *
#页面布局
tk=Tk()
tk.title('货币兑换')
tk.resizable(width=False,height=False)
tk.geometry('400x50')

Label(tk,text='输入:').grid(row=0,column=0)
Label(tk,text='输出:').grid(row=1,column=0)
comva=('美元','泰铢','英镑')
comSome=StringVar()
combox=ttk.Combobox(tk,textvariable=comSome,state='readonly')
combox['values']=comva
combox.grid(row=0,column=1)
combox.current(0)

entry=Entry(tk)
entry.grid(row=0,column=2)

def printto():
    while True:
        if comva[0]==comva[0]:
            try:
                printnum=int(entry)
                printnum*=7
                Label(tk,text=printnum).grid(row=1,column=1)
            except:
                pass
        else:
            print('not')

thread=Thread(target=printto)
thread.setDaemon(True)
thread.start()

mainloop()
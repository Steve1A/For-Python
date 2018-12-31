from tkinter import *
import threading

#计算器类
class Calculator:
    def __init__(self):
    #------------变量定义------------
        self.output_string=''   #显示出的数字
        self.point=False        #数字是否有小数点
        self.get_number1=True   #number1是否需要获得
        self.number1=''         #存储得数，和第一个操作数
        self.operation=''       #存储运算符号
        self.number2=''         #存储第二个操作数
        self.memory_number=0    #额外功能memory的保存数
        self.touch=0            #在MRC按键中是否按了两次，即清零

    #------------屏幕基础设置------------
        self.tk = Tk()
        self.canvas = Canvas(self.tk)
        self.tk.title('计算器')
        self.tk.resizable(width=False, height=False)
        self.output = Label(self.tk,width=25, height=3, font=('Times', 15), anchor='center')           #基本数字显示
        self.output.grid(row=0, column=1, columnspan=3)
        self.M=Label(self.tk,width=5,height=3,font=('Times',15))                                       #memory功能显示
        self.M.grid(row=0,column=4)
        self.operation_output=Label(self.tk, width=5, height=3, font=('Times', 15), anchor='center')   #运算符号显示
        self.operation_output.grid(column=0, row=0)

    #------------按钮设置------------
        #四则运算
        self.default_butt_set(text='+',row=2,column=3,command=lambda :self.change_operation_output('+'))#default_butt_set在类结尾处定义，用于保存Button函数默认参数
        self.default_butt_set(text='-',row=3,column=3,command=lambda :self.change_operation_output('-'))
        self.default_butt_set(text='x',row=4,column=3,command=lambda :self.change_operation_output('x'))
        self.default_butt_set(text='÷',row=5,column=3,command=lambda :self.change_operation_output('÷'))
        #平方、根号
        self.default_butt_set(text='^',row=4,column=4,command=lambda :self.change_operation_output('^'))
        self.default_butt_set(text='√',row=3,column=4,command=lambda :self.change_operation_output('√'))
        #其他按钮设置
        self.default_butt_set(text='C',row=1,column=4,command=self.clear)                  #清零
        self.default_butt_set(text='back',row=2,column=4,command=self.back)                #回退
        self.default_butt_set(text='=',row=5,column=4,command=self.Is)                     #等于
        self.default_butt_set(text='M+',row=1,column=1,command=lambda :self.memory('+'))   #memory功能加法
        self.default_butt_set(text='M-',row=1,column=2,command=lambda :self.memory('-'))   #memory功能减法
        self.default_butt_set(text='MRC',row=1,column=0,command=lambda :self.memory('C'))  #memory功能显示和清除
        self.default_butt_set(text='MS',row=1,column=3,command=lambda :self.memory('S'))   #memory功能保存数字
        #数字按钮，因为通过for循环定义会出现问题，只能“硬调用”
        self.default_butt_set(text='1',row=2,column=0,command=lambda :self.change_output('1'))
        self.default_butt_set(text='2',row=2,column=1,command=lambda :self.change_output('2'))
        self.default_butt_set(text='3',row=2,column=2,command=lambda :self.change_output('3'))
        self.default_butt_set(text='4',row=3,column=0,command=lambda :self.change_output('4'))
        self.default_butt_set(text='5',row=3,column=1,command=lambda :self.change_output('5'))
        self.default_butt_set(text='6',row=3,column=2,command=lambda :self.change_output('6'))
        self.default_butt_set(text='7',row=4,column=0,command=lambda :self.change_output('7'))
        self.default_butt_set(text='8',row=4,column=1,command=lambda :self.change_output('8'))
        self.default_butt_set(text='9',row=4,column=2,command=lambda :self.change_output('9'))
        self.default_butt_set(text='.',row=5,column=0,command=lambda :self.change_output('.'))
        self.default_butt_set(text='0',row=5,column=1,command=lambda :self.change_output('0'))
        self.default_butt_set(text='00',row=5,column=2,command=lambda :self.change_output('00'))

    #------------通过多线程实现键盘输入检测------------
        self.thr=threading.Thread(target=lambda:self.canvas.bind_all('<Key>',self.auto))  #绑定方法auto实现在下“功能实现”中
        self.thr.setDaemon(True)
        self.thr.start()



    #------------修改数字输出------------
    def change_output(self,button_number):
        self.touch=0      #设置memory为0
        #确认输入不是小数点，大括号内逻辑：首先如果显示 为空，则输入不能为0即0不能为第一输入；或者已有显示数字
        if button_number != '.' and ((self.output_string=='' and button_number!='0') or self.output_string!=''):
            self.output_string += button_number
            #---既定流程---
            if self.get_number1==True:
                self.number1+=button_number
            else:
                self.number2+=button_number
            #---既定流程---

        # 如果输入有小数点，并且没有现在没有小数点，并且显示不为空即不能小数点为第一输入
        elif button_number == '.' and self.point == False and self.output_string!='':
            self.output_string += button_number   #保证没有小数点后将显示数字label添加数字
            #---既定流程---
            if self.get_number1==True:            #确定需要number1
                self.number1+=button_number       #则将number1添加数字
            else:
                self.number2+=button_number       #否则将number2添加数字
            #---既定流程---
            self.point = True                     #已有小数点

        #设置最长输入长度为28
        if len(self.output_string) <=28:
            self.output.config(text=self.output_string)      #将输出修改为新数字



    #------------计算部分------------
    #修改运算符号显示
    def change_operation_output(self,operation):
        self.touch=0
        try:
            self.Is()                                        #按下运算符号后应将现在已有的算式运算出结果
        except:
            pass                                             #出现错误属正常现象，不做处理
        self.operation=operation                             #将参数operation化为self属性，用于后续计算
        self.operation_output.config(text='%s'%operation)    #将显示计算符号label更新
        self.get_number1=False                               #按下运算符号说明number1已获取完毕，则设置为False
        self.output_string=''                                #number1获取完毕则清空显示，等待获取number2
    #实际运算方法
    def Is(self):
        #真正用于计算的列表，将number1、operation、number2排列在一起，方便后续检测
        self.real_operation=[str(self.number1),self.operation,self.number2]
        #列表中的第二位是计算符号，需要替换为python中的运算符
        if self.real_operation[1]=='^':                                                  #平方
            self.real_operation[self.real_operation.index(self.real_operation[1])]='**'
        elif self.real_operation[1]=='x':                                                #乘法（原来为字母‘x’）
            self.real_operation[self.real_operation.index(self.real_operation[1])]='*'
        elif self.real_operation[1]=='÷':                                                #除法（原来为unicode字符‘÷’）
            self.real_operation[self.real_operation.index(self.real_operation[1])]='/'
        elif self.real_operation[1]=='√':                                                #根号（特殊处理）
            self.real_operation[self.real_operation.index(self.real_operation[1])]='**'            #先替换为平方符号
            self.real_operation[self.real_operation.index(self.number2)]=str(1/float(self.number2))  #再将算式中的number2设置为1的number2分之一
        try:
            self.output.config(text=eval(''.join(self.real_operation)))    #尝试将显示修改为使用eval函数计算后的算式
        except:
            self.output.config(text='错误')                     #若用户输入算式有误，则输出为“错误”
        self.output_string=''                                  #将输出改为空等待获取第二个数据
        self.point=False                                       #设置小数点为False
        self.operation_output.config(text='')                  #修改输出
        self.number1=str(eval(''.join(self.real_operation)))   #再将number1改为得数
        self.number2=''



    #------------功能实现------------
    #清除
    def clear(self):             #实现非常简单，只需修改所有变量到初始值，并修改显示，但不修改memory
        self.touch=0
        self.output_string=''
        self.point=False
        self.get_number1=True
        self.number1=''
        self.operation=''
        self.number2=''
        self.operation_output.config(text='')
        self.output.config(text=self.output_string)
    #回退
    def back(self):
        self.touch=0
        if self.output_string!='':                                  #判定显示不为空，否则list out fo the range
            self.output_string=list(self.output_string)             #将输出的字符变为列表，方便删除
            if self.output_string[len(self.output_string)-1]=='.':  #先判定要删除的是否为小数点，如成立，则将point设为无
                self.point=False
            del self.output_string[-1]                              #删除列表最后一项（-1位为倒数第一项）
            self.output_string=''.join(self.output_string)          #连接列表并修改输出
            self.output.config(text=self.output_string)
    #输入数字
    def auto(self,event):   #event参数检测事件
        '''
        此处存在bug，若输入数字使用鼠标，小数点使用键盘会导致小数点无法输入，但发现windows自带计算器也有这个问题（windows7）
        经检验，当按以上操作时，键盘输入的keysym属性不为period，输出keysym时无法显示，暂无解决办法
        '''
        #暂时没有想到更优解，只好通过or语句连接所有数字keysym
        print(event.keysym)
        if event.keysym == '1' or event.keysym == '2' or event.keysym == '3' or event.keysym == '4' or event.keysym == '5' or event.keysym == '.' or event.keysym == '6' or event.keysym == '7' or event.keysym == '8' or event.keysym == '9' or event.keysym == '0':
            self.change_output(event.keysym)                     #调用change_output方法修改为keysym
        elif event.keysym == 'period'and self.point == False:   #如果为period即小数点，则修改为小数点，防止双小数点在change_output方法内实现
            self.change_output('.')
        elif event.keysym == 'BackSpace':                        #如果为BackSpace则为回退，调用back
            self.back()
        elif event.keysym=='Escape' or event.keysym=='Delete':   #如为Escape或Delete，调用清空方法
            self.clear()
        elif event.keysym=='Return':                             #如为Return则为回车，调用计算方法
            self.Is()
    #保存数字memory
    def memory(self,mode):        #设置mode参数确定为哪个按键，对应调用
        if mode=='+':             #如为+，则确定为M+调用
            self.touch=0
            try:
                self.Is()         #首先尝试计算结果
            except:
                pass
            self.memory_number+=float(self.number1)     #并执行加法操作

        elif mode=='-':          #如为-，则确定为M-调用
            self.touch=0
            try:
                self.Is()
            except:
                pass
            self.memory_number-=float(self.number1)     #并执行减法操作

        elif mode=='C' and self.touch==0:               #如为C，则确定为MRC调用
            self.output_string=str(self.memory_number)  #首先输出保存memory
            self.output.config(text=self.output_string) #更新
            if self.get_number1==True:                  #如果需要number1
                self.number1=str(self.memory_number)    #则修改number1为memory
            else:
                self.number2=str(self.memory_number)    #否则number2
            self.touch=1                                #修改按下次数为1

        elif mode=='C' and self.touch==1:               #如果为C并且已经按下一次，则清空memory
            self.memory_number=0
        elif mode=='S':                                 #如果为S则save保存现在显示为memory
            self.memory_number=float(self.output_string)

        if self.memory_number!=0:                       #实现“M”保存提示，如果memory不等于0说明已保存memory，则修改为M
            self.M.config(text='M')
        else:
            self.M.config(text='')                      #否则清空

    #因为tkinter中button的参数太多，定义一个皮包函数
    def default_butt_set(self,text,row,column,command,font=('Times',25),acbg='green',fg='green',width=5):
        button=Button(text=text,font=font,width=width,activebackground=acbg,fg=fg,command=command)
        button.grid(row=row,column=column)

#创建对象
calculator=Calculator()
mainloop()

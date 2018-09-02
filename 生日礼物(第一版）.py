from tkinter import*
import pygame
from threading import*
import pyautogui as pag
import time
from PIL import Image,ImageTk

TF=True
c=0
tk=Tk()
canvas=Canvas(tk,width=1500,heigh=1000)

def music():
    file='生日快乐 - 小蓓蕾组合.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(1)

def move():
    while TF:
        posget=pag.position()
        if posget[0]>=1000 and posget[1]>=500 and posget[0]<=1175 and posget[1]<=610:
            pag.moveTo(200,550)
        time.sleep(0.6)

def thButton():
    thr2=Thread(target=move)
    thr2.setDaemon(True)
    thr2.start()
    canvas.delete('all')
    thread=Thread(target=music)
    thread.setDaemon(True)
    thread.start()
    def photo():
        global c
        c+=1
        try:
            pho=Image.open('%s.jpg'%(c))
            pho.thumbnail((1300,1000))
            img=ImageTk.PhotoImage(image=pho)
            limg=Label(tk,image=img)
            limg.place(x=0,y=0)
        except:
            pass
        Button(text='下一张',command=(photo),font=('Times',15)).place(x=1350,y=300)
        canvas.mainloop()
        global TF
        TF=False
    Button(text='惊喜', bg='yellow', font=('Times', 25), command=(photo)).place(x=1000, y=500)

canvas.create_text(240, 235, text='寻找开启按钮', fill='red', font=('Times', 30))
button=Button(command=(thButton),text='Open!').place(x=1000,y=600)
canvas.pack()
canvas.mainloop()
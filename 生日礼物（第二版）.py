from tkinter import *
from PIL import Image,ImageTk
from threading import *
import pyautogui as pag
import pygame
import time

p=0
TF=True
tk=Tk()
canvas=Canvas(tk,width=2000,height=1000)
canvas.pack()

def music():
    while True:
        pygame.mixer.init()
        pygame.mixer.music.load('生日快乐 - 小蓓蕾组合.mp3')
        pygame.mixer.music.play()
        time.sleep(115)

def move():
    global TF
    while TF:
        mou1,mou2=pag.position()
        if mou1>=799 and mou2>=522 and mou1<=930 and mou2<=606:
            pag.moveTo(300,500)
            time.sleep(1)
def thButton():
    thr1=Thread(target=move)
    thr1.setDaemon(True)
    thr1.start()
    thr2=Thread(target=music)
    thr2.setDaemon(True)
    thr2.start()
    canvas.create_text(850, 200, text='Happy Birthday To You!', font=('Times', 50), fill='red')
    canvas.create_text(870, 260, text='祝老爹生日快乐！', font=('Times', 50), fill='yellow')
    def photo():
        global TF
        TF=False
        global p
        p+=1
        try:
            pho=Image.open('%s.jpg'%(p))
            pho.thumbnail((1300,1000))
            img=ImageTk.PhotoImage(image=pho)
            Label(tk,image=img).place(x=0,y=0)
            Button(text='下一张',font=('Times',20),command=photo).place(x=1400,y=300)
            canvas.mainloop()
        except:
            pass
    Button(text='惊喜!',bg='red',command=photo,font=('Times',30)).place(x=800,y=500)

Button(text='Open!',command=thButton).place(x=800,y=400)
canvas.mainloop()
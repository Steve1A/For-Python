from tkinter import*
import random
tk=Tk()
canvas=Canvas(tk,width=500,height=500)
canvas.pack()

colors=('green','blue','orange','pink','purple')
i=random.randint(50,100)
for x in range(0,i):
    x1=random.randrange(500)
    x2=x1+random.randrange(500)
    x3=random.randrange(500)
    y1=random.randrange(500)
    y2=y1+random.randrange(500)
    y3=random.randrange(500)
    ran_col=random.choice(colors)
    canvas.create_polygon(x1,y1,x2,y2,x3,y3,fill=ran_col,outline='')

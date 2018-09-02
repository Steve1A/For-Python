from tkinter import*
import random
tk=Tk()
canvas=Canvas(tk,width=500,height=500)
canvas.pack()

def rectangle(width,height,fill_color):
	x1=random.randrange(width)
	x2=x1+random.randrange(width)
	y1=random.randrange(height)
	y2=y1+random.randrange(height)
	canvas.create_rectangle(x1,x2,y1,y2,fill=fill_color)

rectangle(400,400,'green')
rectangle(400,400,'red')
rectangle(400,400,'blue')
rectangle(400,400,'orange')
rectangle(400,400,'yellow')
rectangle(400,400,'pink')
rectangle(400,400,'purple')
rectangle(400,400,'violet')
rectangle(400,400,'magenta')
rectangle(400,400,'cyan')

tk.mainloop()
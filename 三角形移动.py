from tkinter import*
tk=Tk()
canvas=Canvas(tk,width=400,height=400)
canvas.pack()
x=canvas.create_polygon(10,10,10,60,50,35)
tk.mainloop()
def move(event):
    if event.keysym=='Up':
        canvas.move(x,0,-9)
    elif event.keysym=='Down':
        canvas.move(x,0,9)
    elif event.keysym=='Left':
        canvas.move(x,-9,0)
    else:
        canvas.move(x,9,0)
canvas.bind_all('<KeyPress-Up>',move)
canvas.bind_all('<KeyPress-Down>',move)
canvas.bind_all('<KeyPress-Left>',move)
canvas.bind_all('<KeyPress-Right>',move)

input('按任意键退出')
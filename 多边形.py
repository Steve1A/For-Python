import turtle
t=turtle.Pen()
def star(size,points,color,around):
	x=360/points
	if color==True:
		t.begin_fill()
	for i in range(0,points):
		t.forward(size)
		t.left(180-x)
		t.forward(size)
		t.right(180-(x*2))
	if color==True:
		t.end_fill()
		t.color(0,0,0)
	if around==True:
		for i in range(0,points):
		       t.forward(size)
		       t.left(180-x)
		       t.forward(size)
		       t.right(180-(x*2))

t.reset()
t.color(1,0,0)
star(100,13,True,False)

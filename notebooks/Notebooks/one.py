import turtle 
p = turtle.Pen()
p.color('red','yellow')
p.speed(0)
p.begin_fill()
for var in range(200) : 
	p.forward(250)
	p.left(160)
p.end_fill()
turtle.exitonclick()
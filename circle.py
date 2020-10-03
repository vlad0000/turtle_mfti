import turtle

turtle.speed(4)
turtle.shape('turtle')
turtle.penup()
turtle.goto(390, 0)
turtle.left(90)
turtle.pendown()

for i in range(360):
    turtle.forward(3)
    turtle.left(1)
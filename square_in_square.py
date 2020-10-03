import turtle
turtle.speed(1)

def square(step):
    turtle.forward(step)
    turtle.left(90)
    turtle.forward(step)
    turtle.left(90)
    turtle.forward(step)
    turtle.left(90)
    turtle.forward(step)
    turtle.left(90)

step = 90
x = 0
y = 0

for i in range(10):
    square(step)
    step += 20
    turtle.penup()
    x += -30
    y += -10
    turtle.goto(x, y)
    turtle.pendown()
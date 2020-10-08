import math
import turtle

def draw_regular_poligons(n, long_party):
    '''
    Функция рисует количество многоугольников
    :param n: int, - количество фигур
    :param long_party: int, - длинна стороны в пикселях
    :return: None
    '''
    parties = 3
    radius = 0
    position_x = radius
    position_y = 0
    turtle.left(45)
    for figure in range(n):
        angle = 360 / parties
        radius = long_party / (2 * math.sin(math.degrees(360) / (2 * parties)))
        position_x = radius
        turtle.penup()
        turtle.goto(position_x, position_y)
        turtle.pendown()
        for draw in range(parties):
            turtle.left(angle)
            turtle.forward(long_party)
        print(radius)
        parties += 1
        long_party += 10
        position_x = radius
        turtle.penup()
        turtle.goto(position_x, position_y)
        turtle.pendown()


draw_regular_poligons(7, 20)
input()
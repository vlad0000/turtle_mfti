import turtle
turtle.speed(10)
def spider (n, step=60):
    '''
    :param n: Колличество ног от 1 до 360 - целое число
    :param step: длинна ноги в пикселях - целое число
    :return: None
    '''
    angle = 360 / n
    for i in range(n):
        turtle.forward(step)
        turtle.backward(step)
        turtle.left(angle)
    return None


n = int(input('Количество лапок?(1 - 360)\n: '))
spider(n)
spider
input('Нажмите enter')
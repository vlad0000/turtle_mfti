import turtle

def draw_spiral(n=10, step=1, speed=6):
    '''
    Рисует спираль
    :param n: кольчество витков - целое число
    :param step: шаг в пикселях, размер витка(рекомендуемое значение от 1 - 5) - целое число
    :param speed: Скорость рисовки - целое число
    :return: None
    '''
    turtle.left(90)
    angle = 8
    count = 180 // angle
    for i in range(n * 2):
        for k in range(count):
            turtle.forward(step)
            turtle.left(angle)
        print(i, ': полукруг')
        step += 1
    return None
draw_spiral(12)



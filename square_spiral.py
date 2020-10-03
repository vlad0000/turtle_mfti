import turtle

def draw_square_spiral(n=4, step=10, speed=6):
    '''
    Функция рисует квадратную спираль
    :param n: int, количество витков(по умолчанию 4)
    :param step: int, размер шага в пикселях(по умолчанию 10)
    :param speed: int, скорость курсора, от 0 - 10(по умолчанию 6)
    :return: None
    '''
    for turn in range(n*2):
        for half_loop in range(2):
            turtle.forward(step)
            turtle.left(90)
        step += 10

draw_square_spiral(15)
import turtle as t

t.speed(1)
t.left(90)

def draw_arch(step, angle):
    '''
    Функция рисует дугу
    :param step: длинна шага в пикселях
    :return: None
    '''
    for draw in range(20):
        t.forward(step)
        t.right(angle)
def draw_spring(n):
    '''
    Функция рисует пружину
    :param n: int, Длинная пружины в звеньях
    :return: None
    '''
    angle = 9
    step = 5
    smal_step = 1
    for spring in range(n):
        draw_arch(step, angle)
        draw_arch(smal_step, angle)
draw_spring(6)
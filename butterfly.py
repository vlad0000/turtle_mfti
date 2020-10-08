import turtle as t
t.speed(10)
t.left(90)
def wing(angle, step):
    '''
    Рисует крылья
    :return: None
    '''
    for left in range(int(360/angle)):
        t.left(angle)
        t.forward(step)
    for right in range(int(360/angle)):
        t.left(-angle)
        t.forward(step)

def draw_butterfly(n):
    '''
    Функция рисует бабочеку из "Восьмерок"
    :param n: int, - количество восьмерок(размер крыльев)
    :return: None
    '''
    angle = 10
    step = 5
    for draw in range(n):
        wing(angle, step)
        step += 1

draw_butterfly(10)
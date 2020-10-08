import turtle as t
def draw_flower(n=3):
    '''
    Функция рисует из "Восьмерок" цветок
    :param n: int, - количество лепистков, помноженное на 2(по умолчанию 3)
    :return: None
    '''
    t.speed(10)
    angle = 2

    for petal in range(n):
        for circles in range(2):
            for circle in range(180):
                t.left(angle)
                t.forward(2)
            angle = -angle
        t.left(120)


draw_flower()
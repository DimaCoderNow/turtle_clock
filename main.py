import time
import turtle

# Список сегментов для цифр
segments_list = [((6, 200), (28, 180), (106, 180), (128, 200)),
                 ((112, 175), (112, 118), (126, 105), (133, 112), (133, 194)),
                 ((125, 95), (133, 87), (133, 6), (112, 25), (112, 82)),
                 ((120, 100), (109, 90), (26, 90), (15, 100), (26, 110), (109, 110)),
                 ((2, 194), (23, 175), (23, 118), (9, 105), (2, 112)),
                 ((9, 95), (23, 82), (23, 25), (2, 6), (2, 87)),
                 ((6, 0), (28, 20), (106, 20), (128, 0)), ]
# Словарь содержащий индексы сегментов для создания цифры
digits_dict = {
    0: (0, 1, 2, 4, 5, 6),
    1: (1, 2),
    2: (0, 1, 3, 5, 6),
    3: (0, 1, 2, 3, 6),
    4: (1, 2, 3, 4),
    5: (0, 2, 3, 4, 6),
    6: (0, 2, 3, 4, 5, 6),
    7: (0, 1, 2, 4),
    8: (0, 1, 2, 3, 4, 5, 6),
    9: (0, 1, 2, 3, 4, 6),
}
turtle.mode("logo")
turtle.up()
turtle.bgcolor("#2B2B2B")
name_shape = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# создаем цифры из сегментов
for i in range(10):
    shape = turtle.Shape("compound")
    for j, segment in enumerate(segments_list):
        if j in digits_dict[i]:
            shape.addcomponent(segment, "#17F568", "green")
        else:
            shape.addcomponent(segment, "#0B2B0B")
    turtle.register_shape(name_shape[i], shape)
# Создаем точки для секунд
dot = ["none_dot", "dot"]
for i, color in enumerate(["#0B2B0B", "#17F568"]):
    dot_shape = turtle.Shape("compound")
    poly_1 = ((-10, 150), (10, 150), (10, 130), (-10, 130))
    poly_2 = ((-10, 50), (10, 50), (10, 70), (-10, 70))
    dot_shape.addcomponent(poly_1, color)
    dot_shape.addcomponent(poly_2, color)
    turtle.register_shape(dot[i], dot_shape)
# Создаем экземпляры черепашки для каждой из цифр на часах
clock_face = []
for i, coordinate in enumerate([(-170, 0), (-340, 0), (30, 0), (200, 0)]):
    clock_face.append(turtle.Turtle(shape="zero"))
    clock_face[i].up()
    clock_face[i].hideturtle()
    clock_face[i].setposition(coordinate)
    clock_face[i].showturtle()

# Пока для теста вывода
for i in name_shape:
    clock_face[2].shape(i)
    clock_face[0].shape(i)
    for j in range(10):
        clock_face[3].shape(name_shape[j])
        if j % 2:
            turtle.shape(dot[1])
        else:
            turtle.shape(dot[0])
            clock_face[1].shape(name_shape[j])
        time.sleep(1)


turtle.mainloop()

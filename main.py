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
                4: ( 1, 2, 3, 4),
                5: (0, 2, 3, 4, 6),
                6: (0, 2, 3, 4, 5, 6),
                7: (0, 1, 2, 4),
                8: (0, 1, 2, 3, 4, 5, 6),
                9: (0, 1, 2, 3, 4, 6),
}
turtle.mode("logo")
name_shape = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for i in range(10):
    shape = turtle.Shape("compound")
    for j, segment in enumerate(segments_list):
        if j in digits_dict[i]:
            shape.addcomponent(segment, "#17F568", "green")
    turtle.register_shape(name_shape[i], shape)


for _ in range(100):
    for i in name_shape:
        turtle.shape(i)
        time.sleep(1)


turtle.mainloop()
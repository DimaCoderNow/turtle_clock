import turtle


turtle.mode("logo")

# Список сегментов для цифр

segments_list = [((6, 200), (28, 180), (106, 180), (128, 200)),
                ((112, 175), (112, 118), (126, 105), (133, 112), (133, 194)),
                ((125, 95), (133, 87), (133, 6), (112, 25), (112, 82)),
                ((120, 100), (109, 90), (26, 90), (15, 100), (26, 110), (109, 110)),
                ((120, 100), (109, 90), (26, 90), (15, 100), (26, 110), (109, 110)),]

shape_sero = turtle.Shape("compound")
for i, segment in enumerate(segments_list):
    if i in (0, 1, 2):
        shape_sero.addcomponent(segment, "#17F568", "green")
turtle.register_shape("zero", shape_sero)
turtle.reset()
turtle.shape("zero")

turtle.mainloop()
import turtle


turtle.mode("logo")

# Сегменты для цифр
segment_1 = ((6, 200), (28, 180), (106, 180), (128, 200))
segment_2 = ((112, 175), (112, 118), (126, 105), (133, 112), (133, 194))
segment_3 = ((125, 95), (133, 87), (133, 6), (112, 25), (112, 82))
segment_4 = ((120, 100), (109, 90), (26, 90), (15, 100), (26, 110), (109, 110))

shape_sero = turtle.Shape("compound")
shape_sero.addcomponent(segment_1, "#17F568", "green")
shape_sero.addcomponent(segment_2, "#17F568", "green")
shape_sero.addcomponent(segment_3, "#17F568", "green")
shape_sero.addcomponent(segment_4, "#17F568", "green")
turtle.register_shape("zero", shape_sero)
turtle.reset()
turtle.shape("zero")

turtle.mainloop()

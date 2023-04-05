import turtle

#1. Прямоугольник
# Создайте новый холст с помощью функции Pen модуля turtle и изобра- зите на нем прямоугольник.

t = turtle.Pen()
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.reset()

#2. Треугольник
# Создайте новый холст и нарисуйте на нем треугольник. Разворачивая че- репашку, сверяйтесь с изображением окружности и градусов поворота (см. «Перемещение черепашки» на стр. 51).

t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.reset()

#3. Рамка без углов
t.forward(100)
t.up()
t.forward(50)
t.left(90)
t.forward(50)
t.down()
t.forward(100)
t.up()
t.forward(50)
t.left(90)
t.forward(50)
t.down()
t.forward(100)
t.up()
t.forward(50)
t.left(90)
t.forward(50)
t.down()
t.forward(100)
t.up()
t.forward(50)
t.left(90)
t.forward(50)
t.down()
t.reset()

# turtle.done()
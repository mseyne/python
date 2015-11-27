# -*- coding:Utf:8 -*-
from dessin_tortue import *

up()
goto(-150, 50)
i = 0

while i < 18:
	down()
	carre(25, 'red', 20)
	up()
	forward(35)
	i += 1

goto(0, 400)
x = 10
i = 0

while i < 10:
	down()
	triangle(x, 'blue', 20)
	up()
	forward(x+10)
	i += 1
	x += 10

seth(0)
goto(-450, -100)
x = 10
i = 0

while i < 8:
	down()
	carre(x, 'red', 0)
	up()
	forward(x + 5)
	down()
	triangle(x, 'blue', 0)
	up()
	forward(x + 5)
	i += 1
	x += 10

a = input()
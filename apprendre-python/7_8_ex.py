# -*- coding:Utf:8 -*-
from dessin_tortue import *


c = 0
a = 10
t = 10

up()
goto(0, 0)
down()
tracer(0) #directement

while c < 10:

	etoileSix(t, "red", 0)
	up()
	forward(t + 5)
	down()
	carre(t, "green", 0)
	carre(t, "green", 0)
	up()
	forward(t + 5)
	down()
	etoileCinq(t, "blue", 0)
	up()
	left(90)
	forward(t/2)
	right(90)
	forward(t + 5)
	down()

	c, a, t = c + 1, a + 10, t + 10

a = input()
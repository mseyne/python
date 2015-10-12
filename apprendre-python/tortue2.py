from dessin_tortue import *

up()
goto(-400, 0)

x = 20

while x < 100:
	down()
	etoileCinq(x, "green", 0)
	up()
	seth(0)
	forward(x + 10)
	x += 20

while x > 20:
	down()
	etoileCinq(x, "green", 0)
	up()
	seth(0)
	forward(x + 10)
	x -= 20

a = input()
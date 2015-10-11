from tortuecarre import *

up()
goto(-150, 50)

i = 0
while i < 10:
	down()
	carre(25, 'red')
	up()
	forward(30)
	i += 1

a = input()
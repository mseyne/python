# -*- coding:Utf:8 -*-
from turtle import *

def carre(taille, couleur, angle):
	"fonction qui dessine un carré de taille et de couleur déterminées"
	color(couleur)
	c = 0
	left(angle)
	while c < 4:
		forward(taille)
		left(90)
		c = c + 1

def triangle(taille, couleur, angle):
	"fonction qui dessine un triangle équilatéral de taille, d'angle et de couleur déterminées"
	color(couleur)
	c = 0
	left(angle)
	while c < 3:
		forward(taille)
		right(120)
		c += 1

def etoileCinq(taille, couleur, angle):
	"fonction qui dessine une étoile"
	color(couleur)
	c = 0
	right(angle)
	while c < 5:
		forward(taille)
		right(144)
		c += 1

def etoileSix(taille, couleur, angle):
	"fonction qui utilise la fonction triangle 2 fois de manière inversé pour obtenir l'étoile à six branches"
	# color(couleur)
	# c = 0
	# left(angle)
	# #premier triangle
	# while c < 3:
	# 	forward(taille)
	# 	right(120)
	# 	c += 1

	triangle(taille, couleur, angle)

	up()
	right(90)
	forward(taille/2)
	left(90)
	down()

	#deuxième triangle
	c = 0
	while c < 3:
		forward(taille)
		left(120)
		c += 1

	right(45) # c'est cette rotation qui permet la spirale de l'ex 7_8
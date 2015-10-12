from turtle import *

def carre(taille, couleur, angle):
	"fonction qui dessine un carré de taille et de couleur déterminées"
	color(couleur)
	c = 0
	left(angle)
	while c < 4:
		forward(taille)
		right(90)
		c = c + 1

def triangle(taille, couleur, angle):
	"fonction qui dessine un triangle équilatéral de taille, d'angle et de couleur déterminées"
	color(couleur)
	c = 0
	right(angle)
	while c < 3:
		forward(taille)
		right(120)
		c += 1

def etoileCinq(taille, couleur, angle):
	"fonction qui dessine une étoile"
	color(couleur)
	c = 0
	left(angle)
	while c < 5:
		forward(taille)
		right(144)
		c += 1

def etoileSix():
	"fonction qui utilise la fonction triangle 2 fois de manière inversé pour obtenir l'étoile à six branches"
	pass
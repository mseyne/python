# -*- coding:Utf-8 -*-
# une série de triangles équilatéraux de différentes couleurs.

import turtle as tt
import random
import time

COULEURS = ["red", "blue", "yellow", "green", "brown", "gold", "grey", "pink"]

class Program():

	def __init__(self):
		self.nbTriangle = int(input("Combien de triangle souhaitez vous dessiner ?"))

	def creation_triangle(self):
		#choix de taille du triangle
		self.chx = random.randint(10, 100)
		tt.begin_fill()
		for _ in range(3):
			tt.forward(self.chx)
			tt.left(120)
		tt.end_fill()
		print("debug", tt.heading())

	def choix_position(self):
		#position aléatoire dans l'écran
		self.x = random.randint(-350, 350)
		self.y = random.randint(-350, 350)
		tt.up()
		tt.goto(self.x, self.y)
		tt.down()

	def choix_couleur(self):
		#choix d'une couleur pour le triangle
		self.choix = random.randint(0, len(COULEURS)-1)
		self.couleur1 = COULEURS[self.choix]
		self.choix = random.randint(0, len(COULEURS)-1)
		self.couleur2 = COULEURS[self.choix]
		tt.pencolor(self.couleur1)
		tt.fillcolor(self.couleur2)

	def choix_taille(self):
		#choix de la taille du trait du triangle
		self.w = random.randint(2, 6)
		tt.width(self.w)

	def afficher_triangle(self):
		self.compteur = 0
		while self.compteur < self.nbTriangle:
			print("Triangle", self.compteur + 1)
			self.choix_position()
			self.choix_couleur()
			self.choix_taille()
			self.creation_triangle()
			self.compteur += 1
		for i in reversed(range(5)):
			print(i + 1)
			time.sleep(1)

if __name__ == "__main__":
	program = Program()
	program.afficher_triangle()
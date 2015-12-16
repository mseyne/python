# -*- coding:Utf-8 -*-
"le programme de la balle qui se déplace en cercle avec un bouton et laisse une trace derrière elle"

from tkinter import *
from math import sin, cos
from random import choice

COLOR = ["lavender", "bisque", "khaki", "azure", "ivory", "blue", "red", "yellow", "green"]

def creationBout(source, texte, commande):
	return Button(source, text=texte, command=commande)

def creationCans(source, w, h, color = COLOR[5]):
	return Canvas(source, width=w, height=h, bg=color)

	
def deplacerBalle():
	global x, y, ang

	xp, yp, = x, y #sauvegarde des paramètres précédents

	# ici j'ai utilisé la correction
	ang += .1
	#x, y = sin(ang), cos(ang)
	x, y = sin(2*ang), cos(3*ang) #courbe de Lissajous
	x, y = x*75 + 100, y*75 + 100

	can1.coords(cercle, x+r, y+r, x-r, y-r)
	can1.create_line(xp, yp, x, y, fill =choice(COLOR)) 
	afficherTexte()

def afficherTexte():
	canTxt.itemconfig(texte, text="x = %s, y = %s" % (round(x,2), round(y,2)))


fenetre = Tk()

#création des canvas
can1 = creationCans(fenetre, 200, 200, COLOR[3])
canTxt = creationCans(fenetre, 200, 20, COLOR[0])
canBut = creationCans(fenetre, 200, 40)

#création du cercle
x, y, r, ang = 100., 175., 5, 0.
cercle = can1.create_oval(x+r, y+r, x-r, y-r, fill=COLOR[6])

#création des boutons
btDepl = creationBout(canBut, "déplacer", deplacerBalle)
btQuit = creationBout(canBut, "quitter", fenetre.quit)

#création du texte
texte = canTxt.create_text(80, 10, fill=COLOR[6], text="x = %s, y = %s" % (x, y))

#mise en place de la grille
can1.grid(row=1, column=1)
canTxt.grid(row=2, column=1)
canBut.grid(row=3, column=1)

btDepl.grid(row = 1, column=1, pady=3, padx=5)
btQuit.grid(row = 1, column=2, padx=5)



fenetre.geometry("200x260+400+300")
fenetre.mainloop()
# -*- coding:Utf-8 -*-
"le programme de la balle qu'on déplace avec un bouton"

from tkinter import *

COLOR = ["lavender", "bisque", "khaki", "azure", "ivory", "white", "blue", "red", "yellow", "green"]

def creationBout(source, texte, commande):
	return Button(source, text=texte, command=commande)

def creationCans(source, w, h, color = COLOR[5]):
	return Canvas(source, width=w, height=h, bg=color)

def verifBalle(w):
	print("hello, world! 1", x, y)

	if x >= 190 and y >= 190:
		print("hello, world! 2", x, y)
		return 0
	if x <= 10 and y <= 10:
		print("hello, world! 3", x, y)
		return 1
	else:
		return w
	
def deplacerBalle():
	global x, y, way
	print("debug1:",way)
	way = verifBalle(way)
	print("debug1:",way)

	if way == 1:
		x, y = x+10, y+10
	elif way == 0:
		x, y = x-10, y-10

	can1.coords(cercle, x+r, y+r, x-r, y-r)
	afficherTexte()

def afficherTexte():
	canTxt.itemconfig(texte, text="x = %s, y = %s" % (x, y))


fenetre = Tk()

#création des canvas
can1 = creationCans(fenetre, 200, 200, COLOR[3])
canTxt = creationCans(fenetre, 200, 20, COLOR[0])
canBut = creationCans(fenetre, 200, 40)

#création du cercle
x, y, r, way = 100, 100, 10, 1
cercle = can1.create_oval(x+r, y+r, x-r, y-r, fill=COLOR[6])

#création des boutons
btDepl = creationBout(canBut, "déplacer", deplacerBalle)
btQuit = creationBout(canBut, "quitter", fenetre.quit)

#création du texte
texte = canTxt.create_text(50, 10, fill=COLOR[6], text="x = %s, y = %s" % (x, y))

#mise en place de la grille
can1.grid(row=1, column=1)
canTxt.grid(row=2, column=1)
canBut.grid(row=3, column=1)

btDepl.grid(row = 1, column=1, pady=3, padx=5)
btQuit.grid(row = 1, column=2, padx=5)



fenetre.geometry("200x260+400+300")
fenetre.mainloop()
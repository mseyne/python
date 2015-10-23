# -*- coding:Utf-8 -*-

#two cercles than we can move independently and display the distance between them

from tkinter import *

x1, y1, r1, x2, y2, r2 = 50, 50, 30, 150, 150, 40
color = ["yellow", "blue", "green", "ivory", "white", "red"]

def cercle(x, y, r, coul):
	return canva.create_oval(x+r, y+r, x-r, y-r, fill=coul )

def bouton(texte, commande):
	return Button(fenetre, text=texte, command=commande)

def mouvementCercle(chx, dg, hb):
	global x1, y1, x2, y2
	if chx == 0:
		x1, y1 =  x1 + dg, y1 + hb
		canva.coords(cercle1, x1+r1, y1+r1, x1-r1, y1-r1)
	else:
		x2, y2 =  x2 + dg, y2 + hb
		canva.coords(cercle2, x2+r2, y2+r2, x2-r2, y2-r2)

def distanceCercles():
	"retourne un texte dans le canva qui change à chaque fois que la distance change"
	pass

def depl_gauche(choix):
	print("debug : OK", choix)
	c = choix
	x, y = -10, 0
	mouvementCercle(c, x, y)

def depl_droite(choix):
	c = choix
	x, y = 10, 0
	mouvementCercle(c, x, y)

def depl_haut(choix):
	c = choix
	x, y = 0, -10
	mouvementCercle(c, x, y)

def depl_bas(choix):
	c = choix
	x, y = 0, 10
	mouvementCercle(c, x, y)

fenetre = Tk()

canva = Canvas(fenetre, bg=color[3], width = 200, height = 200)
canva.pack(padx = 5, pady = 5)
canvt = Canvas(fenetre, bg=color[4], width = 200, height = 20)
canvt.pack()


# distance = distanceCercles()
cercle1 = cercle(x1, y1, r1, color[0])
cercle2 = cercle(x2, y2, r2, color[1])

print(cercle1, cercle2)

bouton("Quitter", fenetre.quit).pack(side="right", padx = 5, pady = 5)

Button(fenetre, text="gauche", command=lambda: depl_gauche(0)).pack()
# b1gauche = bouton("<-C1", depl_gauche(0))
# b1gauche.pack()
# b1droite =
# b1bas =
# b1haut =

# b2gauche =
# b2droite = 
# b2bas = 
# b2haut =

fenetre.resizable(0,0)
fenetre.mainloop()
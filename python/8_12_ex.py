# -*- coding:Utf-8 -*-

#two cercles than we can move independently and display the distance between them

from tkinter import *

# variables

x1, y1, r1, x2, y2, r2 = 50, 50, 30, 150, 150, 40
color = ["yellow", "blue", "green", "ivory", "white", "red"]

# définition de fonctions

def cercle(x, y, r, coul):
	return canva.create_oval(x+r, y+r, x-r, y-r, fill=coul )

def bouton(source, texte, commande):
	return Button(source, text=texte, command=commande)

def mouvementCercle(chx, dg, hb):
	"reçoit l'input du bouton et déplace le cercle choisit en conséquence"
	global x1, y1, x2, y2
	if chx == 0:
		x1, y1 =  x1 + dg, y1 + hb
		canva.coords(cercle1, x1+r1, y1+r1, x1-r1, y1-r1)
	else:
		x2, y2 =  x2 + dg, y2 + hb
		canva.coords(cercle2, x2+r2, y2+r2, x2-r2, y2-r2)
	distanceCercles()

def distanceCercles():
	"retourne un texte dans le canva qui change à chaque fois que la distance change"
	print(x1, y1, r1, x2, y2, r2)
	print()
	print(canva.coords(cercle1), canva.coords(cercle2))
	canvt.itemconfig(text, text="x1 = %s, y1 = %s, x2 = %s, y2 = %s" % (x1, y1, x2, y2))

#programme

fenetre = Tk()

#création des canvas dans la fenetre
canva = Canvas(fenetre, bg=color[3], width = 200, height = 200)
canva.pack(padx = 5, pady = 5)
canvt = Canvas(fenetre, bg=color[4], width = 200, height = 20)
canvt.pack()
canv01 = Canvas(fenetre, bg=color[4], width = 200, height = 20)
canv01.pack()
canv02 = Canvas(fenetre, bg=color[4], width = 200, height = 20)
canv02.pack()

# distance = distanceCercles()
cercle1 = cercle(x1, y1, r1, color[0])
cercle2 = cercle(x2, y2, r2, color[1])

# création du texte dans le canvat
text = canvt.create_text(100, 10, text="Hello, World!")

# création des différents boutons
b1gauche = bouton(canv01, "C1 gauche", lambda: mouvementCercle(0, -10, 0))
b1gauche.pack(side="left")
b1droite = bouton(canv01, "C1 droite", lambda: mouvementCercle(0, 10, 0))
b1droite.pack(side="left")
b1bas = bouton(canv01, "C1 bas", lambda: mouvementCercle(0, 0, 10))
b1bas.pack(side="left")
b1haut = bouton(canv01, "C1 haut", lambda: mouvementCercle(0, 0, -10))
b1haut.pack(side="left")

b2gauche = bouton(canv02, "C2 gauche", lambda: mouvementCercle(1, -10, 0))
b2gauche.pack(side="left")
b2droite = bouton(canv02, "C2 droite", lambda: mouvementCercle(1, 10, 0))
b2droite.pack(side="left")
b2bas = bouton(canv02, "C2 bas", lambda: mouvementCercle(1, 0, 10))
b2bas.pack(side="left")
b2haut = bouton(canv02, "C2 haut", lambda: mouvementCercle(1, 0, -10))
b2haut.pack(side="left")

bouton(fenetre, "Quitter", fenetre.quit).pack(side="right", padx = 5, pady = 5)


fenetre.resizable(0,0)
fenetre.mainloop()
# -*- coding:Utf-8 -*-
"identique à 8_13, mais possibilité de choisir le déplacement de trois cercles(bleu, jaune, rouge) avec des boutons"

from tkinter import *

x, y, r = [50, 100, 150], [50, 100, 150], 10
color = ["yellow", "blue", "green", "ivory", "white", "red", "orange"]
cercle, c = 0, 1 #cercle

def creationBouton(source, text, command, color):
	return Button(source, text=text, command=command, bg=color)

def creationCercle(x, y, r, color):
	"crée un cercle de coordonée x, y"
	return canva.create_oval(x + r, y + r, x - r, y - r, fill=color)

def cercleMove(event):
	"deplace le cercle choisi"
	global x, y
	x[c]= event.x
	y[c]= event.y
	canva.coords(cercle, x[c] + r, y[c] + r, x[c] - r, y[c] - r)

def choixCercle(chx):
	"selon le bouton choisi, change de cercle"
	global c, cercle
	if chx == 1:
		cercle = cercle1
		c = 0
		canvT.itemconfig(text, text="Cercle jaune sélectionné.", fill=color[6])
	elif chx == 2:
		cercle = cercle2
		c = 1
		canvT.itemconfig(text, text="Cercle bleu sélectionné.", fill=color[1])
	elif chx == 3:
		cercle = cercle3
		c = 2
		canvT.itemconfig(text, text="Cercle rouge sélectionné.", fill=color[5])

fenetre = Tk()

canva = Canvas(fenetre, width=200, height=200, bg=color[3])
canva.pack(pady=5)

canva.bind("<Button-1>", cercleMove)

canvT = Canvas(fenetre, width=200, height=20)
canvT.pack()
canvB = Canvas(fenetre, width=200, height=20)
canvB.pack(pady=5)
canvQ = Canvas(fenetre, width=200, height=20)
canvQ.pack()
# création du texte dans le canvat
text = canvT.create_text(100, 10, text="Hello, World!")

# création des cercles
cercle1 = creationCercle(x[0], y[0], r, color[0])
cercle2 = creationCercle(x[1], y[1], r, color[1])
cercle3 = creationCercle(x[2], y[2], r, color[5])

# création des boutons
But1 = creationBouton(canvB, "Jaune", lambda: choixCercle(1), color[0])
But1.pack(side="left")
But2 = creationBouton(canvB, "Bleu", lambda: choixCercle(2), color[1])
But2.pack(side="left", padx=10)
But3 = creationBouton(canvB, "Rouge", lambda: choixCercle(3), color[5])
But3.pack(side="left")



Button(canvQ, text="Quitter", command=fenetre.quit).pack(side="right", padx = 10, pady = 5)

fenetre.geometry("220x320+400+250")
fenetre.resizable(0,0)
fenetre.mainloop()
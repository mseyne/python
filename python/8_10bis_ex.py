# -*- coding:Utf-8 -*-

from tkinter import *
from random import randrange


def damier():
	"dessiner dix lignes de carrés avec décalage alterné"
	y = 0
	while y < 10:
		if y%2 == 0:
			x = 0
		else:
			x = 1
		ligne_de_carres(x*c, y*c)
		y += 1

def ligne_de_carres(x, y):
    "dessiner une ligne de carrés, en partant de x, y"
    i = 0
    while i < 5:
	    can.create_rectangle(x, y, x+c, y+c, fill="navy")
	    x += 2*c
	    i += 1


def cercle(x, y, r, coul):
    "dessiner un cercle de centre x,y et de rayon r"
    can.create_oval(x+r, y+r, x-r, y-r, fill=coul)

def ajouter_pion():
    "dessiner un pion au hasard sur le damier"
    rayon = c/3
    x = randrange(10) * c + c/2
    y = randrange(10) * c + c/2
    cercle(x, y, rayon, "red")

##### Programme principal : ############
    
# Tâchez de bien "paramétrer" vos programmes, comme nous l'avons
# fait dans ce script. Celui-ci peut en effet tracer des damiers
# de n'importe quelle taille en changeant seulement la valeur
# d'une seule variable, à savoir la dimension des carrés :
 
c = 30                  # taille des carrés
W, H = c * 10, c * 10

fen = Tk()
#fen.geometry('%dx%d+300+200' % (W, H))
can = Canvas(fen, width=W, height=H, bg="ivory")
can.pack(side= "top", padx = 5, pady= 5)

b1 = Button(fen, text="Damier", command=damier)
b1.pack(side="left", padx=3, pady=3)
b2 = Button(fen, text="Pion", command=ajouter_pion)
b2.pack(side="right", padx=3, pady=3)

fen.resizable(0,0)
fen.mainloop()
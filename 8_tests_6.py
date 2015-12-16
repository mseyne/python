# -*- coding:Utf-8 -*-

from tkinter import *

#variables globales dans la fonction avance()
x1, y1 = 10, 10 #coordonnées initiales

#fonctions
#procédure générale de déplacement
def avance(gd, hb):
	global x1, y1
	x1, y1 = x1 + gd, y1 +hb
	can1.coords(oval1, x1, y1, x1+30, y1+30)


#gestionnaires d'événements
def dpl_gauche():
	avance(-10, 0)

def dpl_droite():
	avance(10, 0)

def dpl_haut():
	avance(0, -10)

def dpl_bas():
	avance(0, 10)


#programme principal

#wigdet principal source
fen1=  Tk()
fen1.title("Exercice d'animation avec tkinter")

#widgets child
can1 = Canvas(fen1, bg="dark grey", height=300, width=300)
oval1 = can1.create_oval(x1, y1, x1+30, y1+30, width=2, fill='blue')
can1.pack(side="left")

Button(fen1, text='Quitter', command=fen1.quit).pack(side="bottom")
Button(fen1, text='Gauche', command=dpl_gauche).pack()
Button(fen1, text='Droite', command=dpl_droite).pack()
Button(fen1, text='Haut', command=dpl_haut).pack()
Button(fen1, text='Bas', command=dpl_bas).pack()

#boucle principale (réception des évènements)
fen1.mainloop()
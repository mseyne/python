# -*- coding:Utf-8 -*-
"mouvement d'une balle et changement de couleur"

from tkinter import *
from random import choice

#définition des gestionnaires d'évènements :

COLORS = ["grey", "yellow", "green", "red", "purple", "blue"]

def move():
	"déplacement de la balle"
	global x1, y1, dx, dy, flag, c
	x1, y1 = x1 + dx, y1 + dy

	if x1 > 210:
		x1, dx, dy = 210, 0, 15
		c = 1

	if y1 > 210:
		y1, dx, dy = 210, -15, 0
		c = 1

	if x1 < 10:
		x1, dx, dy = 10, 0, -15
		c = 1
	
	if y1 < 10:
		y1, dx, dy = 10, 15, 0
		c = 1

	if c == 1:
		oval_color()
	can1.coords(oval1, x1, y1, x1+30, y1+30)
	if flag >0:
		fen1.after(50, move)

def stop_it():
	"arrêt de l'animation"
	global flag
	flag = 0

def start_it():
	"démarrage de l'animation"
	global flag
	if flag == 0:
		flag = 1
		move()

def oval_color():
	"changement de couleur aléatoire, une couleur différente à chaque fois"
	global c, color

	while True:
		new_color = choice(COLORS) #a random color with random.choice
		if new_color != color:
			break
	can1.itemconfig(oval1, fill=new_color)
	color = new_color
	c = 0

# Les variables suivantes seront utilisées de manière globale :
x1, y1 = 10, 10 #coordonées initiales
dx, dy = 15, 0 # 'pas' du déplacement
flag = 0  # commutateur
c = 0 #color flag, se lève si le cercle change de direction
color = "red" #the changing color

# Création du widget principal ("parent") :
fen1 = Tk()
fen1.title("Exercice d'animation avec tkinter")

# Création des widgets "enfants" :
can1 = Canvas(fen1, bg='dark grey', height=250, width=250)
can1.pack(side="left", padx=5, pady=5)
oval1 = can1.create_oval(x1, y1, x1+30, y1+30, width=2, fill=color)
bou1 = Button(fen1, text="Quitter", width=8, command=fen1.quit)
bou1.pack(side="bottom")
bou2 = Button(fen1, text="Démarrer", width=8, command=start_it)
bou2.pack()
bou3 = Button(fen1, text="Arrêter", width=8, command=stop_it)
bou3.pack()

# boucle principale
fen1.mainloop()
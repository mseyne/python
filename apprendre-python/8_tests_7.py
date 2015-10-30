# -*- coding:Utf-8 -*-

from tkinter import *

#définition des gestionnaires d'évènements :

def move():
	"déplacement de la balle"
	global x1, y1, dx, dy, flag
	x1, y1 = x1 + dx, y1 + dy
	if x1 > 210:
		x1, dx, dy = 210, 0, 15
	if y1 > 210:
		y1, dx, dy = 210, -15, 0
	if x1 < 10:
		x1, dx, dy = 10, 0, -15
	if y1 < 10:
		y1, dx, dy = 10, 15, 0
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
	if flag ==0:
		flag =1
		move()

# Les variables suivantes seront utilisées de manière globale :
x1, y1 = 10, 10 #coordonées initiales
dx, dy = 15, 0 # 'pas' du déplacement
flag = 0  # commutateur

# Création du widget principal ("parent") :
fen1 = Tk()
fen1.title("Exercice d'animation avec tkinter")

# Création des widgets "enfants" :
can1 = Canvas(fen1, bg='dark grey', height=250, width=250)
can1.pack(side="left", padx=5, pady=5)
oval1 = can1.create_oval(x1, y1, x1+30, y1+30, width=2, fill='red')
bou1 = Button(fen1, text="Quitter", width=8, command=fen1.quit)
bou1.pack(side="bottom")
bou2 = Button(fen1, text="Démarrer", width=8, command=start_it)
bou2.pack()
bou3 = Button(fen1, text="Arrêter", width=8, command=stop_it)
bou3.pack()

# boucle principale
fen1.mainloop()
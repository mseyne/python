# -*- coding:Utf:8 -*-
"identique à 8.12, sauf que le clique est utilisé pour déplacer le cercle plutot que les boutons"

from tkinter import *
from random import choice

x, y, r = 100, 100, 10
color = ["yellow", "blue", "green", "ivory", "white", "red"]

def cercleMove(event):
	global x, y
	x= event.x
	y= event.y
	c = choice(color)
	canva.itemconfig(cercle, fill=c)
	canva.coords(cercle, x + r, y + r, x - r, y - r)


fenetre = Tk()

canva = Canvas(fenetre, width=200, height=200, bg=color[3])
canva.pack(pady=10)

canvT = Canvas(fenetre, width=200, height=20, bg=color[4])
canvT.pack()

cercle = canva.create_oval(x + r, y + r, x - r, y - r, fill=choice(color))

Button(fenetre, text="Quitter", command=fenetre.quit).pack(side="right", padx = 10)

canva.bind("<Button-1>", cercleMove)


fenetre.geometry("220x300+400+250")
fenetre.resizable(0,0)
fenetre.mainloop()
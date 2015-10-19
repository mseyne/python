# -*- coding:Utf-8 -*-

from tkinter import *
from random import choice


def carre(x, y):
	"dessine un petit cube bleu qui sert au plateau"
	can.create_rectangle(x, y, x+20, y+20, outline="black", fill="blue")


def plateau():
	"dessine le plateau"
	can.delete(ALL)
	can.create_rectangle(5, 5, 205, 205, outline="black", fill="ivory")
	c = 1
	for col in range(5, 205, 20):
		print("colonne", col)
		
		if c == 0:
			for row in range(25, 205, 40):
				print('rangée', row)
				carre(row, col)
				c = 1

		elif c == 1:
			for row in range(5, 205, 40):
				print('rangée', row)
				carre(row, col)
				c = 0



def cercle():
	"dessine un petit pion rouge à un des emplacements du plateau"
	r = 5
	x = []
	y = []

	for i in range(10, 200, 40):
		x.append(i)
		y.append(i)
	
	x = choice(x)
	y = choice(y)

	can.create_oval(x-r, y-r, x+r, y+r, fill="red")

fen = Tk()
can = Canvas(fen, width = 210, height = 210, bg="white")
can.pack(padx = 5, pady = 5)
bou1 = Button(fen, text="Plateau", command=plateau)
bou1.pack(side="left", padx = 5, pady = 5)
bou2 = Button(fen, text="Pion", command=cercle)
bou2.pack(side="right", padx = 5, pady = 5)

bou3 = Button(fen, text="quit", command=fen.quit)
bou3.pack(pady = 5)

fen.mainloop()
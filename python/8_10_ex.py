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
		
		if c == 0:
			for row in range(25, 205, 40):
				carre(row, col)
				c = 1

		elif c == 1:
			for row in range(5, 205, 40):
				carre(row, col)
				c = 0


def cercle():
	"dessine un petit pion rouge à un des emplacements du plateau"
	r = 7
	x = []
	y = []

	for i in range(15, 200, 40):
		x.append(i)
		y.append(i)
	
	x = choice(x)
	y = choice(y)

	can.create_oval(x-r, y-r, x+r, y+r, fill="red")

def geometry():
	W, H = 220, 260

	wS = fen.winfo_screenwidth()
	hS = fen.winfo_screenheight()

	x = wS/2 - W/2
	y = hS/2 - H/2

	fen.geometry("%dx%d+%d+%d" % (W, H, x, y))

fen = Tk()
geometry()
can = Canvas(fen, width = 210, height = 210, bg="white")
can.pack(padx = 5, pady = 5)

bou1 = Button(fen, text="Plateau", command=plateau)
bou1.pack(side="left", padx = 5, pady = 5)
bou2 = Button(fen, text="Pion", command=cercle)
bou2.pack(side="right", padx = 5, pady = 5)

bou3 = Button(fen, text="quit", command=fen.quit)
bou3.pack(side= "bottom", pady = 5)
fen.resizable(0,0)
fen.mainloop()
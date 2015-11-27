# -*- coding:Utf:8 -*-

from tkinter import *

def cercle(x, y, r, coul="black"):
	"tracé d'un cercle de centre x, y et de rayon r"
	can.create_oval(x-r, y-r, x+r, y+r, outline=coul)

def figure1():
	"dessiner une cible"
	#effacer le canvas
	can.delete(ALL)
	#trace les deux lignes
	can.create_line(100, 0, 100, 200, fill="blue")
	can.create_line(0, 100, 200, 100, fill="blue")
	#trace les cercles
	rayon = 15
	while rayon < 100:
		cercle(100, 100, rayon)
		rayon += 15

def figure2():
	"dessiner un visage"
	#effacer le canvas
	can.delete(ALL)
	cc = [
	[100, 100, 80, "red"], #visage
	[70, 70, 15, "blue"], #yeux
	[130, 70, 15, "blue"],
	[70, 70, 5, "black"],
	[130, 70, 5, "black"],
	[44, 115, 20, "red"], #joues
	[156, 115, 20, "red"],
	[100, 95, 15, 'purple'],
	[100, 145, 30, 'purple']
	]

	i = 0
	while i < len(cc):
		el = cc[i]
		cercle(el[0], el[1], el[2], el[3])
		i += 1

fen = Tk()
can = Canvas(fen, width = 200, height = 200, bg="ivory")
can.pack(side="top", padx = 5, pady = 5)
b1 = Button(fen, text="Figure 1", command=figure1)
b1.pack(side="left", padx = 5, pady = 5)
b2 = Button(fen, padx = 5, pady = 5, text="Figure 2", command=figure2)
b2.pack(side="right", padx = 5, pady = 5)
fen.mainloop()
# -*- coding:Utf-8 -*-

from tkinter import *
from random import randrange


#variables

height, width = 650, 500
x1, y1, x2, y2 = 0, 10, 500, 10
coul = 'dark green'

#fonctions

def drawline():
	global x1, y1, x2, y2
	can1.create_line(x1, y1, x2, y2, width=2, fill=coul)
	y2, y1 = y2+10, y1+10

def changecolor():
	global coul
	pal = ['purple', 'cyan', 'maroon', 'green', 'red', 'blue', 'orange', 'yellow']
	c = randrange(8)
	coul = pal[c]

def drawline2():
	can1.create_line(width/2, 0, width/2, height, width=2, fill="red")
	can1.create_line(0, height/2, width, height/2, width=2, fill="red")

def drawrect():
	can1.create_rectangle(50, 0, 0, 50, width=2, fill="blue")

def drawarc():
	can1.create_arc(50, 50, 100, 100, width=2, fill="green")

def drawoval():
	can1.create_oval(100, 100, 200, 200, width=2, outline="orange")

def drawpolyg():
	can1.create_polygon(200, 200, 300, 300, 300, 200, width=2, outline="yellow", fill="dark green")

# programme

fen1 = Tk()
can1 = Canvas(fen1, bg='dark gray', height=height, width=width)
can1.pack(side=LEFT)
bou1 = Button(fen1, text="Quitter", command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text="Tracer une ligne", command=drawline)
bou2.pack()
bou3 = Button(fen1, text='Autre couleur', command=changecolor)
bou3.pack()
bou4 = Button(fen1, text="Viseur", command=drawline2)
bou4.pack()
bou5 = Button(fen1, text="Rectangle", command=drawrect)
bou5.pack()
bou6 = Button(fen1, text="Arc", command=drawarc)
bou6.pack()
bou7 = Button(fen1, text="Oval", command=drawoval)
bou7.pack()
bou8 = Button(fen1, text="Polygone", command=drawpolyg)
bou8.pack()

fen1.mainloop()
fen1.destroy() 
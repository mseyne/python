from tkinter import *
from random import randrange


#variables

height, width = 650, 500
x1, y1, x2, y2 = 0, 10, 500, 10
coul = 'dark green'

#fonctions

def drawline():
	#global x1, y1, x2, y2
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

fen1.mainloop()
fen1.destroy()
# -*- coding:Utf-8 -*-

from tkinter import *
from random import randrange


POS = {
1 : [10, 10, 100, 100], 
2 : [60, 60, 150, 150], 
3 : [110, 10, 200, 100], 
4 : [160, 60, 250, 150], 
5 : [210, 10, 300, 100]
}

COUL = ['purple', 'cyan', 'maroon', 'green', 'red', 'blue', 'orange', 'yellow']

def drawCircle():
	for i in POS:
		couleur = COUL[randrange(8)]
		x1, y1, x2, y2 = POS[i][0], POS[i][1], POS[i][2], POS[i][3]
		can1.create_oval(x1, y1, x2, y2, outline=couleur, width="2")

H, W = 400, 600

fen1 = Tk()
can1 = Canvas(fen1, height = H, width = W, bg="grey")
can1.pack(side="top")
bou1 = Button(fen1, text="Quitter", command=fen1.quit).pack(side="right")
bou2 = Button(fen1, text="Dessiner les anneaux", command=drawCircle).pack(side="left")

fen1.mainloop()
fen1.destroy()
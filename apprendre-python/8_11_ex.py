# -*- coding:Utf-8 -*-
"""blue dots avec le clique de la souris"""

from tkinter import *

# def pointeur(event):
# 	chaine.configure(text = "Clic détecté en X =" + str(event.x)\
# 	 + ", Y =" + str(event.y))

def cercle(event):
	x = event.x
	y = event.y
	r = 3
	cadre.create_oval(x+3, y+3, x-3, y-3, fill="blue", outline="blue")

def cadre():
	global cadre
	cadre = Canvas(fen, width = 200, height = 150, bg ="light yellow")
	cadre.pack()
	cadre.bind("<Button-1>", cercle)

# def clean():
# 	cadre.destroy()
# 	cadre()

fen = Tk()

cadre()

chaine = Label(fen, text="Blue dots program")
chaine.pack(side="left")

# bouClean = Button(fen, text="Clean", command=clean)
# bouClean.pack(side="right")

fen.resizable(0,0)
fen.geometry("200x175+600+300")
fen.mainloop()
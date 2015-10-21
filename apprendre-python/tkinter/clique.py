# -*- coding:Utf-8 -*-

from tkinter import *

def pointeur(event):
	chaine.configure(text = "Clic détecté en X =" + str(event.x)\
	 + ", Y =" + str(event.y))

fen = Tk()
cadre = Frame(fen, width = 200, height = 150, bg ="light yellow")
cadre.pack()
cadre.bind("<Button-1>", pointeur)
chaine = Label(fen)
chaine.pack()

fen.resizable(0,0)
fen.geometry("200x175+400+300")
fen.mainloop()
# -*- coding:Utf-8 -*-
"calculatrice simple avec tkinter"

from tkinter import *


def evaluation():
	en = eval(entree.get())
	resultat = Label(fram, text=en)
	resultat.pack()

def frame():
	global fram
	fram = Frame(fen)
	fram.pack(side="bottom")

def nettoyer():
	fram.destroy()
	frame()

fen = Tk()

entree = Entry(fen)
entree.pack(padx=5, pady=5)
#entree.bind()

bout = Button(fen, text="OK", command=evaluation)
bout.pack(side="left", padx=10, pady=5)
bout2 = Button(fen, text="Reset", command=nettoyer)
bout2.pack(side="right", padx=10, pady = 5)

frame()


fen.mainloop()
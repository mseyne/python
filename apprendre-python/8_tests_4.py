# -*- coding:Utf-8 -*-
"calculatrice simple avec tkinter"

from tkinter import *
from math import *

def evaluation(event = '0'):
	en = eval(entree.get())
	chaine.configure(text = "Résultat : " + str(en))

def frame():
	global fram
	fram = Frame(canva)
	fram.pack()

def chaine():
	print("problem !")
	global chaine
	chaine = Label(fram)
	chaine.pack()

# def nettoyer():
# 	chaine.destroy()
# 	chaine()

fen = Tk()

canva = Canvas(fen)
canva.pack(padx = 5, pady = 5)

entree = Entry(fen)
entree.pack(padx=5, pady=5)
entree.bind("<Return>", evaluation)

bout = Button(fen, text="OK", command=evaluation)
bout.pack(side="left", padx=10, pady=5)
# bout2 = Button(fen, text="Reset", command=nettoyer)
# bout2.pack(side="right", padx=10, pady = 5)

frame()
chaine()




fen.mainloop()
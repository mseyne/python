# -*- coding:Utf-8 -*-
'binary to decimal converter'

from tkinter import *
import sys

BINARY = [1]

def createBinaryList():
	"I used it to find the BINARY list"
	global BINARY
	b = 2
	c = 0
	while c < 100:
		BINARY.append(b)
		c += 1
		b = b + b

def convertToBinary():
	dec = ent1.get()
	can1.itemconfig(text1, text=dec)

	#fonction to check if the number is composed only of number

def convertToDecimal():
	bin = ent1.get()
	can1.itemconfig(text1, text=bin)

	#fonction to check if the number is binary (composed of 0 and 1)

def exit(event):
	sys.exit()

def canvas():
	return Canvas(fenetre, width=200, height=50, bg="light grey")

def texte():
	return can1.create_text(100, 25, text="Convertissez une valeur décimal\n en valeur binaire, ou l'inverse.")

def entree():
	return Entry(fenetre, width=10)

def boutons():
	bouQ = Button(fenetre, command=fenetre.quit, text="Q")
	bouQ.grid(row=2, column=4, padx=5, pady=5)
	bouD = Button(fenetre, command=convertToDecimal, text="To decimal")
	bouD.grid(row=2, column=2)
	bouB = Button(fenetre, command=convertToBinary, text="To binary")
	bouB.grid(row=2, column=3)

def grid():
	can1.grid(row=1, column=1, columnspan=4, pady=10)
	ent1.grid(row=2, column=1, sticky="w", padx=5, pady=5)


if __name__ == '__main__':
	createBinaryList()

	fenetre = Tk()
	fenetre.resizable(0,0)
	fenetre.title("Convertisseur Binaire Décimal")
	fenetre.bind('<Escape>', exit)

	boutons()
	ent1 = entree()
	can1 = canvas()
	text1 = texte()
	grid()

	fenetre.mainloop()
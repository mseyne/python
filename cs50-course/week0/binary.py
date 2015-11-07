# -*- coding:Utf-8 -*-
'binary to decimal converter'

from tkinter import *
import sys

DECIMAL = [1]
BINARY = {1:0}

def createBinaryList():
	"I used it to find the BINARY list"
	global BINARY
	b = 2
	c = 0
	while c < 30:
		DECIMAL.append(b)
		BINARY[b] = 0
		c += 1
		b = b + b

def checkDecimal():
	"vérifie si il y a bien une valeur décimal entrée"
	nb = ent1.get()
	c = 0
	for i in nb:
		if i in list('1234567890'):
			c += 1
	if len(nb) == c:
		convertToBinary(int(nb))
	else:
		can1.itemconfig(text1, text="Vous n'avez pas choisi\n un nombre décimal.")

def checkBinary():
	"vérifie s'il y a bien une valeur binaire entrée"
	nb = ent1.get()
	c = 0
	for i in nb:
		if i in list('10'):
			c += 1
	if len(nb) == c:
		convertToDecimal(nb)
	else:
		can1.itemconfig(text1, text="Vous n'avez pas choisi\n un nombre binaire.")

def convertToBinary(nombre):
	"conversion d'un nombre décimal en nombre binaire base 2"
	decNb = nombre
	binNb = ""
	flag = 0 #j'utilise ce drapeau pour savoir à partir de quand j'enregistre les bits dans binNb

	while decNb > 0:
		for i in reversed(DECIMAL):
			if i <= decNb:
				flag = 1
				BINARY[i] = 1
				decNb = decNb%i
			if flag == 1:
				binNb = str(BINARY[i]) + binNb

	can1.itemconfig(text1, text="La valeur binaire de {} est\n{}".format(nombre, binNb))
	cleanBinary()

def cleanBinary():
	"remet le nombre binaire à zéro"
	for i in DECIMAL:
		BINARY[i] = 0

def convertToDecimal(nombre):
	"conversion d'un nombre binaire en nombre décimal"
	nbBin = nombre
	nbDec = 0
	c = 1

	for i in nbBin:
		if i == "1":
			nbDec += c
		c = c * 2

	can1.itemconfig(text1, text="La valeur décimal de {} est\n{}".format(nombre, nbDec))

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
	bouD = Button(fenetre, command=checkBinary, text="To decimal")
	bouD.grid(row=2, column=2)
	bouB = Button(fenetre, command=checkDecimal, text="To binary")
	bouB.grid(row=2, column=3)

def grid():
	can1.grid(row=1, column=1, columnspan=4, pady=10)
	ent1.grid(row=2, column=1, sticky="w", padx=5, pady=5)

def center():
	fenetre.update_idletasks()
	width = fenetre.winfo_width()
	height = fenetre.winfo_height()
	x = round(fenetre.winfo_screenwidth() / 2 - width / 2)
	y = round(fenetre.winfo_screenheight() / 2 - height / 2)
	fenetre.geometry("{}x{}+{}+{}".format(width, height, x, y))

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
	center()
	fenetre.mainloop()
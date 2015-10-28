# -*- coding:Utf-8 -*-
"conversion degré celsius, degré farenheit en mode graphique"

from tkinter import *


def return0(event):
	getEntry(0)

def return1(event):
	getEntry(1)

def getEntry(chx):
	if chx == 0:
		Far = entrFar.get()
		if verifNumerique(Far):
			convertFar(Far)
		# print("debug:","Far 2 Cel :", Far)
	elif chx == 1:
		Cel = entrCel.get()
		if verifNumerique(Cel):
			convertCel(Cel)
		# print("debug:","Cel 2 Far :", Cel)
	# else:
	# 	print("Bug")

def verifNumerique(string):
	verif = False
	for i in range(len(string)):
		if string[i] in list("1234567890."):
			verif = True
		else:
			verif = False
	if len(string) == 0:
		print("Vous n'avez pas transmis de données.")
	elif verif is False:
		print("Il ne s'agit pas d'un nombre entier ou décimal valide.")
	return verif

def convertFar(string):
	celsius = (float(string)-32)/1.80
	convert = round(celsius, 2)
	updateText(string, convert)

def convertCel(string):
	farenheit = float(string)*1.80 + 32
	convert = round(farenheit, 2)
	updateText(convert, string)

def updateText(string1, string2):
	texte1 = "%s degré Farenheit vaut :\n %s degré Celsius." % (string1, string2)
	texte2 = "%s degré Celsius vaut :\n %s degré Farenheit." % (string2, string1)
	can1.itemconfig(txt1, text=texte1)
	can2.itemconfig(txt2, text=texte2)


fenetre = Tk()
fen.title('Fahrenheit/Celsius')

can1 = Canvas(fenetre, bg = "blue", width = 200, height = 150)
can2 = Canvas(fenetre, bg = "red", width = 200, height = 150)

can1.grid(row="1", column="1", columnspan="2")
can2.grid(row="1", column="3", columnspan="2")

txt1 = can1.create_text(100, 75)
txt2 = can2.create_text(100, 74)

txtFar = Label(fenetre, text="Farenheit en Celsius", fg="blue")
entrFar = Entry(fenetre)
bOkFar = Button(fenetre, text="ok", command=lambda: getEntry(0))
txtFar.grid(row="2", columnspan="2", sticky="w")
entrFar.grid(row="3", column="1", sticky="e")
bOkFar.grid(row="3", column="2")
entrFar.bind("<Return>", return0)

txtCel = Label(fenetre, text="Celsius en Farenheit", fg="red")
entrCel = Entry(fenetre)
bOkCel = Button(fenetre, text="ok", command=lambda: getEntry(1))
txtCel.grid(row="2", column="3", columnspan="2", sticky="w")
entrCel.grid(row="3", column="3", sticky="e")
bOkCel.grid(row="3", column="4")
entrCel.bind("<Return>", return1)

bQt = Button(fenetre, text="quitter", command=fenetre.quit)
bQt.grid(row="4", column="4", pady=5)

# fenetre.geometry("400x250+400+200")
fenetre.resizable(0, 0)
fenetre.mainloop()
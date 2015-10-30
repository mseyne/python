# -*- coding:Utf:8 -*-
"passage pièton et changement de couleur des feux à l'appui d'un bouton"

from tkinter import *

CL = ["grey", "yellow", "green", "red"]

def creationCanvas(source, w=100, h=175, c="light grey"):
	return Canvas(source, width=w, height=h, bg=c, highlightthickness=0)

def creationCercle(source, x, y, c):
	return source.create_oval(x-10, y-10, x+10, y+10, fill=c)

def creationLigne():
	can1.create_line(0, 0, 0, 350)
	can1.create_line(199, 0, 199, 350)

def afficherRectangle():
	"affiche les rectangles du passage pour piétons"
	nb = 5
	i = 0
	esp = 0
	for i in range(nb):
		can1.create_rectangle(10+esp, 100, 30+esp, 250, fill=CL[1])
		esp += 40

def changement():
	"changement de couleur des feux"
	global feux
	if feux == 0:
		canNW.itemconfig(feuNW, fill=CL[3])
		canSW.itemconfig(feuNW, fill=CL[2])
		canNE.itemconfig(feuNW, fill=CL[2])
		canSE.itemconfig(feuNW, fill=CL[3])
		feux = 1
	elif feux == 1:
		canNW.itemconfig(feuNW, fill=CL[2])
		canSW.itemconfig(feuNW, fill=CL[3])
		canNE.itemconfig(feuNW, fill=CL[3])
		canSE.itemconfig(feuNW, fill=CL[2])
		feux = 0

fenetre = Tk()
fenetre.title("Feux piétons.")
#fenetre.configure(bg=CL[0])

fenetre.bind("<Escape>", lambda e: fenetre.quit())

frame = Frame(fenetre, width=400, height=400)
frame.pack()

# création des canvas
can1 = creationCanvas(frame, 200, 350, CL[0])
canNW = creationCanvas(frame)
canSW = creationCanvas(frame)
canNE = creationCanvas(frame)
canSE = creationCanvas(frame)

# créationd des feux
feux = 0
feuNW = creationCercle(canNW, 85, 100, CL[2])
feuSW = creationCercle(canSW, 85, 75, CL[3])
feuNE = creationCercle(canNE, 15, 100, CL[3])
feuSE = creationCercle(canSE, 15, 75, CL[2])

# dessin du passage piéton et de la route
afficherRectangle()
creationLigne()

# bouton pour input
bouFeux = Button(frame, text="Changer les feux", command=changement) 
bouQuit = Button(frame, text="Quitter", command=fenetre.quit)

#position grid 3 columns, 3 rows
can1.grid(row=1, rowspan=2, column=2)
canNW.grid(row=1, column=1)
canSW.grid(row=2, column=1)
canNE.grid(row=1, column=3)
canSE.grid(row=2, column=3)
bouFeux.grid(row=3, column=2, pady=10)
bouQuit.grid(row=3, column=3, sticky="e", padx=10, pady=10)


fenetre.geometry("400x400+300+200")
fenetre.resizable(0, 0)
fenetre.mainloop()
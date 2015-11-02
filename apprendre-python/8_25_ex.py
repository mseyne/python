# -*- coding:Utf-8 -*-
"mouvement de la balle en zig zag, en cercle ou le long d'une courbe de Lissajous (voir ex 8_19)"

from tkinter import *
from random import choice

WIDTH, HEIGHT = 300, 300
COLORS = ["blue", "red", "yellow", "green", "purple"]


def move_square():
	start_move()
	pass

def move_zigzag():
	start_move()
	pass

def move_cercle():
	start_move()
	pass

def move_lissajous():
	start_move()
	pass

def start_move():
	global flag
	flag = 1
	oval_color()
	repetition()

def stop_move():
	global flag
	flag = 0

def repetition():
	global flag
	if flag == 1:
		fenetre.after(50, repetition)
		print("hello, world")

def oval_color():
	"changement de couleur aléatoire quand le mouvement change"
	global color
	while True:
		new_color = choice(COLORS) #a random color with random.choice
		if new_color != color:
			break
	can1.itemconfig(oval1, fill=new_color)
	color = new_color

def bouton(source, texte, commande):
	return Button(source, text=texte, command=commande)

def center():
    fenetre.update_idletasks()
    width = fenetre.winfo_width()
    height = fenetre.winfo_height()
    x = (fenetre.winfo_screenwidth() // 2) - (width // 2)
    y = (fenetre.winfo_screenheight() // 2) - (height // 2)
    fenetre.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def info():
	fenetre.update()
	print (fenetre.winfo_width())
	print (fenetre.winfo_height())
	print (fenetre.winfo_geometry())

x, y, r = 100, 100, 10
flag = 0
ang = 0.1
color = COLORS[1]

fenetre = Tk()
fenetre.title("Balle Mouvante.")
fenetre.bind("<Escape>", lambda e: fenetre.quit())

can1 = Canvas(fenetre, width=WIDTH, height=HEIGHT, bg="dark grey")
can1.pack(side="left", padx=5, pady=5)

oval1 = can1.create_oval(x-r, y-r, x+r, y+r, width=2, fill=color)

boutSQ = bouton(fenetre, "Square", move_square)
boutSQ.pack()
boutZZ = bouton(fenetre, "Zig Zag", move_zigzag)
boutZZ.pack()
boutCL = bouton(fenetre, "Cercle", move_cercle)
boutCL.pack()
boutLJ = bouton(fenetre, "Lissajous", move_lissajous)
boutLJ.pack()
boutSP = bouton(fenetre, "Arrêter", stop_move)
boutSP.pack()
boutQT = bouton(fenetre, "Quitter", fenetre.quit)
boutQT.pack(side="bottom")

fenetre.resizable(0,0)
center()
info()

fenetre.mainloop()
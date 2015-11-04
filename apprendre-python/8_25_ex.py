# -*- coding:Utf-8 -*-
"mouvement de la balle en zig zag, en circle ou le long d'une courbe de Lissajous (voir ex 8_19)"
"peut être laisser des marques derrières"

from tkinter import *
from random import choice, randint
from math import cos, sin

WIDTH, HEIGHT = 300, 300
COLORS = ["blue", "red", "yellow", "green", "purple"]


def move_square():
	global x, y, dx, dy, move
	x, y = 20, 20
	dx, dy = 10, 0
	start_coord(x, y)
	move = "square"
	start_move()

def move_zigzag():
	global x, y, dx, dy, move
	x, y = 150, 150
	dx, dy = randint(-10, 10), randint(-10, 10)
	start_coord(x, y)
	move = "zigzag"
	start_move()

def move_circle():
	global x, y, dx, dy, move, ang
	ang, x, y = .1, 150., 250.
	start_coord(x, y)
	move = "circle"
	start_move()

def move_lissajous():
	global x, y, dx, dy, move, ang
	ang, x, y = .1, 198.68, 253.17
	start_coord(x, y)
	move = "lissajous"
	start_move()

def start_coord(x, y):
	"coordonées de départ de la balle"
	can1.coords(oval1, x+r, y+r, x-r, y-r)

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
	if move == "square":
		set_square()
	if move == "zigzag":
		set_zigzag()
	if move == "circle":
		set_circle()
	if move == "lissajous":
		set_lissajous()
	if flag == 1:
		fenetre.after(50, repetition)
		#debug, infinite loop

def set_square():
	"Square Movement !"
	global x, y, dx, dy

	x += dx
	y += dy

	if x > 280:
		x, dx, dy = 280, 0, 10
	if y > 280:
		y, dx, dy = 280, -10, 0
	if x < 20:
		x, dx, dy = 20, 0, -10
	if y < 20:
		y, dx, dy = 20, 10, 0

	can1.coords(oval1, x+r, y+r, x-r, y-r)
	


def set_zigzag():
	"Zig Zag Movement !"
	global x, y, dx, dy

	x += dx
	y += dy

	if x > 290:
		x = 290
		if y <= 150:
			dx, dy = -2, 7
		if y > 150:
			dx, dy = -2, -7
	if y > 290:
		y = 290
		if x <= 150:
			dx, dy = -5, -7
		if x > 150:
			dx, dy = 5, -7
	if x < 10:
		x = 10
		if y <= 150:
			dx, dy = 5, -7
		if y > 150:
			dx, dy = 5, 7
	if y < 10:
		y = 10
		if x <= 150:
			dx, dy = 5, 7
		if x > 150:
			dx, dy = -5, 7

	can1.coords(oval1, x+r, y+r, x-r, y-r)

def set_circle():
	"Circle Movement !"
	global x, y, ang

	ang += 0.1
	x, y = sin(ang), cos(ang)
	x, y = x*125+150, y*125+150

	can1.coords(oval1, x+r, y+r, x-r, y-r)

def set_lissajous():
	"Lissajous Movement !"
	global x, y, ang
	
	xp, yp, = x, y

	ang += 0.1
	x, y = sin(2*ang), cos(3*ang)
	x, y = x*125+150, y*125+150

	can1.coords(oval1, x+r, y+r, x-r, y-r)
	can1.create_line(xp, yp, x, y, fill =choice(COLORS)) 


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
	# print (fenetre.winfo_width())
	# print (fenetre.winfo_height())
	# print (fenetre.winfo_geometry())

x, y, r = 100, 100, 10 #données circle
dx, dy = 10, 0 #déplacement
move = None
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
boutCL = bouton(fenetre, "Circle", move_circle)
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
# -*- coding:Utf8 -*-
#utilisation de la correction pour la comprendre

#librairie
from tkinter import *

#variables
x, y, v, dx, dv, flag = 15, 15, 0, 6, 5, 0 #coordinates, speed and flag

#fonctions
def move():
	global x, y, v, dx, dv, flag
	xp, yp = x, y #mémorise les coordonées précédentes
	#déplacement horizontal
	if x > 385 or x < 15:
		dx = -dx
	x = x + dx
	#variation de la vitesse verticale (toujours vers le bas)
	v = v + dv
	#déplacement vertical (proportionel à la vitesse)
	y = y + v
	if y > 240:
		y = 240
		v = -v

	can.coords(balle, x+10, y+10, x-10, y-10)
	can.create_line(xp, yp, x, y, fill="light grey")

	if flag == 1:
		fen.after(50, move)

def start():
	global flag
	flag = 1
	if flag == 1:
		move()

def stop():
	global flag
	flag = 0

#programme
fen = Tk()
fen.title("Falling and Bouncing ball")
can = Canvas(fen, width = 400, height = 250, bg="white")
can.pack()
balle = can.create_oval(x+10, y+10, x-10, y-10, fill="red")
Button(fen, text="Start", command=start).pack(side="left", padx=10)
Button(fen, text="Stop", command=stop).pack(side="left")
Button(fen, text="Quitter", command=fen.quit).pack(side="right", padx=10, pady=5)
fen.mainloop()
# -*- coding:Utf-8 -*-
"click the ball game"

"""
-déplacement aléatoire de la balle dans le Canvas
-zigzag et rebond aléatoires
-10 secondes compteur avant que le jeu ne se termine
-changement de couleur lorsque la balle est cliqué et la vitesse de la balle augmente
-ajoute un point au score et remet le compter à 10 secondes
"""

from tkinter import *
from random import randint
import sys

#variables
WIDTH, HEIGHT = 400, 400
COLOR = ["blue", "red", "yellow", "green", "purple"]
x, y, r = 20, 50, 10 
v = 10

score = 0
flag = 0

#functions

def newGame():
	"reset score and ball speed"
	global score, flag, v, x, y
	score = 0
	flag = 1
	v = 10
	x, y = 200, 200
	moveBall()

def stopGame():
	global flag
	flag = 0

def moveBall():
	"ball movement"
	global x, y, v

	if x >
	x = x + v
	
	if 
	canBall.coords(ball, x+r, y+r, x-r, y-r)

	if flag == 1:
		root.after(50, moveBall)

def clickBall(event):
	"ball clicked by the player"
	global score
	color = COLOR[randint(0, len(COLOR)-1)]
	canBall.itemconfig(ball, fill=color)
	canScore.itemconfig(text, text="The score is : {}".format(score))
	score += 10

	if score == 100:
		flag = 0

def createCanvas(w, h, c):
	"Create the differents widgets"
	canva = Canvas(root, width=w, height=h, bg=c)
	#ball.bind()
	return canva

def setupGrid():
	"Put the different widgets on grid"
	canBall.grid(row=1, column=1, columnspan=3)
	canScore.grid(row=2, column=1, columnspan=3)

def setButtons():
	bStart = Button(text="New Game", command=newGame)
	bStop = Button(text="Stop", command=stopGame)
	bQuit = Button(text="Q", command=root.quit)
	bStart.grid(row=3, column=1)
	bStop.grid(row=3, column=2)
	bQuit.grid(row=3, column=3, pady=5)

def exitProgram(event):
	"leave the program"
	sys.exit()

def centerWindow():
	root.update_idletasks()
	width = root.winfo_width()
	height = root.winfo_height()
	x = (root.winfo_screenwidth()//2) - width // 2
	y = (root.winfo_screenheight()//2) - height // 2
	root.geometry("{}x{}+{}+{}".format(width, height, x, y))

#program

if __name__ == "__main__":
	root = Tk()
	root.title("Click the ball game")
	root.bind("<Escape>", exitProgram)

	canBall = createCanvas(WIDTH, HEIGHT, "light grey")
	ball = canBall.create_oval(x+r, y+r, x-r, y-r, fill=COLOR[0], width=2)
	canScore = createCanvas(400, 20, "light grey")
	text = canScore.create_text(200, 10, text="Score")
	canBall.tag_bind(ball, "<Button-1>", clickBall)

	setupGrid()
	setButtons()
	centerWindow()

	root.mainloop()
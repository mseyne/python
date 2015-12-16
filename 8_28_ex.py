# -*- coding:Utf-8 -*-
"click the ball game"

#libraries
from tkinter import *
from random import randint, choice
import sys
import tkinter.messagebox

#variables
WIDTH, HEIGHT = 400, 400
COLOR = ["blue", "red", "yellow", "green", "purple"]
STEPS = [-20, -15, -10, 10, 15, 20]
STEPSP = [10, 15, 20]
STEPSN = [-20, -15, -10]

x, y, r = 20, 50, 120 
dx, dy = 0, 0 #step x, step y
vitesse = 400

score = 0
flag = 0

#functions
def askNG():
	answer = tkinter.messagebox.askquestion("Play Again ?", "Do you want to play again ?")
	if answer == "yes":
		newGame()
	else:
		exitProgram(True)

def newGame():
	"reset score and ball speed"
	global score, flag, dx, dy, x, y, vitesse, r
	score = 0
	flag = 1
	dx, dy = choice(STEPS), choice(STEPS)
	x, y = 200, 200
	vitesse = 400
	r = 120
	canScore.itemconfig(text, text="Let's start ! Try to click the ball !")
	moveBall()

def stopGame():
	global flag
	flag = 0

def moveBall():
	"ball movement"
	global x, y, dx, dy

	if x >= 400:
		x = 400
		dx = choice(STEPSN)
		dy = choice(STEPS)
	
	if x <= 0:
		x = 0
		dx = choice(STEPSP)
		dy = choice(STEPS)

	if y >= 400:
		y = 400
		dy = choice(STEPSN)
		dx = choice(STEPS)

	if y <= 0:
		y = 0
		dy = choice(STEPSP)
		dx = choice(STEPS)

	x, y = x + dx, y + dy
	canBall.coords(ball, x+r, y+r, x-r, y-r)

	if flag == 1:
		root.after(vitesse, moveBall)
	if flag == 0:
		askNG()

def clickBall(event):
	"ball clicked by the player"
	global score, flag, vitesse, r
	if flag == 1:
		color = COLOR[randint(0, len(COLOR)-1)] # I could use simply choice(COLOR)
		canBall.itemconfig(ball, fill=color)
		score += 10
		canScore.itemconfig(text, text="The score is : {}".format(score))
		vitesse -= 35
		r -= 12
		if score == 100:
			flag = 0
	else:
		pass


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
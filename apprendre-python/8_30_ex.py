# -*- coding:Utf-8 -*-
"many balls moving and bouncing on each other"

#libraries
from tkinter import *
from sys import exit
from random import choice, randint

#datas
TITLE = "Bouncing Balls !"
COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise']

#global variables
gameBalls = {}
gameBallsPrevPositions = {}
gameBallsNewPositions = {}
gameBallsMovements = {}
flag = 0
nbBalls = 10
r = 10


#functions
def newGame():
	"clean the gameScreen and start a new game"
	global gameBalls
	gameScreen.delete('all')
	for i in gameBalls:
		gameScreen.delete(i)

	# create the balls of the game
	createBalls(nbBalls)


def moveBalls():
	"ball movements"
	
	# update previous position of the balls
	for i in gameBalls:
		gameBallsPrevPositions[i] = gameScreen.coords(gameBalls[i])

	print(gameBalls["ball1"], gameBallsPrevPositions["ball1"], gameBallsNewPositions["ball1"])

def createCanva(w, h, c="light grey"):
	return Canvas(root, width=w, height=h, bg=c)

def createBalls(ballNumber):
	"return a list of oval objects placed in gameScreen"
	b = 1

	while b <= ballNumber:
		color = choice(COLORS)
		x = randint(20, 580)
		y = randint(20, 580)
		ball = gameScreen.create_oval(x+r, y+r, x-r, y-r, fill=color)
		gameBalls["ball"+ str(b)] = ball
		b += 1

	for i in gameBalls:
		gameBallsNewPositions[i] = gameScreen.coords(gameBalls[i])

def setWindow():
	"used to set the window, title, center"
	root.update_idletasks()
	root.title(TITLE)
	root.bind("<Escape>", exitProgram)
	width = root.winfo_width()
	height = root.winfo_height()
	x = (root.winfo_screenwidth()//2)-width//2
	y = (root.winfo_screenheight()//2)-height//2
	root.geometry("{}x{}+{}+{}".format(width, height, x, y))

def setGrid():
	"used to set the game grid"
	gameScreen.grid(row=1, column=1, columnspan=3)
	textScreen.grid(row=2, column=1, columnspan=3)
	butNew.grid(row=3, column=1)
	butStart.grid(row=3, column=2, padx=5, sticky="w")
	butStop.grid(row=3, column=2, sticky="e")
	butQuit.grid(row=3, column=3, pady=5)

def exitProgram(event=1):
	exit()

def createButton(text, command):
	return Button(root, text=text, command=command)

def startMoving():
	"initiate the balls movement"
	global flag
	flag = 1
	moveBalls()

def stopMoving():
	"stop the balls movement"
	global flag
	if flag == 1:
		flag = 0


#program
if __name__ == "__main__":
	root = Tk()

	# main screen of the game
	gameScreen = createCanva(600, 600)

	# text screen of the game
	textScreen = createCanva(600, 50)


	# define the game button
	butNew = createButton("Start a new game", newGame)
	butStart = createButton("Start", startMoving)
	butStop = createButton("Stop", stopMoving)
	butQuit = createButton("Quit", root.quit)

	setGrid()
	setWindow()
	root.mainloop()
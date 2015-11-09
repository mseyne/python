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
import sys

#variables
WIDTH, HEIGHT = 400, 400
X, Y, R = 20, 50, 10 
COLOR = ["blue", "red", "yellow", "green", "purple"]

#functions

def newGame():
	"reset score and ball speed"
	pass

def moveBall():
	"ball movement"
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
	bStart = Button(text="Start", command=moveBall)
	bQuit = Button(text="Q", command=root.quit)
	bStart.grid(row=3, column=1)
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
	ball = canBall.create_oval(X+R, Y+R, X-R, Y-R, fill=COLOR[0])
	canScore = createCanvas(400, 20, "light grey")
	txtScore = canScore.create_text(200, 10, text="Score")

	setupGrid()
	setButtons()
	centerWindow()

	root.mainloop()
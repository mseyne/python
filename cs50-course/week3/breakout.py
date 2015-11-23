# -*- coding:Utf-8 -*-
"breakout game"

"""
One paddle, one bouncing ball and bricks
"""

#libraries
from tkinter import *
from random import choice

#datas
TITLE = "Breakout Game"

COLORS = [
'ivory', 'gainsboro', 'old lace', 'linen', 'papaya whip', 'blanched almond', 'bisque', 
'peach puff', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
'light blue', 'powder blue', 'pale turquoise'
]

WIDTH, HEIGHT = 400, 600

#variables
bricks = []

bx, by, br = 0, 0, 10 #ball coordinates and radius

px, py, pw, ph = 200, 580, 80/2, 16/2 #x y rectangle coordinates, half width and half height

#functions
def setGrid():
	gameScreen.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
	butNew.grid(row=1, column=0, padx= 5, pady= 10)
	butQuit.grid(row=1, column=2)


def configWindow():
	root.update_idletasks()
	width = root.winfo_width()
	height = root.winfo_height()
	x = (root.winfo_screenwidth()//2) - width//2
	y = (root.winfo_screenheight()//2) - height//2
	root.geometry("{}x{}+{}+{}".format(width, height, x, y))


#program
if __name__ == "__main__":
	root = Tk()
	root.title(TITLE)

	#create gamescreen
	gameScreen = Canvas(root, width=WIDTH, height=HEIGHT, bg=COLORS[0], highlightthickness=1, highlightbackground="black")
	
	#create button
	butQuit = Button(root, text="Quit", command=root.quit)
	butNew = Button(root, text="New Game")


	#create a rectangle that will serve as game paddle
	paddle = gameScreen.create_rectangle(px+pw, py+ph, px-pw, py-ph, fill="blue")
	

	setGrid()
	configWindow()

	root.mainloop()
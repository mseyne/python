# -*- coding: utf-8 -*-
"unicode characters table"

from tkinter import *
import sys

TITLE = "UNICODE CHARACTERS TABLE"


def setWindow():
	"center window"
	root.update_idletasks()
	width = root.winfo_width()
	height = root.winfo_height()
	x = (root.winfo_screenwidth()//2) - width//2
	y = (root.winfo_screenheight()//2) - height//2
	root.geometry("{}x{}+{}+{}".format(width, height, x, y))

def setGrid(ph):
	row = 1
	column = 1

	for i in ph:
		i.grid(row=row, column=column, sticky="w"+"e"+"n"+"s", padx = 5, pady = 5)
		column += 1
		if column%10 == 0:
			row +=1
			column = 1
	

def exit(event=1):
	sys.exit()

def getFrames():
	nb = 0
	PlaceHolder = []
	while nb < 20:
		frame = Frame(root, relief="ridge", bd=2, width=50, height=50)
		PlaceHolder.append(frame)
		nb += 1

	return PlaceHolder

def getLabels():
	pass


if __name__ == '__main__':
	root = Tk()
	root.title(TITLE)
	root.bind("<Escape>", exit)

	phList = getFrames() #place holder list
	chList = getLabels() #unicode character list
	setGrid(phList)
	setWindow()
	root.mainloop()
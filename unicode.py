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
	root.resizable(0,0)

def setGrid(ph):
	row = 1
	column = 1

	for i in ph:
		i.grid(row=row, column=column, sticky="w"+"e"+"n"+"s", padx = 5, pady = 5)
		column += 1
		if column%35 == 0:
			row +=1
			column = 1
	

def exit(event=1):
	sys.exit()

def getCanvas():
	nb = 0
	placeHolder = []
	while nb < 600:
		canva = Canvas(root, relief="ridge", bd=2, width=30, height=30)
		placeHolder.append(canva)
		nb += 1

	return placeHolder

def getTexts(can):
	nb = 0
	charList = []

	for i in can:
		i.create_text(15, 15, text=chr(nb))
		nb += 1


if __name__ == '__main__':
	root = Tk()
	root.title(TITLE)
	root.bind("<Escape>", exit)

	phList = getCanvas() #place holder list
	getTexts(phList) #unicode character list
	setGrid(phList)
	setWindow()
	root.mainloop()
# -*- coding:Utf-8 -*-

#libraries
from tkinter import *
import sys

#datas
ALPHA = "abcdefghijklmnopqrstuvwxyz"
NUMER = "0123456789"
CHARA = "!?,.:/\&\"#'{([-|éèà_ç^@)=}-+*ù%"
SPACE = " "
LIMITS = [ALPHA, NUMER, CHARA, SPACE]

WIDTH, HEIGHT = 300, 100

TEXTS = [
"What encoding do you want to use ?",
"1 - Caesar Cipher ?",
"2 - Vigenere Cipher ?"
]

#variables

flag = "menu"

#functions

def configWindow():
	root.title("Cipher Encoding Decoding")
	root.resizable(0, 0)
	root.update_idletasks()
	width = root.winfo_width()
	height = root.winfo_height()
	x = (root.winfo_screenwidth()//2) - width//2
	y = (root.winfo_screenheight()//2) - height//2
	root.geometry("{}x{}+{}+{}".format(width, height, x, y))

def exit(event):
	sys.exit()

def setGrid():
	"set the grid"
	cipherScreen.grid(row="0", column="0", columnspan="2", padx=10, pady=10)
	entryScreen.grid(row="1", column="0", columnspan="2", padx=0, pady=10)
	entry.grid(row="0", column="0", padx=10, pady=5)
	butOk.grid(row="0", column="1", padx=10)
	butQt.grid(row="0", column="2", padx=10)

def menu():
	"start menu, user choose cipher"
	global flag
	flag = "menu"
	cipherScreen.create_text(WIDTH/2, HEIGHT/2, text=TEXTS[0])
	cipherScreen.create_text(WIDTH/2, HEIGHT/2+20, text=TEXTS[1])
	cipherScreen.create_text(WIDTH/2, HEIGHT/2+40, text=TEXTS[2])

def redirection():
	"redirect command depending flag"
	action = enTxt.get()
	if flag=="menu":
		print("You choose,", action)



#progam
if __name__ == "__main__":
	root = Tk()
	root.bind('<Escape>', exit)
	# main screen
	cipherScreen = Canvas(root, width=WIDTH, height=HEIGHT, bg="ivory")
	# entry screen
	entryScreen = Frame(root, width=WIDTH, height=HEIGHT/3)

	# create entry
	enTxt = StringVar()
	entry = Entry(entryScreen, textvariable=enTxt, width=30, borderwidth=3, relief="groove")


	# create buttons
	butOk = Button(entryScreen, text="Ok", command=redirection)
	butQt = Button(entryScreen, text="Quit", command=root.quit)

	if flag == "menu":
		menu() #choose action, caesar or vigenere
	
	setGrid()
	configWindow()
	root.mainloop()
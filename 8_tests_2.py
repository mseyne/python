# -*- coding:Utf-8 -*-

from tkinter import *

W, H = 300, 300

def delCan():
	can1.pack_forget()

def callCan():
	can1.pack()

fen1 = Tk()

can1 = Canvas(fen1, bg="dark grey", width = W, height = H)
can1.pack()

bou1 = Button(fen1, text="Delete Canvas", command=delCan)
bou1.pack()
bou3 = Button(fen1, text="Canvas", command=callCan)
bou3.pack()
bou2 = Button(fen1, text="Quitter", command=fen1.quit)
bou2.pack()

fen1.mainloop()
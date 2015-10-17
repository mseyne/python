# -*- conding:Utf-8 -*-

from tkinter import *
from random import randrange



COUL = ['dark gray', 'purple', 'cyan', 'maroon', 'green', 'red', 'blue', 'orange', 'yellow']

WDT1, HGT1 = 400, 500
WDT2, HGT2 = 800, 100

def cercle(x, y, r, coul = 'black'):
	pass

def figure_1():
	pass

def figure_2():
	pass

source = Tk()
#source.geometry

fra1 = Frame(source, bg=COUL[5],  width=WDT1, height=HGT1).pack(side="left")
fra2 = Frame(source, bg=COUL[2],  width=WDT1, height=HGT1).pack(side="right")
fra3 = Frame(source, bg=COUL[4],  width=WDT2, height=HGT2).pack(side="bottom")
#fra4 = Frame(source, bg=COUL[5],  width=WDT1, height=HGT1).pack(side="right")

# fen1 = Canvas(source, bg=COUL[5],  width=WDT2, height=HGT2).pack(side="top")
# fen2 = Canvas(source, bg=COUL[2],  width=WDT2, height=HGT2).pack(side="left")
# fen3 = Canvas(source, bg=COUL[4],  width=WDT2, height=HGT2).pack(side="right")
# fen4 = Canvas(source, bg=COUL[8],  width=WDT2, height=HGT2).pack(side="bottom")

# text1 = Label(fen1, text="1").pack()
# text2 = Label(fen2, text="2").pack()
# text3 = Label(fen3, text="3").pack()
# text4 = Label(fen4, text="4").pack()

#bou1 = Button(fen2, text="Quitter", command=source.quit).pack()


source.mainloop()
source.destroy()
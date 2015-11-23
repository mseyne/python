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

#variables

#objects
class Window(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent, background="grey")
		self.parent = parent
		self.initUI()
		self.configWindow()

	def initUI(self):
		self.parent.title("Cipher Encoding Decoding")
		self.pack(fill=BOTH, expand=1)

	def configWindow(self):
		self.parent.update_idletasks()
		width = self.parent.winfo_width()
		height = self.parent.winfo_height()
		x = (self.parent.winfo_screenwidth()//2) - width//2
		y = (self.parent.winfo_screenheight()//2) - height//2
		self.parent.geometry("{}x{}+{}+{}".format(width, height, x, y))

	def exit():
		sys.exit()


#functions
def start():
	root = Tk()
	window = Window(root)
	root.mainloop()

def setButton():
	pass

#progam
if __name__ == "__main__":
	start()
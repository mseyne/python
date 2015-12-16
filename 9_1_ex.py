# -*- coding:utf-8 -*-
"write and read"

from os import remove

INFO = [
"What do you want to do?",
"1. Read a file.",
"2. Create a new file.",
"3. Add text in a file.",
"5. Leave program.",
"What is the name of the file you want to read?",
"What is the name of the file you want to create?",
"What is the name of the file in which you want to write?",
"What text do you want to write in the file?",
"This file already exist.",
"This file does not exist.",
"4. Remove a file.",
"What is the name of the file to remove?"
]

def question():
	print(INFO[0])
	print(INFO[1]) 
	print(INFO[2])
	print(INFO[3])
	print(INFO[11])
	print(INFO[4])

def menu():
	"ask user an action"
	question()

	while 1:
		answer = input(">>>")
		if answer == '1':
			readFile()
			question()
		if answer == '2':
			createFile()
			question()
		if answer == '3':
			appendFile()
			question()
		if answer == '4':
			removeFile()
			question()
		if answer == '5':
			break
		else:
			print("Please choose between 1 and 5.")

def readFile():
	print(INFO[5])
	fileInput = input(">>>")
	if existCheck(fileInput):
		rfile = open(fileInput)
		print(rfile.read())
		rfile.close()
	else:
		print(INFO[10])

def createFile():
	print(INFO[6])
	fileInput = input(">>>")
	if existCheck(fileInput):
		print(INFO[9])
	else:
		cfile = open(fileInput, 'w')
		cfile.close()

def appendFile():
	print(INFO[7])
	fileInput = input(">>>")
	if existCheck(fileInput):
		print(INFO[8])
		write = 1
		rfile = open(fileInput, 'a')
		while write:
			textInput = input(">>>")
			if len(textInput) == 0:
				write = 0
				rfile.close()
			else:
				rfile.write(textInput+'\n')
	else:
		print(INFO[10])

def removeFile():
	"remove the file"
	print(INFO[12])
	fileInput = input(">>>")
	if existCheck(fileInput):
		remove(fileInput)
		print(fileInput, "removed.")
	else:
		print(INFO[10])

def existCheck(fname):
	"check if the file exist with exception error try except"
	try:
		f = open(fname)
		f.close()
		return 1
	except:
		return 0


if __name__ == "__main__":
	menu()
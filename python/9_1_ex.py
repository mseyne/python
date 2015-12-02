# -*- coding:utf-8 -*-
"script qui propose de lire et écrire des fichiers"

INFO = [
"What do you want to do?",
"1. Read a file.",
"2. Create a new file.",
"3. Add text in a file.",
"4. Leave program.",
"What is the name of the file?"
]

def menu():
	"ask user an action"
	print(INFO[0])
	print(INFO[1]) 
	print(INFO[2])
	print(INFO[3])
	print(INFO[4])
	
	while 1:
		answer = input(">>>")
		if answer == '1':
			readFile()
		if answer == '2':
			createFile()
		if answer == '3':
			appendFile()
		if answer == '4':
			break
		else:
			print("Please choose between 1 and 4.")

def readFile():
	print(INFO[5])
	fileName = input("")
	pass

def createFile():
	pass

def appendFile():
	pass

def existCheck():
	"check if the file exist with exception error try except"


if __name__ == "__main__":
	menu()
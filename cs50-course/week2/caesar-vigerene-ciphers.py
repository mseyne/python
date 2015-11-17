# -*- coding: utf-8 -*-

#libraries
import sys
import os


#datas
TITLE = "-----------------------\nCRYPTOGRAPHY ALGORITHMS\n-----------------------"

ALNUM = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
ALPHA = "abcdefghijklmnopqrstuvwxyz"
NUMERIC = "1234567890"

INFO = [
"What cipher do you want to use ?",
"1 : The Caesar cipher ?",
"2 : The Vigenère cipher ?",
"3 : No, thank you, bye.",
"Do you want to encode a text or decode a cipher ?",
"1 : Encode text.",
"2 : Decode cipher.",
"What is the text you wish to encode ?",
"What is the shift you want to use ? (type 0 to get them all)",
"What cipher do you want to decode ?",
"What is the shift of the cipher ? (if you don't know, type 0)",
"You can use only the alphabetic characters.",
"You can use only the numerical characters."
]

PROMPT = '>>>'

#variables



#fonctions
def string(limits):
	"ask for the user to give a short input"
	question = 1
	while question:
		answer = input(PROMPT)
		if answer in list(limits):
			return answer
		else:
			print("You can write ", end="")
			for i in limits:
				print("'", i, sep="", end="")
			print(".")


def longString(limits, caution):
	"ask for the user to give a long input"
	question = 1
	while question:
		flag = 1
		answer = input(PROMPT).lower()
		for i in answer:
			if i not in list(limits):
				flag = 0
			if i == " ":
				flag = 1
		if flag == 1:
			return answer
		else:
			print(caution)


def datasCaesar():
	"get the datas from the user"
	action = menu2()
	
	if action == "1":
		print(INFO[7])
		text = longString(ALPHA, INFO[11]) 
		print(INFO[8])
		shift = longString(NUMERIC, INFO[12])
		encodeCaesar(text, shift)
		return False
	
	if action == "2":
		print(INFO[9])
		text = longString(ALPHA, INFO[11]) 
		print(INFO[10])
		shift = longString(NUMERIC, INFO[12])
		decodeCaesar(text, shift)
		return False

def encodeCaesar(text, shift=0):
	"encode the datas from the user"
	encoding = []
	print("your text", text, "your shift", shift)

def decodeCaesar(ciphertext, shift=0):
	"decode the datas from the user"
	decoding = []
	print("your text", ciphertext, "your shift", shift)

def displayCaesar():
	"print out all the shifts 1: 2: .. 26:"


def datasVigenere():
	"get the datas from user"
	action = menu2()
	if action == "1":
		cipher = encodeVigenere()
	if action == "2":
		cipher = decodeVigenere()

def encodeVigenere():
	print("let's encode Vigenère cipher!")
	return False

def decodeVigenere():
	print("let's decode Vigenère cipher!")
	return False

def displayVignere():
	"display the datas encoded or decoded from the user"
	pass

def menu2():
	"ask for encoding or decoding"
	print(INFO[4])
	print(INFO[5])
	print(INFO[6])
	answer = string('12')
	return answer



def menu():
	"ask user a cryptography algorithm"
	os.system('cls')
	print(TITLE)
	print(INFO[0])
	print(INFO[1])
	print(INFO[2])
	print(INFO[3])

	cipher = True
	while cipher:
		answer = string('123Qq')
		if answer == '1':
			cipher = datasCaesar()
		elif answer == '2':
			cipher = datasVigenere()
		elif answer in list("3Qq"):
			sys.exit()


if __name__ == '__main__':
	menu()

# -*- coding: utf-8 -*-

#libraries
import sys
import os


#datas
TITLE = "-----------------------\nCRYPTOGRAPHY ALGORITHMS\n-----------------------"

ALNUM = "ABCDEFGHIJKLMONPQRSTUVWXYZ0123456789"

TEXTS = [
"What cipher do you want to use ?",
"1 : The Caesar cipher ?",
"2 : The Vigenère cipher ?",
"3 : No, thank you, bye.",
"Do you want to encode a text or decode a cipher ?",
"1 : Encode text.",
"2 : Decode cipher."
]

PROMPT = '>>>'

#variables



#fonctions
def string(limits):
	"ask for the user to give an input"
	question = 1
	while question:
		answer = input(PROMPT)
		if answer in list(limits):
			return answer
		else:
			print("Vous pouvez écrire ", end="")
			for i in limits:
				print("'", i, sep="", end="")
			print(".")


def encodeCaesar():
	"possibility to choose the shift or see the 26 possibilities"
	print("let's encode caesar cipher!")
	return False

def decodeCaesar():
	print("let's decode caesar cipher!")
	return False

def displayCaesar():
	"print out all the shifts 1: 2: .. 26:"

def encodeVigenere():
	print("let's encode Vigenère cipher!")
	return False

def decodeVigenere():
	print("let's decode Vigenère cipher!")
	return False

def menu2():
	"ask for encoding or decoding"
	print(TEXTS[4])
	print(TEXTS[5])
	print(TEXTS[6])
	answer = string('12')
	return answer



def menu():
	"ask user a cryptography algorithm"
	os.system('cls')
	print(TITLE)
	print(TEXTS[0])
	print(TEXTS[1])
	print(TEXTS[2])
	print(TEXTS[3])

	cipher = True
	while cipher:
		answer = string('123Qq')
		if answer == '1':
			action = menu2()
			if action == "1":
				cipher = encodeCaesar()
			if action == "2":
				cipher = decodeCaesar()
		elif answer == '2':
			action = menu2()
			if action == "1":
				cipher = encodeVigenere()
			if action == "2":
				cipher = decodeVigenere()
		elif answer in list("3Qq"):
			sys.exit()


if __name__ == '__main__':
	menu()

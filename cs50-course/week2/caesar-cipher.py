# coding: latin-1


#libraries
import sys
import os


#datas
TITLE = "-----------------------\nCRYPTOGRAPHY ALGORITHMS\n-----------------------"

ALNUM = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
ALPHA = "abcdefghijklmnopqrstuvwxyz"
NUMERIC = "1234567890"
MINUS = "-"
SPACE = " "

INFO = [
"What cipher do you want to use ?",
"1 : The Caesar cipher ?",
"2 : The Vigenère cipher ?",
"3 : No, thank you, bye.",
"Do you want to encode a text or decode a cipher ?",
"1 : Encode text.",
"2 : Decode cipher.",
"What is the text you wish to encode ?",
"What is the shift you want to use ? (type enter to get them all)",
"What cipher do you want to decode ?",
"What is the shift of the cipher ? (if you don't know, type enter)",
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
			if i == SPACE: #Exception for " "
				flag = 1
			if i == MINUS and answer[0] == MINUS: #Exception for "-"
				flag = 1
			if i == "":
				flag = 1
		if flag == 1:
			if answer == "":
				answer = "0"
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
		encodeCaesar(text, shift)
		return False

def encodeCaesar(text, shift):
	"encode the datas from the user"
	encoding = []
	cipher = ""
	s = 0 # 26 shifts counter

	if shift !="0":
		for letter in text:
			if letter == SPACE:
				encoding.append(SPACE)
			else:
				index = ALPHA.index(letter) #get the index letter
				encoding.append(shiftIndex(index, shift)) #add to cipher new letter
		for letter in encoding:
			cipher += letter #build the cipher from encoding list
		print(cipher) #return cipher

	elif shift == "0":
		for letter in text: 
			while s < 26:  #same than before, but do it for the 26 shifts
				if letter == SPACE:
					encoding.append((letter+str(s), SPACE)) #add to encoding " "
				else:	
					index = ALPHA.index(letter)
					encoding.append((letter+str(s), shiftIndex(index, s)))
				s += 1
			s = 0
		displayCaesar(text, encoding) #return 26 ciphers


def shiftIndex(index, shift):
	"move index letter from shift given and return new letter"
	newIndex = (int(index) + int(shift))%26
	return (ALPHA[newIndex])
	
def decodeCaesar(ciphertext, shift=0):
	"decode the datas from the user"
	decoding = []
	print("your text", ciphertext, "your shift", shift)

def displayCaesar(text, codetable):
	"print out all the shifts 1: 2: .. 26:"
	wordList = []
	c = 0

	while c < 26:
		wordList.append([c])
		for code in codetable:
			if int(code[0][1:]) == c:
				wordList[c].append(code[1])
		c += 1

	for word in wordList:
		print("shift", word[0], ":", end=" ")
		c = 1
		newWord = ""
		while c <= len(text):
			newWord += word[c] 
			c+=1
		print(newWord)


def datasVigenere():
	"get the datas from user"
	action = menu2()
	if action == "1":
		cipher = encodeVigenere()
	if action == "2":
		cipher = decodeVigenere()

def encodeVigenere():
	print("let's encode Vigenère cipher!")
	print("no implemented yet :(")
	return False

def decodeVigenere():
	print("let's decode Vigenère cipher!")
	print("no implemented yet :(")
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
	

# coding: latin-1

"""
-restart the displayCaesar code, too much confuse method
"""

#libraries
import sys
import os


#datas
TITLE = "-----------------------\nCRYPTOGRAPHY ALGORITHMS\n-----------------------"

ALNUM = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
ALPHA = "abcdefghijklmnopqrstuvwxyz"
NUMERIC = "1234567890"
MINUS = "-"

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
		decodeCaesar(text, shift)
		return False

def encodeCaesar(text, shift):
	"encode the datas from the user"
	encoding = []
	cipher = ""
	c = 0

	if shift !="0":
		for i in text:
			index = ALPHA.index(i)
			encoding.append(shiftCaesar(index, shift))

		for letter in encoding:
			cipher += letter
		print(cipher)

	elif shift == "0":
		for i in text:
			while c < 26:
				index = ALPHA.index(i)
				shift = c
				encoding.append((i+str(c),shiftCaesar(index, shift)))
				c += 1
			c = 0
		print(encoding)
		displayCaesar(text, encoding)




def shiftCaesar(index, shift):
	"move index letter from shift given"
	newIndex = (int(index) + int(shift))%26
	return (ALPHA[newIndex])
	
def decodeCaesar(ciphertext, shift=0):
	"decode the datas from the user"
	decoding = []
	print("your text", ciphertext, "your shift", shift)

def displayCaesar(text, codetable):
	"print out all the shifts 1: 2: .. 26:"
	wordList = []
	word = 0
	c = 0
	lenght = 26

	print(codetable)


	for i in text:
		while c < lenght:
			if word == 0:
				wordList.insert(c, codetable[c][1])
				word = 1
			wordList[c] += codetable[c][1]
			c += 1
		lenght += 26

	print(wordList)



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

text = "aze"
code = [
('a0', 'a'), ('a1', 'b'), ('a2', 'c'), ('a3', 'd'), ('a4', 'e'), ('a5', 'f'), ('a6', 'g'), ('a7', 'h'), ('a  8', 'i'), 
('a9', 'j'), ('a10', 'k'), ('a11', 'l'), ('a12', 'm'), ('a13', 'n'), ('a14', 'o'), ('a15', 'p'), (  'a16', 'q'), 
('a17', 'r'), ('a18', 's'), ('a19', 't'), ('a20', 'u'), ('a21', 'v'), ('a22', 'w'), ('a23', 'x'  ), ('a24', 'y'), 
('a25', 'z'), ('z0', 'z'), ('z1', 'a'), ('z2', 'b'), ('z3', 'c'), ('z4', 'd'), ('z5', 'e'),   ('z6', 'f'), ('z7', 'g'), 
('z8', 'h'), ('z9', 'i'), ('z10', 'j'), ('z11', 'k'), ('z12', 'l'), ('z13', 'm'),   ('z14', 'n'), ('z15', 'o'), 
('z16', 'p'), ('z17', 'q'), ('z18', 'r'), ('z19', 's'), ('z20', 't'), ('z21', '  u'), ('z22', 'v'), ('z23', 'w'), 
('z24', 'x'), ('z25', 'y'), ('e0', 'e'), ('e1', 'f'), ('e2', 'g'), ('e3', '  h'), ('e4', 'i'), ('e5', 'j'), ('e6', 'k'), 
('e7', 'l'), ('e8', 'm'), ('e9', 'n'), ('e10', 'o'), ('e11', 'p'  ), ('e12', 'q'), ('e13', 'r'), ('e14', 's'), ('e15', 't'), 
('e16', 'u'), ('e17', 'v'), ('e18', 'w'), ('e19',   'x'), ('e20', 'y'), ('e21', 'z'), ('e22', 'a'), ('e23', 'b'), 
('e24', 'c'), ('e25', 'd')
]


if __name__ == '__main__':
	#menu()
	

	displayCaesar(text, code)


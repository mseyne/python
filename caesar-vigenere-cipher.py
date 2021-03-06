# -*- coding:Utf-8 -*-

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
"What is the shift you want to use ? (type enter to get them all)",
"What cipher do you want to decode ?",
"What is the shift which have been used for the cipher ? (if you don't know, type enter)",
"You can use only the alphabetic characters in one unique word.",
"You can use only the numerical characters (negative number accepter).",
"What is the key word that will encode your text?",
"What is the key word that will decode your cipher?"
]

PROMPT = '>>>'

#variables



#fonctions
def string(limits):
	"ask for the user to give a short input"
	while True:
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
	while True:
		flag = 1
		check = list(limits)
		
		answer = getInput()

		if answer == "":
			return "0"

		for i in answer:
			if i in check:
				pass
			elif "1" in check and i == '-' and answer[0] == '-': #Exception for "-"
				pass
			else:
				print(caution)
				flag = 0
				break

		if flag == 1:
			return answer


def getInput():
	"ask for the user to give a long input"
	answer = input(PROMPT).lower()
	return answer
		

def datasCaesar():
	"get the datas from the user"
	action = menuAction()
	
	if action == "1":
		print(INFO[7])
		text = getInput() 
		print(INFO[8])
		shift = longString(NUMERIC, INFO[12])
		encodeCaesar(text, shift, '1')
		return False
	
	if action == "2":
		print(INFO[9])
		text = getInput()
		print(INFO[10])
		shift = longString(NUMERIC, INFO[12])
		encodeCaesar(text, shift, '2')
		return False


def encodeCaesar(text, shift, action):
	"encode the datas from the user"
	print("let's encode Caesar cipher!")
	print('===========================', "\nYour text is :", text + ". Your shift is :", shift+".")
	encoding = []
	cipher = ""
	s = 0 # 26 shifts counter

	#shift become negative if the action is decoding
	if action == '2' and shift != "0":
		shift = -int(shift)

	wordToEncode = ''

	#make one word of the user input
	for letter in text:
		if letter in list(ALPHA):
			wordToEncode += letter

	if shift !="0":
		for letter in wordToEncode:
			index = ALPHA.index(letter) #get the index letter
			cipher += shiftIndex(index, shift) #add to cipher new letter
		
		newText = ""
		pos = 0

		#rebuild the complete sentence
		for letter in text:
			if letter in list(ALPHA):
				newText += cipher[pos]
				pos += 1
			else:
				newText += letter
		print("Your cipher is :", newText) #return cipher

	if shift == "0":
		for letter in wordToEncode: 
			while s < 26:  #same than before, but do it for the 26 shifts
				index = ALPHA.index(letter)
				encoding.append((letter+str(s), shiftIndex(index, s)))
				s += 1
			s = 0
		displayCaesar(text, encoding) #return 26 ciphers


def shiftIndex(index, shift):
	"move index letter from shift given and return new letter"
	newIndex = (int(index) + int(shift))%26
	return (ALPHA[newIndex])
	
# def decodeCaesar(ciphertext, shift=0):
# 	"decode the datas from the user"
# 	decoding = []
# 	print("your text", ciphertext, "your shift", shift)


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
		newWord = ""
		pos = 1
		for letter in text:
			if letter in list(ALPHA):
				newWord += word[pos]
				pos += 1
			else:
				newWord += str(letter)
		print("shift", word[0], ":", end=" ")
		print(newWord)


def datasVigenere():
	"get the datas from user"
	action = menuAction()
	
	if action == "1":
		print(INFO[7])
		text = getInput() 
		print(INFO[13])
		key = longString(ALPHA, INFO[11])
		encodeVigenere(text, key, '1')
		return False
	
	if action == "2":
		print(INFO[9])
		text = getInput() 
		print(INFO[14])
		key = longString(ALPHA, INFO[11]) 
		encodeVigenere(text, key, '2')
		return False

def encodeVigenere(text, key, action):
	print("let's encode Vigenère cipher!")
	print('=============================', "\nYour text is :", text + ". Your key is :", key+".")

	#take a one string lowered and build the key along this with key banane ex = string, jesuiscontent, key, bananebananeb
	#convert the string along the shift for each letter of the key word
	wordToEncode = ""
	#take the user input and build the world with letter checked ready for encoding
	for character in text:
		if character in ALPHA:
			wordToEncode += character
	# print(wordToEncode)

	#create a keyword using the key of the same lenght than the variable wordToEncode
	keyword = ""
	pos = 0 #index position
	for letter in wordToEncode:
		keyword += key[pos % len(key)]
		pos += 1
	# print(keyword)

	#take the index of each letter of the keyword which will serve as shift for the wordToEncode lettes and build a list
	shiftsList = []
	for letter in keyword:
		shiftsList.append(ALPHA.index(letter))
	# print(shiftsList)

	#shift each letter from wordToEncode with the integer of the same index in shiftsList
	newWord = ""
	pos = 0 #index position
	while pos < len(wordToEncode):
		letterIndex = ALPHA.index(wordToEncode[pos])
		shift = shiftsList[pos]
		# print("letter:", wordToEncode[pos], "index:", letterIndex, "shift", shift)
		if action == "1": #encoding
			newIndex = (letterIndex + shift) % 26
		if action == "2": #decoding
			newIndex = (letterIndex - shift) % 26
		newLetter = ALPHA[newIndex]
		# print("newIndex", newIndex, "newletter", newLetter)
		newWord += newLetter
		pos+=1

	#rebuild the sentence (with space and others character) 
	newText = ""
	pos = 0 #index position
	for letter in text:
		if letter in list(ALPHA):
			newText += newWord[pos]
			pos += 1
		else:
			newText += letter

	print("Your cipher is :", newText, end='\n=============================\n')

	#return
	return False

# def decodeVigenere(text, key):
# 	print("let's decode Vigenère cipher!")
# 	print("no implemented yet :(")
# 	return False

def displayVignere():
	"display the datas encoded or decoded from the user"
	pass

def menuAction():
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


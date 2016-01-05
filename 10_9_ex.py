# -*- config:Utf-8 -*-
"check if user input is a number"

NUMBERS = list("1234567890")

def estUnChiffre(data):
	check = 0
	for char in data:
		if char in NUMBERS:
			check += 1

	if check == len(data):
		return "vrai"
	else:
		return "faux"


userInput = input("Choisissez un caractère à vérifier\n>>>")

answer = estUnChiffre(userInput)

print("Il est", answer, "que", userInput, "est un nombre.")
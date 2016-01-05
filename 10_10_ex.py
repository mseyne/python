# -*- config:Utf-8 -*-
"check if user input is upperCase"

UPPERCASE = list("azertyuiopqsdfghjklmwxcvbnéèàçù".upper())

def aUneMaj(data):
	check = 0
	for char in data:
		if char in UPPERCASE:
			check += 1

	if check > 0:
		return "vrai"
	else:
		return "faux"


userInput = input("Choisissez un texte à vérifier\n>>>")

answer = aUneMaj(userInput)

print("Il est", answer, "que '" + userInput + "' contient au moins une majuscule.")
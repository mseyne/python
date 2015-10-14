# -*- coding:Utf-8 -*-

def inverse(ch):
	phrase = ""
	for i in range(len(ch)-1, -1, -1):
		phrase += ch[i]
	return phrase


phrase = input("Choisissez une phrase que vous souhaitez inverser:\n>>>")
phrInv = inverse(phrase)

print("Votre phrase inversé ressemble à ça :", phrInv, end='.\n\n')
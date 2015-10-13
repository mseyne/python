# -*- coding:Utf:8 -*-

def compteCar(ca, ch):
	nb = 0
	for i in ch:
		if ca == i:
			nb += 1
	return nb

phrase = input("Tapez un mot ou une phrase.\n>>>")
lettre = input("Tapez une lettre que vous souhaitez vérifier.\n")

print(phrase, lettre)
print("il y a", compteCar(lettre, phrase), "fois la lettre", lettre, "dans la phrase", phrase, end='.\n')
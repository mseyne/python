# -*- coding:Utf:8 -*-

def sep(vs):
	x = []
	for i in vs:
		x.append(eval(i))
	return x

def plusGrand(n1, n2, n3):
	x = 0
	if n1 > x :
		x = n1
	if n2 > x :
		x = n2
	if n3 > x :
		x = n3
	return x


valeurs = input("Choisissez trois nombres séparé par des virgules :\n>>> ").split(",")
valeurs = sep(valeurs)
plus_grand = plusGrand(valeurs[0], valeurs[1], valeurs[2])
print("La valeur la plus grande des trois nombres est", plus_grand, end=".\n")
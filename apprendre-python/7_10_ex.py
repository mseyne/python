# -*- coding:Utf:8 -*-

nb = 0
print(type(nb))

def indexMax(liste):
	global nb
	for i in liste:
		if int(i) > nb:
			nb = i
	return nb


listNb = input("Donnez une liste de nombres séparé par des virgules").split(",")
indexMax(listNb)
print("Le nombre le plus grand de la liste", listNb, "est", nb, end=".\n")
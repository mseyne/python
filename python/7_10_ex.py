# -*- coding:Utf:8 -*-

nb = 0

def nbMax(liste):
	global nb
	for i in liste:
		i = int(i)
		if i > nb:
			nb = i
	return nb


def indexMax(lt, nb):
	nb = str(nb)
	return lt.index(nb)


listNb = input("Donnez une liste de nombres séparé par des virgules.\n>>>").split(",")
nbMax(listNb)
print("\nLe nombre le plus grand de la liste", listNb, "est", nb, end=".\n")
index = indexMax(listNb, nb)
print("\nL'index du nombre", nb, "dans la liste", listNb, "est", index, end=".\n")
print("\n")
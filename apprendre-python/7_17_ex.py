# -*- coding:Utf-8 -*-
"Une fonction qui trie la valeur la plus grande à partir des bornes index données"

def mkInt(liste):
	nListe = []
	for i in liste:
		nListe.append(int(i))
	return nListe


def eleMax(liste, debut=0, fin=0):
	nbMax = 0
	c = debut
	f = fin

	if f <= c:
		f = len(liste)

	while c < f:
		if liste[c] > nbMax:
			nbMax = liste[c]
		c += 1

	return nbMax

# serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]
# print("Debug", eleMax(serie))
# print("Debug", eleMax(serie, 2, 5))
# print("Debug", eleMax(serie, 2))
# print("Debug", eleMax(serie, fin = 3, debut = 1))


listNb = input("Choisissez une liste de nombre séparé par des virgules.\n>>>").split(",")
depart = int(input("Choisissez l'index de départ :\n>>>"))
termine = int(input("Choisissez l'index de fin :\n>>>"))
listNb = mkInt(listNb) #Je fais une liste d'integer
print("Le nombre le plus grand entre l'index", depart, "et l'index", termine, "est\
", eleMax(listNb, depart, termine), end=".\n")
# -*- coding:Utf-8 -*-

def compteMots(ph):
	c = 0
	for i in ph:
		c += 1
	return c


phrase = input("Ecrivez plusieurs mots à la suite les uns avec les autres.").split()
nbMots = compteMots(phrase)

print("\nVous avez inscrit", nbMots, "mots.\n")
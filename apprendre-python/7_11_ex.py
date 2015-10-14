# -*- coding:Utf-8 -*-

MOIS = [None, "Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre",
"Novembre", "Décembre"]

def nomMois(nb):
	nb = int(nb)
	if nb <= 0 or nb > 12:
		print("Vous devez choisir entre 1 et 12.")
	else: 
		return MOIS[nb]

moisChx = input("Quel numéro de mois souhaitez vous trouver ?")
mois = nomMois(moisChx)

if mois == None:
	print("\n")
else:
	print("\nLe mois que vous cherchez est", mois, end=".\n\n")
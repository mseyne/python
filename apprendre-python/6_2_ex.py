# -*- coding:Utf-8 -*-

from math import sqrt

print("***\nCalcul du périmètre et l'aire d'un triangle\n***")
cotés = input("Donnez les trois coté du triangle séparé par des virgules\n>>>").split(",")
a, b, c = int(cotés[0]), int(cotés[1]), int(cotés[2])
d = (a + b + c)/2 #périmètre
aire = sqrt(d*(d-a)*(d-b)*(d-c))

print(cotés, a, b, c, type(cotés), type(c), d, round(aire, 2))

liste = []

while True:
    valeur = input("Quelle valeur souhaitez vous ajouter à la liste ?\
'Entrez' pour quitter\n>>>")
    if valeur == "":
        break
    liste.append(valeur)

print(liste)

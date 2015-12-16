# -*- coding:Utf-8 -*-

somme_versé = float(input("Quel sommes versez vous ?"))
taux_intérêts = float(input("Quel est l'intérêt annuel en pourcentage ?"))/100
nb_années = int(input("Nombre d'années ?"))
compteur = 0

while compteur <= nb_années:
    print("l'année", compteur, "la sommes plus intérêt est a :", somme_versé,
          "euros.")
    somme_versé = somme_versé + somme_versé * taux_intérêts
    compteur += 1

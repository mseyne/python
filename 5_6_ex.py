# -*- coding:Utf-8 -*-

texte_choisi = input("Quel texte souhaité vous vérifier les lettres ?")
lettre_vérifiée = input("Quelle lettre voulez vous vérifier ?")
compteur_lettre = 0

for i in texte_choisi.lower():
    if i == lettre_vérifiée.lower():
        compteur_lettre += 1

if compteur_lettre > 0:
    print("Il y a", compteur_lettre, lettre_vérifiée, "dans le texte :",
          texte_choisi)
else:
    print("Il n'y a pas de", lettre_vérifiée, "dans le texte :", texte_choisi)

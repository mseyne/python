# -*- coding:Utf-8 -*-

mot = input("Quel mot souhaitez vous transformer ?")
signe = input("Quel signe souhaitez vous intercaler ?")
nouveau_mot = ""
longueur = ""  #petite astuce avec len pour out of range

for i in mot:
    nouveau_mot += i + signe

print(nouveau_mot[0: len(nouveau_mot)-1])

nouveau_mot = ""

for i in range(len(mot)-1, -1, -1):
    nouveau_mot += mot[i]

print(nouveau_mot)
if nouveau_mot == mot:
    print("et il s'agit d'un palindrome !")
else:
    print("ce n'est pas un palindrome !")


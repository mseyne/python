# -*- coding:Utf-8 -*-

def changeCar(ch, ca1=" ", ca2="*", debut = 0, fin = 0):
	nPhrase = ""
	c = debut
	f = fin

	if f <= c:
		f = len(ch)

	while c < f:		
		if ch[c] == ca1:
			nPhrase += ca2
		else:
			nPhrase += ch[c]
		c += 1

	return nPhrase

#print("DEBUG", changeCar("Ceci est une longue phrase avec beaucoup d'espace !", "e", "3", 4, 20))

phrase = input("Choisissez une phrase :\n>>>")
caraMoin = input("Choisissez le caratère que vous souhaitez enlever :\n>>>")
caraPlus = input("Choisissez le caratère que vous souhaitez ajouter :\n>>>")

commence = int(input("À quel index souhaitez vous commencer?\n>>>"))
termine = int(input("À quel index souhaitez vous terminer?\n>>>"))

print("1:", changeCar(ch = phrase, ca1 = caraMoin, ca2 = caraPlus))
print("2:", changeCar(ch = phrase, ca1 = caraMoin, ca2 = caraPlus, debut = commence, fin = termine))
print("3:", changeCar(ch = phrase, ca1 = caraMoin, ca2 = caraPlus, debut = commence))
print("4:", changeCar(ch = phrase, ca1 = caraMoin, ca2 = caraPlus, fin = termine))
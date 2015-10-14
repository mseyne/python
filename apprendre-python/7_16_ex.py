# -*- coding:Utf-8 -*-

def changeCar(ch, ca1=" ", ca2="*", debut = 0, fin = 0):
	
	nPhrase = ""
	
	if fin <= 0:
		fin = len(ch)

	# for i in range(0, debut):
	# 	nPhrase += ch[i]

	for i in range(debut, fin+1):
		if ch[i] == ca1:
			nPhrase += ca2
		else:
			nPhrase += ch[i]

	# for i in range(fin, len(ch)):
	# 	nPhrase += ch[i]

	return nPhrase

phrase = input("Choisissez une phrase :\n>>>")
caraPlus = input ("Choisissez le caratère que vous souhaitez ajouter :\n>>>")
caraMoin = input ("Choisissez le caratère que vous souhaitez enlever :\n>>>")
commence = int(input("À quel index souhaitez vous commencer?\n>>>"))
termine = int(input("À quel index souhaitez vous terminer?\n>>>"))

print(changeCar(ch = phrase, ca1 = caraMoin, ca2 = caraPlus))
print(changeCar(ch = phrase, ca1 = caraMoin, ca2 = caraPlus, debut = commence, fin = termine))
print(changeCar(ch = phrase, ca1 = caraMoin, ca2 = caraPlus, debut = commence))
print(changeCar(ch = phrase, ca1 = caraMoin, ca2 = caraPlus, fin = termine))
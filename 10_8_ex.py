# -*- coding:Utf-8 -*-
"recherche le nombre d'occurence de caractères particulier dans une phrase données"

dictioCheck = {"é": 0, "è":0, "ë":0, "e":0, "ê":0}
caractCheck = list(dictioCheck.keys())
phraseCheck = input("Choose a sentence to check :\n>>>")
    
for letter in phraseCheck:
   	if letter in caractCheck:
	   	dictioCheck[letter] += 1

wordreturn = ""
noCarac = 0

for carac in caractCheck:
    if dictioCheck[carac] > 0:
        wordreturn += str(dictioCheck[carac]) + " lettre(s) " + carac + ", "
    if dictioCheck[carac] == 0:
    	noCarac += 1

if noCarac == 5:
	print("Dans la phrase", phraseCheck, "il n'y a pas les caractères recherchés.")
else:
	print("Dans la phrase", phraseCheck, "il y a " + wordreturn[:-2] + ".")


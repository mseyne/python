# -*- coding:Utf-8 -*-
"recherche le nombre d'occurence de caractères particulier dans une phrase données"

dictioCheck = {"é": 0, "è":0, "ë":0, "e":0, "ê":0}
caractCheck = list(dictioCheck.keys())
phraseCheck = input("Choose a sentence to check :\n>>>")
    
for letter in phraseCheck:
   	if letter in caractCheck:
	   	dictioCheck[letter] += 1

print("Dans la phrase", phraseCheck, "il y a ", end="")

wordreturn = ""
for carac in caractCheck:
    if dictioCheck[carac] > 0:
        wordreturn += str(dictioCheck[carac]) + " lettre(s) " + carac + ", "

print(wordreturn[:-2] + ".")


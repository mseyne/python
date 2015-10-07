# -*- coding:Utf-8 -*-

nom = input("Comment vous appelez vous ?")
sex = input("Êtes-vous un homme ou une femme ?")

print(sex)

if sex == "h" or sex == "homme":
    print("bonjour monsieur %s" % nom)
    print("h/homme")
else:
    print("bonjour madame {}".format(nom))

bornes = eval(input("Choisissez deux nombres, le deuxième plus grand \
que le premier :\n>>>"))
multiples = eval(input("Choisissez les deux multiples que vous souhaitez \
additionner :\n>>>"))
liste = []

for i in range(bornes[0], bornes[1]):
    if not i % multiples[0] or not i % multiples[1]:
        liste.append(i)

somme = 0

for i in liste:
    somme += i

print("la somme de", liste, "est égale à", somme)

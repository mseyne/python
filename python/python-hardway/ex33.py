# -*- coding: utf-8 -*-
# Python Hardway, Exercice 33, While Loops
# ex33.py
# This script introduce the while loop

def boucle(starting, limit, increment):
    count = 0
    number = starting
    numbers = []
    while count < limit:
#        print("%d :" % count)
#        print("At the top number is %d" % number)
        numbers.append(number)
        count = count + 1
        number += increment
#        print("Numbers now: ", numbers)
#        print("At the bottom count is %d" % number)
    return numbers

print("On souhaite remplir une liste d'une suite de nombre.")
print("On commence à partir de quel nombre ?")
start = int(input("> "))
print("On démarre de", start)
print("Combien de nombre ajoute t'on à la liste ?")
quantity = int(input("> "))
print("De combien on incrémente chaque nombre ?")
incr = int(input("> "))

numlist = boucle(start, quantity, incr)

print("The list of numbers: ")

#for num in numlist:
#print(numlist)
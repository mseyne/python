# -*- coding: utf-8 -*-
# Python Hardway, Exercice 16, Reading and Writing Files
# ex16.py
# This script erase or create a new file and write three lines of content

from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# crée un nouveau fichier ou écrase celui existant avec l'argument 'w'
targetw = open(filename, 'w')

print("Truncating the file. Goodbye!")
# efface le fichier, mais semble inutile car 'w' truncate déjà le fichier
#targetw.truncate()

print("Now I'm going to ask you for three lines.")
# demande à l'utilisateur les trois chaînes de caractères mise en trois variables
#line1 = input("line 1: ")
#line2 = input("line 2: ")
#line3 = input("line 3: ")
line1, line2, line3 = input("line1: "), input("line2: "), input("line3: ")

print("I'm going to write these to the file.")

# copie les trois variables dans le fichier et saute la ligne avec \n
# first try
# writeline = line1 + "\n" + line2 + "\n" + line3 + "\n"
# targetw.write(writeline)
# second try, clever one
targetw.write("%s\n%s\n%s\n" % (line1, line2, line3))

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
targetw.close()

# inspired ex15 script to read the new file
print("We check the result")
targetr = open(filename, 'r')
print(targetr)
print(targetr.read())

print("And finally, we close it.")
# fermer le fichier ouvert permet de récupérer la mémoire utilisé
targetr.close()
print('done!')
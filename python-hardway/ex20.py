# -*- coding: utf-8 -*-
# Python Hardway, Exercice 20, Functions and Files
# ex20.py
# This script open a file with three lines content and use
# fonction to read it, rewind it, and read it again line by line

from sys import argv

script, input_file = argv

# première fonction, print le contenu du fichier
def print_all(f):
    print(f.read())
    
# deuxième fonction, rembobine le fichier lu
def rewind(f):
    f.seek(0)
    
# troisième fonction, imprime une ligne du fichier
def print_a_line(line_count, f):
    print(line_count, f.readline(), end='')

# une quatrième fonction qui converti en string
# un compteur incrémenté et y ajoute ":"
def compteur_str(compteur_int):
    compteur = str(compteur_int) + ":"
    return compteur

# le fichier est ouvert et placé dans une variable
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

#current_line = 1
c = 1
current_line = compteur_str(c)
print_a_line(current_line, current_file)

#current_line = current_line + 1 # incrémentation de +1
c += 1
current_line = compteur_str(c)
print_a_line(current_line, current_file)

#current_line += 1 # incrémentation de +1
c += 1
current_line = compteur_str(c)
print_a_line(current_line, current_file)

current_file.close()
# -*- coding: utf-8 -*-
# Python Hardway, Exercice 13, Parameters, Unpacking, Variables
# ex13.py

from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
fourth = input("A fourth argument? ")
print("Your fourht variable is:", fourth)
print(type(first), type(second), type(third), type(fourth))
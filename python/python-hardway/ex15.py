# -*- coding: utf-8 -*-
# Python Hardway, Exercice 15, Reading Files
# ex15.py
# This script open a txt file and read it

from sys import argv 

script, filename = argv

txt = open(filename) # open the file fonction in a variable

print("Here's your file %r:" % filename) 
print(txt)
print(txt.read()) # read the file opened in the variable txt and print it
#txt = close(txt) # bug breaking the code
print(txt.read())

print("Type the filename again:") # repeat the operation using input fonction

file_again = input("> ") 

txt_again = open(file_again)

print(txt_again.read())
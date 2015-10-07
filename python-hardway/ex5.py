# -*- coding: utf-8 -*-
# Python Hardway, Exercice 5, More Variables and Printing
# ex05.py

name = 'Michaël Seyne'
age = 31 #not a lie?
height = 165 # centimètres
weight = 75 # kilogrammes
eyes = 'Bleu'
teeth = 'White'
hair = 'Brown'

print("Let's talk about %s." % name)
print("He is %r years old." % age)
print("He's %d inches tall." % height)
print("He's %d pounds heavy." % weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight))

# Drill
# Try to write some variables that convert the inches and pounds to centimeters and kilos.
# Do not just type in the measurements. Work out the math in Python.
# -*- coding: utf-8 -*-
# Python Hardway, Exercice 11, Asking Questions
# ex11.py

print("How old are you?", end=" ")
age = input()
print("How tall are you?", end=" ")
height = input()
print("How much do you weigh?", end=" ")
weight = input()

print("So, you're %s old, %s tall and %s heavy." % (
    age, height, weight))
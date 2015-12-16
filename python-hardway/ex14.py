# -*- coding: utf-8 -*-
# Python Hardway, Exercice 14, Prompting and Passing
# ex14.py

from sys import argv

script, user, ia  = argv
prompt = '-> '

print("Hello, I am %s the ghost in the computer." % ia)
print("Hi %s, I'm running %s script." % (user, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s" % user)
likes = input(prompt)

print("Where do you live %s?" % user)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print('''
      Alright, so you said %r about liking me.
      You live in %r. Not sure where that is.
      And you have a %r computer.
      \tNice.
      ''' % (likes, lives, computer))
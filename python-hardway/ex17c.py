# -*- coding: utf-8 -*-
# Python Hardway, Exercice 17 help, Create one file
# ex17c.py
# This script is used to created new files .txt and creating one line

from sys import argv

script, filename = argv
new_file = open(filename, 'w')

content = input('What do you want to write in this new file?\n> ')
content = content + '\n'

#new_file.write(content)
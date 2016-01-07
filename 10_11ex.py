# -*- coding:Utf-8 -*-
'convert a sentence in a list of words'

def convertToList(text):
  liste = text.split(' ')
  return liste

userData = input('choose a sentence\n>>>')

newList = convertToList(userData)

print(newList)

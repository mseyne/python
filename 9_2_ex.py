# -*- coding:Utf-8 -*-
#return the longer string from a file

wordlist = []
wordmax = ""

filename = open("myfile.txt", 'r')
for i, l in enumerate(filename):
	wordlist.append(l)

for word in wordlist:
	if len(word) > len(wordmax):
		wordmax = word

print(wordmax)

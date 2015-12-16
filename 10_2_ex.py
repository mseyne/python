# -*- coding:utf-8 -*-
"transform a string"

longString = input("Give a long sting.\n>>>")

def cutString(string):
	"cut the string in many parts"
	parts = []
	part = ""
	c = 0

	for char in string:

		part += char
		c+=1

		if c == len(string)//4:
			c = 0
			parts.append(part)
			part = ""
	
	if len(part) != len(string)//4 and len(part) > 0:
		parts.append(part)
	return parts


def buildNewString(stringList):
	"rebuild a string with the cut"
	c, d = 0, -1
	newString = ""
	while c < len(stringList):
		newString += stringList[d]
		c += 1
		d -= 1
	print(newString)

buildNewString(cutString(longString))
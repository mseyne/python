# -*- coding:Utf-8 -*-


def findChr(uistr, uich, start):
	"return the index of a character in a string"
	return uistr.find(uich, start)


# Test :
if __name__ == '__main__':
	strUserInput = input("A sting\n>>>")
	chrUserInput = input("A charactere\n>>>")
	findStart = input("Start from (default 0)\n>>>")
	if findStart == "":
		findStart = 0
	index = findChr(strUserInput, chrUserInput, int(findStart))
	if index > -1:
		print("The index of", chrUserInput, "in", strUserInput, "is",index)
	else:
		print("No", chrUserInput, "in", strUserInput)
# -*- coding:Utf:8 -*-

"""
1. Multiply every other digit by 2, 
starting with the number’s second-to-last digit, and then add those products' digits together.

2. Add the sum to the sum of the digits that weren’t multiplied by 2.

3. If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), 
the number is valid!
"""


def processNb(nb):
	"different step to get to result"
	if not checkNb(nb):
		print("You have not choosed a proper number.")
		return False
	else:
		card = checkCard(nb)
		nbSliced1 = sepNb1(nb)
		nbSliced2 = sepNb2(nb)
		nbMulti = multNb(nbSliced2)

		nbAdd1 = addNb(nbSliced1)
		nbAdd2 = addNb(nbMulti)
		nbAdd3 = nbAdd1 + nbAdd2

		if int(nbAdd3) % 10 == 0:
			print("You number is a valid number.")
			print("Your card is {}.".format(card))
		else:
			print("Your number is not a valid number.")
		return True

def checkCard(nb):
	"find the card and return it"

	if nb[0] == "4":
		return "Visa"	

	if nb[0] == "6":
		return "Dicover"

	if nb[0] == "3" and nb[1] == "7" or nb[1] == "4":
		return "American Express"

	if nb[0] == "3" and nb[1] == "0" or nb[1] == "8":
		return "Diners Club"

	if nb[0] == "5" and int(nb[1]) in range(1, 6):
		return "MasterCard"

def checkNb(nb):
	"check if the input is number"
	c = 0
	for i in nb:
		if i in list('1234567890'):
			c+=1
	if c == len(nb):
		return True
	else:
		return False

def sepNb1(nb):
	"slice the number to keep every two digit, starting with the last number digit."
	return nb[-1::-2] #return the number sliced

def sepNb2(nb):
	"slice the number to keep every two digit, starting with the number’s second-to-last digit."
	return nb[-2::-2] #return the number sliced


def multNb(nb):
	"Multiply"
	numbers = list(nb)
	multiply = []
	for i in numbers:
		multiply.append(str(int(i)*2))
	return "".join(multiply)

def addNb(nbs):
	number=0 
	for i in nbs:
		number += int(i)
	return number

def askInput():
	"ask user an input"
	flag = False

	while not flag:
		number = input("Give a number to check\n>>>")
		
		flag = processNb(number)


#program

if __name__ == "__main__":
	askInput()

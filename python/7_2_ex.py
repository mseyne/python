# -*- coding:Utf-8 -*-

def ligneCar(n, ca):
	"renvoie n * ca"
	ch = ca * n
	return ch

nb = int(input("Choisissez un nombre que vous souhaitez multiplier\n>>>"))
lt = input("Choisissez un ou plusieurs caractères que vous souhaitez multiplier\n>>>")

print(ligneCar(nb, lt))
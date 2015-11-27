# -*- coding:Utf-8 -*-

a = eval(input("Donnez les deux années bornes vous souhaitez vérifier(séparé par une virgule)"))

def vérif_bissextile(a):
	if not a % 4 and a % 100 or not a % 400:
		print(a, "est une année bissextile.")
	else:
		print(a, "n'est pas une année bissextile.")
	return ("")

for i in range(a[0], a[1]):
	print(vérif_bissextile(i))
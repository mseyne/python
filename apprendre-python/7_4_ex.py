# -*- coding:Utf-8 -*-

def intPar(x):
	for i in range(len(x)):
		x[i] = int(x[i])
	return x

def volBoite(x1, x2, x3):
	"volume parallélépipédique"
	pass


par = input("Donnez les trois valeurs de votre parallélépipède en 3D séparées par une virgule.").split(",")

print(intPar(par))
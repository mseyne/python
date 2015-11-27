# -*- coding:Utf-8 -*-

def intPar(x):
	for i in range(len(x)):
		x[i] = eval(x[i])
	return x

def volBoite(x1, x2, x3):
	"volume parallélépipédique"
	volume = x1 * x2 * x3
	return volume


par = input("Donnez les trois valeurs de votre parallélépipède en 3D séparées par une virgule.").split(",")
par = intPar(par)
vol = volBoite(par[0], par[1], par[2])
print("Le volume du parallélépipède en 3D est :", vol)
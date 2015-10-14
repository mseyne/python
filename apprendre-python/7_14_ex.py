# -*- coding:Utf-8 -*-

def intPar(x):
	for i in range(len(x)):
		x[i] = eval(x[i])
	return x

def volBoite(x1 = 10, x2 = 10, x3 = 10):
	"volume parallélépipédique"
	volume = x1 * x2 * x3
	return volume


par = input("Donnez les trois valeurs de votre parallélépipède en\
 3D séparées par une virgule.\n>>>").split(",")
par = intPar(par)
vol = volBoite(par[0], par[1], par[2])
print("Le volume du parallélépipède en 3D est :", vol)

print(volBoite())
print(volBoite(5.2))
print(volBoite(5.2, 3))
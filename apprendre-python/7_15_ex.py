# -*- coding:Utf-8 -*-

def intPar(x):
	for i in range(len(x)):
		x[i] = eval(x[i])
	return x

def volBoite(x1 = -1, x2 = -1, x3 = -1):
	"volume parallélépipédique"
	if x1 > 0 and x2 > 0 and x3 > 0:
		volume = x1 * x2 * x3
	elif x1 > 0 and x2 > 0 and x3 < 0:
		volume = x1 * x1 * x2
	elif x1 > 0 and x2 < 0 and x3 < 0:
		volume = x1 * x1 * x1
	elif x1 < 0:
		return "error"

	return round(volume, 3)


par = input("Donnez les trois valeurs de votre parallélépipède en\
 3D séparées par une virgule.\n>>>").split(",")
par = intPar(par)
vol = volBoite(par[0], par[1], par[2])
print("Le volume du parallélépipède en 3D est :", vol)

#print(volBoite())
print(volBoite(5.2))
print(volBoite(5.2, 3))
print(volBoite(5.2, 3, 7.4))
# -*- coding:Utf-8 -*-

from math import pi

def surfCercle(R):
	"returne la surface, l'air d'un cercle"
	air = R * R * pi
	return air

ray = float(input("Quelle est le rayon de votre cercle dont vous souhaitez connaitre l'air ?"))
print(surfCercle(ray))
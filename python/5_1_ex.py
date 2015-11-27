# -*- coding:Utf-8 -*-

radian = float(input("Quel est l'angle en radian à convertir?\n>"))

pi = 3.14159265359

degré_convert = radian * 180 / pi
degré = int(degré_convert)
reste_degré = degré_convert - degré
print()
print(degré_convert, degré, reste_degré, '\n')

minutes_convert = reste_degré * 60
minutes = int(minutes_convert)
reste_minutes = minutes_convert - minutes

print(minutes_convert, minutes, reste_minutes, '\n')

secondes_convert = reste_minutes * 60
secondes = round(secondes_convert, 2)
print(secondes_convert, secondes, '\n')

print(radian, "rad correspond à", degré, "°,", minutes, "min,", secondes, "sec.")



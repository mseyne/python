# -*- coding:Utf-8 -*-
pi = 3.14159265359

degré = input("Quel est l'angle en degré à convertir? (format : x,x,x)\n>")
degré_list = degré.split(',')
degré_dict = {}
degré_dict["degrés"] = degré_list[0]
degré_dict["minutes"] = degré_list[1]
degré_dict["secondes"] = degré_list[2]

minutes_convert = int(degré_dict["minutes"]) / 60
secondes_convert = int(degré_dict["secondes"]) / 60
degré_décimal = int(degré_dict["degrés"]) + minutes_convert + secondes_convert
radian_convert = pi * degré_décimal / 180
radian = round(radian_convert, 4)

print(degré_list)
print(degré_dict)
print(minutes_convert, secondes_convert, degré_décimal, '\n')

print(degré_dict["degrés"], '°',degré_dict["minutes"], 'min',
      degré_dict["secondes"], 'sec correspond à', radian, 'radians')

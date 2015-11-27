# -*- coding:Utf-8 -*-
'''Ce programme découpe une réponse en une liste'''

answer = input("donner la largeur, la hauteur et la profondeur d'un\
parallépipède rectangle (séparé et terminé par une virgule)")

al = len(answer) #longueur de string answer
triangle = [] #list avec l, L, p du triangle
c = 0 #compteur
data = "" #data to extract from answer

while c < al:
    s = answer[c]#string to check
    if s != ",":
        data = data + s
    else:
        triangle.append(int(data))
        data=""
    c += 1

l, h, p = triangle[0], triangle[1], triangle[2]
print('largeur :', l, 'hauteur :', h, 'profondeur', p)
volume = l * h * p
print('le volume est de :', volume)

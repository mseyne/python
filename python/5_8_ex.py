# -*- coding:Utf-8 -*-

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
t2 = [ ' Janvier ' , ' Février ' , ' Mars ' , ' Avril ' , ' Mai ' , ' Juin ' , 
' Juillet ' , ' Août ' , ' Septembre ' , 'Octobre ' , ' Novembre ' , ' Décembre ' ]
t3 = []
longueur = len(t1)
compteur = 0

while compteur < longueur:
    t3.append(t1[compteur])
    t3.append(t2[compteur])
    compteur += 1
print(t3)

t4 = ''
for i in t2:
    t4 += i

print(t4)

# -*- coding:Utf-8 -*-
'''
Table de multiplications et vérification de multiples
'''

mul = int(input("multiplier par ? : \n>>>")) #multiplication
mlt = int(input("multiple de ? : \n>>>")) #multiple
nb = int(input("Combien de termes ? : \n>>>"))
c = 0


while c < nb:
    c += 1
    rs = c * mul
    print(c, "x", mul, "=", rs, end='')
    if rs % mlt == 0:
        print("* (multiple de", mlt, end=")\n")
    else:
        print("")

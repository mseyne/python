# -*- coding:Utf-8 -*-

list_nb = [12, 101, 2, 3, 43, 5, 6, 13, 54]
list_nm = ["hallo", "hello", "hoho", "hi", "babacool", "tata"]
nb_grand = 0

for i in list_nb:
    if i > nb_grand:
        nb_grand = i
print(nb_grand)

list_pair = []
list_impair = []

for i in list_nb:
    if i%2 == 0:
        list_pair.append(i)
    else:
        list_impair.append(i)

print(list_pair, list_impair)

list_i4 = [] #inférieur à 4
list_s4 = [] #supérieur à 4

for i in list_nm:
    if len(i) <= 4:
        list_i4.append(i)
    else:
        list_s4.append(i)

print(list_i4, list_s4)

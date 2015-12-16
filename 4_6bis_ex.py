# -*- coding:Utf-8 -*-
'''
Ce programme converti une durée donnée en années,
mois, jours, minutes, secondes en un total en secondes.
'''

answer = input("donner le nombre d'année, de mois, de jours, d'heures,\
de minutes et de secondes que vous souhaitez convertir en\
secondes (6 nombres séparés et terminé par des virgules)")

al = len(answer) #longueur de string answer
key = ['ans', 'mois', 'jours', 'heures', 'minutes', 'secondes'] #list avec ans, mois, jours, heures, minutes et secondes
k = 0 #key position
convert = {} #empty dictionnary
c = 0 #compteur
data = "" #data to extract from answer

while c < al:
    s = answer[c]#string to check
    if s != ",":
        data = data + s
    else:
        convert[key[k]] = int(data)
        data=""
        k += 1
    c += 1

sec_sec = convert['secondes']
sec_ans = convert['ans'] * 31104000
sec_mois = convert['mois'] * 2592000
sec_jour = convert['jours'] * 86400
sec_heur = convert['heures'] * 3600
sec_min = convert['minutes'] * 60
sec_tot = sec_ans + sec_mois + sec_jour + sec_heur + sec_min + sec_sec

print("Dans", convert['ans'], "années,", convert["mois"], "mois,",
      convert["jours"], "jours,", convert['heures'], "heures,",
      convert["minutes"], "minutes et", convert['secondes'], "secondes \
il y a :", sec_tot, "secondes.")

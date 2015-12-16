# -*- coding:Utf-8 -*-

ns = int(input("nombre de secondes à convertir : \n >>>"))

sec_rest = ns%60
minutes = ns//60
min_rest = minutes%60
heures = minutes//60
heu_rest = heures%24
jours = heures//24
jou_rest = jours%30
mois = jours//30
mois_rest = mois%12
ans = mois//12

print("Il y a ", ans, "années,", mois_rest, "mois,", jou_rest,"jours,",heu_rest,"heures,"
      ,min_rest, "minutes et", sec_rest, "secondes dans", ns, "secondes.")


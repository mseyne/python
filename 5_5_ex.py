# -*- coding:Utf-8 -*-

grain_riz_cp = 1 #case précédente
grain_riz_ca = 1 #case actuelle
nb_cases = 64
compteur = 1
riz_total = 0

while compteur <= nb_cases:
    print("Sur la case", compteur, "il y a", grain_riz_ca, "grain(s) de riz.")
    #print("Sur la case", compteur, "il y a", float(grain_riz_ca), "grain(s) de riz.")
    riz_total += grain_riz_ca
    grain_riz_cp, grain_riz_ca = grain_riz_ca, grain_riz_ca + grain_riz_cp
    compteur += 1

print("Au total il y a", riz_total, "grains de riz.")

#arrondi les nombres d'un fichier

fichier1 = open("nombres.txt", "r")
datas = fichier1.readlines()
fichier1.close()

valeurs = []
print(datas)

for data in datas:
	if "\n" in data:
		newData = float(data[:-1])
	else:
		newData = float(data)
	valeurs.append(round(newData))
print(valeurs)

fichier2 = open("nombresR.txt", "w")

for valeur in valeurs:
	fichier2.write(str(valeur)+"\n")

fichier2.close()
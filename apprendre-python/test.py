# -*- coding:Utf-8 -*-

def question(annonce, essais = 4, please = 'Oui ou Non, svp'):
	while essais > 0:
		reponse = input(annonce).lower()
		if reponse in ("o", "oui"):
			return 1
		if reponse in ("n", "non"):
			return 0
		print(please)
		essais +- 1

question("Est-ce que tu veux des haricots ?")
question("Est-ce que tu veux aller sur Mars ?")
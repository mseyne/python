# -*- coding:Utf-8 -*-

notes = {}
while True:
	réponse = input("Quel est le nom de l'élève que vous souhaitez ajouter à la liste ?")
	if réponse == "ok":
		break
	notes[réponse] = int(input("Quel est sa note?"))
	print("Tapez 'ok' lorsque vous avez terminé.")

total = 0
haute = 0
basse = 20

for i in notes:
	print(i, ":", notes[i])
	total += notes[i]
	if notes[i] > haute:
		haute = notes[i]
	elif notes[i] < basse:
		basse = notes[i]

moyenne = total / len(notes)
print("la moyenne est de :", moyenne)
print("la note la plus basse est :", basse)
print("la note la plus haute est :", haute)
# -*- coding:Utf-8 -*-

noms = ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre-Benoit', 'Louise']
notes = [10, 0, 19, 9, 10, 7, 12]
autorisés = list('azertyuiopqsdfghjklmwxcvbni')
c = 0

def transform_note(note):
	x = ''
	if note == 0:
		x = "E"
	elif note > 0 and note < 10:
		x = "D"
	elif note >= 10 and note < 15:
		x = "C"
	elif note >= 15 and note < 18:
		x = "B"
	else:
		x = "A"
	return x

def nombre_lettres(nom):
	x = 0
	for i in nom:
		if i.lower() in autorisés:
			x += 1
	return x

while c < len(noms):
	print(noms[c], " a obtenu :", notes[c], "sur 20 ce qui correspond à un", transform_note(notes[c]))
	print("Il y a", nombre_lettres(noms[c]), "lettres dans le prénom", noms[c], '.')
	c += 1


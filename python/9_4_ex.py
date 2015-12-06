#triple les espaces entre chaque mots

filename = open("multibin.txt", "r")

texte = filename.read()
newText = ""

for letter in texte:
	if letter == " ":
		newText += " "*3
	else:
		newText += letter



filename.close()

print(newText)


# -*- coding:Utf-8 -*-
"Renvoie le nombre de majuscule"

def upperFilter(text):
	"filter words from text and return number"
	listWord = []
	word = ""
	flag = 0
	c = 1

	for letter in text:
		if letter == letter.upper() and letter != " ":
			flag = 1

		if flag == 1 and letter != " ":
			word += letter

		if flag == 1 and letter == " " or flag == 1 and c == len(text):
			listWord.append(word)
			word = ""
			flag = 0
		c += 1
		print(c, len(text))

	return listWord

userInput = input("Choose a sentence:\n>>>")
listWord = upperFilter(userInput)
print(listWord, "il y a", len(listWord))


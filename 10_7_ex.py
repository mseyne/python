"check the occurence of a word in a sentence"

sentence = input("Give a sentence please\n>>>")
word = input("Please give the word to look for\n>>>")
check = ""
occurence = 0
flag = 0
length = 0

for letter in sentence:

	if flag == 0 and letter == word[0]:
		flag = 1
		check += letter #first letter
		length += 1
	
	if flag == 1 and length < len(word):
		print(letter, word[length])
		if letter == word[length]:
			check += letter #next letter
			length += 1

	if check == word:
		occurence += 1
		flag = 0
		check = ""
		length = 0
	print(check, length, flag, letter)

print("The word", word, "occur", occurence, "times in", sentence, ".")
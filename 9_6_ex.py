#check differences between two files

file1 = open("difference1.txt", "r")
file2 = open("difference2.txt", "r")


def checkDatas():
	data1 = file1.read()
	data2 = file2.read()
	if data1 not in data2:
		print("let's check what wrong.")
		checkError()
	else:
		print("file identical.")

def checkError():
	file1.seek(0)
	file2.seek(0)
	data1 = file1.readlines()
	data2 = file2.readlines()
	c = 0
	while c < len(data1) and c < len(data2):
		if data1[c] != data2[c]:
			print("There is an error to line", c+1)
			for letter in data1[c]:
				if letter not in data2[c]:
					print("The letter", letter, "is not in the other file.")
			for letter in data2[c]:
				if letter not in data1[c]:
					print("The letter", letter, "is not in the other file.")
		c+=1


checkDatas()


file1.close()
file2.close()
#create a third file with two others

file1 = open("difference1.txt", "r")
file2 = open("difference2.txt", "r")
file3 = open("fusion.txt", "a")

files = [file1, file2]

def readLines(f):
	'read a line'
	lines = f.readlines()
	return lines

def getLength(txt):
	'return length of file'
	return len(txt)

def writeLine():
	try:
		file3.write(text1[c])
	except IndexError:
		pass

	try:
		file3.write(text2[c])
	except IndexError:
		pass

text1 = readLines(file1)
text2 = readLines(file2)
length1 = getLength(text1)
length2 = getLength(text2)
mxlength = max(length1, length2)

c = 0
while c < mxlength:
	jump="yes"
	try:
		if text1[c] == "\n":
			jump="no"
	except IndexError:
		pass
	try:
		if text2[c] == "\n":
			jump="no"		
	except IndexError:
		pass
	if jump=="yes":
		writeLine()
	c+=1


file1.close()
file2.close()
file3.close()
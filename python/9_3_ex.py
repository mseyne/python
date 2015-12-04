#create multiplication file

import pickle

filename = open("multiplication.txt", "w")
multiple = range(2, 31)
c = 1

for i in multiple:
	filename.write("table of "+str(i)+": ")
	while c <= 20:
		result = i * c
		filename.write(str(c)+"x"+str(i)+"="+str(result)+" ")
		c += 1
	c = 1
	filename.write("\n")


filename = open("multibin.txt", "wb")

print("file created.")
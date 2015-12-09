# add age and birth date to members

"""
bug, should be a different age for each member; find out how much member have been registered and ask for each the correct datas.
"""

DATAS = []
data1 = ["age", ""]
data2 = ["birthdate", ""]
NEWDATAS = []

def copyFile():
	"copy file in datas"
	global DATAS
	memberFile = open("members.txt", "r")
	DATAS = memberFile.readlines()
	memberFile.close()

def askDatas():
	"ask user for new datas"
	global data1, data2
	data1[1] = input("What is the age of the member ?") 
	data2[1] = input("What is the birthdate of the member ?") 

def readDatas():
	"read datas"
	c = 0
	while c < len(DATAS):
		print(DATAS[c])
		NEWDATAS.append(DATAS[c])
		c+=1
		if c % 7 == 0:
			NEWDATAS.append(data1[0]+" : "+data1[1]+"\n")
			NEWDATAS.append(data2[0]+" : "+data2[1]+"\n")
			print(data1[0], ":", data1[1])
			print(data2[0], ":", data2[1])

def writeDatas():
	"write data in new file"
	newFile = open("members2.txt", "w")
	for data in NEWDATAS:
		newFile.write(data)
	newFile.close()

copyFile()
askDatas()
readDatas()
writeDatas()
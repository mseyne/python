# add age and birth date to members

DATAS = []
NEWDATAS = []

def copyFile():
	"copy file in datas"
	global DATAS
	memberFile = open("members.txt", "r")
	DATAS = memberFile.readlines()
	memberFile.close()

def askDatas():
	"ask user for new datas"
	data1 = ["age", ""]
	data2 = ["birthdate", ""]
	data3 = ["sex", ""]
	data1[1] = input("What is the age of the member ?") 
	data2[1] = input("What is the birthdate of the member ?") 
	data3[1] = input("What is the sex of the member ?")
	return [data1, data2, data3]

def newDatas():
	"read datas"
	c = 0
	name = ""

	while c < len(DATAS):
		NEWDATAS.append(DATAS[c])

		if c % 7 == 2 or c % 7 == 3:
			namepart = DATAS[c].split()[2]
			name += namepart+" "

		c+=1

		if c % 7 == 0:
			print(name, ":")
			dataList = askDatas()
			for data in dataList:
				NEWDATAS.append(data[0]+" : "+data[1]+"\n")
			name = ""

def writeDatas():
	"write data in new file"
	newFile = open("members2.txt", "w")
	for data in NEWDATAS:
		newFile.write(data)
	newFile.close()

def readDatas():
	"read the new datas"
	for d in NEWDATAS:
		print(d)

copyFile()
newDatas()
writeDatas()
readDatas()
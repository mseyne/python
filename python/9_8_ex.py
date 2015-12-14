#add in a file, lastname, firstname, adress, phone number, postal code

dictionnary = [["lastname",""], ["firstname",""], ["postal code",""], ["address", ""], ["phone number",""]]
member = 0
DATAS = []


def checkMember():
	'check the number of Member'
	global member
	member = 0
	c = 0
	for data in DATAS:
		c+=1
		if c % 7 == 0:
			member += 1

	print("There is already", member, "members.")

def addMember():
	"ask for the member informations"
	global dictionnary, member
	member += 1
	c = 0
	while c < len(dictionnary):
		data = input("Please give me the "+dictionnary[c][0]+" of the member.\n>>>")
		dictionnary[c][1] = data
		c+=1
	writeFile()

def writeFile():
	"add a member in a file"
	memberfile = open("members.txt", "a")
	memberfile.write("\nMember number : "+"#"+str(member)+"\n============\n")
	for data in dictionnary:
		memberfile.write(data[0]+" : "+data[1]+"\n")
	memberfile.close()

def readFile():
	"read and save the member file"
	global DATAS
	memberfile = open("members.txt", "r")
	DATAS = memberfile.readlines()
	for data in DATAS:
		print(data)
	memberfile.close()
	checkMember()

def menuText():
	print("==============================================")
	print("do you want to add a member or read the list ?")
	print("1. Add a member.")
	print("2. Read list.")
	print("3. Quit.")
	print("==============================================")

def menu():
	menuText()
	answer = ""
	while answer != "3":
		answer = input(">>>")
		if answer == "1":
			addMember()
			menuText()
		if answer == "2":
			readFile()
			menuText()
		if answer == "3":
			pass

if __name__ == "__main__":
	readFile()
	menu()

"find a data in file"

OPTIONS = ["postal code", "address", "phone number", "age", "birthdate", "sex"]
DATAS = []
NAMES = []


def gatherNames():
	"get the names from datas"
	global NAMES
	gather = ""
	name = ""
	c = 0 #append to NAMES when name and lastnam gathered

	for data in DATAS:
		if "firstname" in data:
			gather += data[11:]
			c += 1

		if "lastname" in data:
			gather += data[10:]
			c += 1

		if c == 2:
			for letter in gather:
				if letter not in "\n": #remove the \n
					name += letter
			NAMES.append(name)
			#return to default
			gather, name = "", "" 
			c = 0

def checkInfo(option, ln, fn):
	"check if user input is valid"
	valid = 0
	datas = []
	c = 0

	for data in DATAS:
		if ln in data.lower():
			valid += 1
		if fn in data.lower():
			valid += 1
		if valid == 2 and c < 7: #add all the data related to this member
			datas.append(data)
			c += 1

	if valid == 2:
		pass
	else:
		print("no", ln, fn, "in records.")
	
	if option in OPTIONS:
		valid += 1
	else:
		print("no", option)

	if valid == 3:
		getInfo(option, ln, fn, datas)


def getInfo(option, ln, fn, datas):
	"return the information"
	print("You want to know the", option, "of", ln, fn)
	for data in datas:
		if option in data:
			print(data)

def loadFile():
	global DATAS
	fileSource = open("members2.txt", 'r')
	DATAS = fileSource.readlines()
	fileSource.close()

def menu():
	loadFile() #load datas

	#display all the members names
	gatherNames()
	nb = 1
	for name in NAMES:
		print(nb,':', name)
		nb+=1

	print("What is the lastname of the member you are interested to know about?")
	lastname = input(">>>").lower()

	print("What is the firstname of the member you are interested to know about?")
	firstname = input(">>>").lower()

	print("What data are you interested to know ?")
	for option in OPTIONS[:-1]:
		print(option, end=", ")
	print(OPTIONS[-1]+".")
	option = input(">>>").lower()

	checkInfo(option, lastname, firstname)

if __name__ == "__main__":
	menu()
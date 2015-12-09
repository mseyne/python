"find a data in file"

OPTIONS = ["postal code", "address", "phone number", "age", "birthdate", "sex"]
DATAS = []


def checkInfo(option, name):
	"check if user input is valid"
	print("You want to know the", option, "of", name)
	print("Let's check")
	return True


def getInfo(option, name):
	"return the information"
	print("You want to know the", option, "of", name)
	print("Here it is.")


def readFile():
	fileSource = open("members2.txt", 'r')
	DATAS = fileSource.readlines()
	fileSource.close()
	print(DATAS)

def menu():
	print("What data are you interested to know ?")
	for option in OPTIONS[:-1]:
		print(option, end=", ")
	print(OPTIONS[-1]+".")
	option = input(">>>")

	print("What is the name of the member you are interested to know about?")
	name = input(">>>")
	if checkInfo(option, name):
		getInfo(option, name)

if __name__ == "__main__":
	menu()
	readFile()
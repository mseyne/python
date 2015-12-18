string = input(">>>")
c = 0
nstring = ""
while c < len(string):
	nstring += string[c] + "*"
	c+=1

print(nstring[:-1])


nstring = ""
for letter in string:
	nstring += letter+"*"

print(nstring[:-1])


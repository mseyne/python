# -*- coding:Utf:8 -*-

space = "     "
brick = "#"
c = 0 #counter

while c <= 5:
	print(space + brick + " " + brick)
	brick += "#"
	space = space[1::]
	c += 1
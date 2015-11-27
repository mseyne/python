y = 0
distanceHaute = 0
distanceBasse = 280
flag = "down"

while distanceHaute <= 280:
	if y >= distanceBasse:
		flag = "up"
		distanceHaute += 50

	if y <= distanceHaute:
		flag = "down"

	if flag == "down":
		y += 10

	if flag == "up":
		y -= 10

	print("flag", flag, "y", y, "haut:", distanceHaute,)
	input()
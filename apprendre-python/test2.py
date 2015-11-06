y = 0.
vitesse = 0.20
distanceHaute = 0
distanceBasse = 280
remonte = 2 * 280 / 3
flag = "down"

while distanceHaute >= 0:
	y += vitesse
	if y >= distanceBasse:
		flag = "up"
		vitesse = .20
		distanceHaute = remonte
		remonte = 2 * remonte / 3
	if y <= distanceHaute:
		flag = "down"
		vitesse = -.20
	if flag == "down":
		vitesse += 0.10
	if flag == "up":
		vitesse += -0.10
	print("flag", flag, "y", round(y, 3), "vitesse", round(vitesse, 3), "haut:", round(distanceHaute), "remonte:", round(remonte))
	input()
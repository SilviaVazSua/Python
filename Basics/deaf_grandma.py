

from random import randint

bye = 0

while bye < 3:
	your_message = input("Say something to Grandma:")
	if your_message.isupper():
		x = randint(1930, 1950)
		print("NO, NOT SINCE", x, "!")
		if your_message == "BYE":
			bye += 1
		else:
			bye = 0
	else:
		print("HUH?! SPEAK UP, GIRL!")

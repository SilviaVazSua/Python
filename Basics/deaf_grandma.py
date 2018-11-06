# Whatever you say to Grandma (whatever you type in), she should respond with this: HUH?! SPEAK UP, GIRL! unless you shout it (type in all capitals). If you shout, she can hear you (or at least she thinks so) and yells back: NO, NOT SINCE 1938! Grandma shouts a different year each time, maybe any year at random between 1930 and 1950. You can’t stop talking to Grandma until you shout BYE.

# What if Grandma doesn’t want you to leave? When you shout BYE, she could pretend not to hear you. You have to shout BYE three times in a row. If you shout BYE three times but not in a row, you should still be talking to Grandma.

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

#same as number_to_letter.py but in a function

def ascii_to_letter():  
	for i in range(65, 116):
		if i < 90 or i > 96:
			print(i, " stands for ", chr(i))

ascii_to_letter()

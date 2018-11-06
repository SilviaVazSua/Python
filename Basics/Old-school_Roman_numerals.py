# A method that when passed an integer between 1 and 3000 (or so) returns a string containing the proper old-school Roman numeral. In other words, old_roman_numeral 4 should return 'IIII'.

def int2roman():
	number = input("Enter a number (1 to 3000) in decimal form: ")
	number = int(number)
	numerals = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
	result=""
	for value, numeral in sorted(numerals.items(), reverse=True):
		while number >= value:
			result += numeral
			number -= value
	print (result)

int2roman()

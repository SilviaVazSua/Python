# Rewrite your previous method to return the new-style Roman numerals so when someone calls roman_numeral 4, it should return 'IV', 90 should be 'XC' etc.

def int2roman():
	number = input("Enter a number (1 to 3000) in decimal form: ")
	number = int(number)
	numerals = {1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
	result=""
	for value, numeral in sorted(numerals.items(), reverse=True):
		while number >= value:
			result += numeral
			number -= value
	print (result)

int2roman()

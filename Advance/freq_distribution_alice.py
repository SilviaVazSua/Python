import re # we need to import the Regex module

filename = "alice_in_wonderland.txt"
file = open(filename, encoding="utf8") 

raw = file.read()

def freq_distribution(file):
	results = {} # create empty dictionary
	raw_lower = raw.lower() # everything in lowercase, we want to count all the letter a-z also if they are in capitals.
	raw_lower_sorted = sorted(raw_lower) # we want the final print sorted alphabetically.
	
	freq = 1 # create a counter set to 1
	regex = re.compile('[a-z]') #this search for all the letters a-z, not taking anything else into consideration.

	for char in raw_lower_sorted:
	 	if regex.match(char): #just if it's a letter in lowercase
	 		if char in results.keys():
	 			results[char] += 1
	 		else: 
	 			results[char] = freq

	print("*** Have you ever wondered how many letters are there in your favourite book? Take a look! ***")

	for key in results:
		print(key, ":", results[key])

freq_distribution(file)



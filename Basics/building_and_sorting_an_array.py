# Program that asks us to type as many words as we want (one word per line, continuing until we just press Enter on an empty line) and then repeats the words back to us in alphabetical order. 


print("Enter the number of words you want: ")
words_array = []
words = []

while words != "":
	words = input()
	words_array.append(words)

words_array = sorted(words_array)

print("These are your words in alphabetic order: \n")
	
for i in words_array:
	print (i)	

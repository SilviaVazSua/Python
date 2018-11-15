print("Let's do a trick. Give a message and I\'ll cypher it.' ")
message = input(" >> ")

def string_to_ascii(message):
	message_list = []

	for char in message:
		ascii = ord(char)
		message_list.append(ascii)

	print(message_list)

string_to_ascii(message)
